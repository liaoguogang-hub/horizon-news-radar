#!/usr/bin/env python3
"""Send Horizon daily report to Feishu via Open API.

Usage:
    uv run python scripts/feishu_notify.py \\
        --report docs/daily/2026-07-27.md \\
        --app-id "$FEISHU_APP_ID" \\
        --app-secret "$FEISHU_APP_SECRET" \\
        --chat-id "$FEISHU_CHAT_ID"

Required env / Secrets:
    FEISHU_APP_ID       — from open.feishu.cn → 应用 → 凭证
    FEISHU_APP_SECRET   — from open.feishu.cn → 应用 → 凭证
    FEISHU_CHAT_ID      — chat_id (格式 oc_xxx)，从群 open chat_id API 拿

API doc: https://open.feishu.cn/document/server-docs/im-v1/message/create
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request


FEISHU_BASE = "https://open.feishu.cn/open-apis"
MAX_CONTENT_CHARS = 4000  # 飞书 markdown element 单元素 4K 限制
MAX_RETRIES = 2


def get_tenant_access_token(app_id: str, app_secret: str) -> str:
    """Exchange app_id + app_secret for tenant_access_token."""
    url = f"{FEISHU_BASE}/auth/v3/tenant_access_token/internal"
    payload = json.dumps({"app_id": app_id, "app_secret": app_secret}).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        body = json.loads(resp.read().decode())
    if body.get("code") != 0:
        raise RuntimeError(f"Failed to get tenant_access_token: {body}")
    return body["tenant_access_token"]


def send_interactive_card(
    token: str, chat_id: str, title: str, card: dict
) -> dict:
    """Send an interactive card message to a Feishu chat.

    The card dict is built by `build_feishu_card()` containing all elements
    (header + per-news-item links + footer).

    Returns the parsed JSON response from Feishu.
    """
    payload = {
        "receive_id": chat_id,
        "msg_type": "interactive",
        "content": json.dumps(card, ensure_ascii=False),
    }

    url = f"{FEISHU_BASE}/im/v1/messages?receive_id_type=chat_id"
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    last_err: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            body_text = e.read().decode(errors="replace")[:500]
            last_err = RuntimeError(f"HTTP {e.code}: {body_text}")
            if e.code < 500:  # 4xx 不重试
                break
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
    raise RuntimeError(f"Feishu API failed after {MAX_RETRIES + 1} attempts: {last_err}")


def parse_news_items(content: str, max_items: int = 15) -> list[dict]:
    """Parse Horizon daily summary .md into individual news items.

    Horizon's format (table-of-contents style):
        1. [新闻标题](#item-1) ⭐️ 8.0/10
        2. [下一条新闻](#item-2) ⭐️ 8.0/10
        ...

    Horizon's format (per-item section):
        <a id="item-1"></a>
        ## [Title](URL) ⭐️ Score/10

        summary text...

        source · feed · date · [discussion](url)

        ---

    Note: The .md 摘要 uses **anchor links** (#item-N), not the original article URL.
    The original URL is only in the rendered HTML.

    Returns list of dicts: {index, title, url, score, summary, source}
    """
    items = []
    # 1) Parse the table-of-contents list (1. [title](#item-N) ⭐️ Score/10)
    # Note: ⭐️ is 2 unicode chars (⭐ + variation selector). Use ⭐️? pattern.
    toc_pattern = re.compile(
        r"^\s*(\d+)\.\s+\[([^\]]+)\]\(#(item-\d+)\)\s*⭐️?\s*([\d.]+|N/A|\?)\s*/\s*10",
        re.MULTILINE,
    )

    # 2) Parse detailed sections: <a id="item-N"></a>\n## ... \n\nsummary \n\n source\n\n---\n\n
    # Build map: anchor -> summary text
    section_pattern = re.compile(
        r'<a id="(item-\d+)"></a>\s*\n\s*##\s*\[?[^\]\n]*\]?\(?[^\)\n]*\)?[^\n]*\n+\s*([^\n]+(?:\n[^\n]+){0,8}?)(?=\n\n|\n---|\Z)',
        re.MULTILINE,
    )
    anchor_to_summary = {}
    for sm in section_pattern.finditer(content):
        anchor_to_summary[sm.group(1)] = sm.group(2).strip()

    for m in toc_pattern.finditer(content):
        index = int(m.group(1))
        title = m.group(2).strip()
        anchor = m.group(3).strip()
        score = m.group(4).strip()

        # Get the actual summary text (from detailed section, not next TOC line)
        item_summary = anchor_to_summary.get(anchor, "")
        # Clean markdown: remove links but keep text
        item_summary = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", item_summary)
        # Remove other markdown artifacts
        item_summary = item_summary.replace("⚡️", "").replace("⚡", "")
        # Truncate to 200 chars
        item_summary = item_summary[:200].strip()

        items.append({
            "index": index,
            "title": title,
            "anchor": anchor,
            "url": "",
            "score": score,
            "summary": item_summary,
        })
        if len(items) >= max_items:
            break
    return items


def build_feishu_card(date_str: str, news_items: list[dict], gh_pages_base: str) -> dict:
    """Build Feishu interactive card with each news item as clickable markdown.

    Each news title links to: {gh_pages_base}/YYYY/MM/DD/summary-zh.html#item-N
    User clicks → lands on GitHub Pages summary at that news section,
    where the original article URL is available in the HTML.
    """
    elements: list[dict] = []

    # Header line
    elements.append({
        "tag": "markdown",
        "content": (
            f"**📡 Horizon 医药日报 · {date_str}**\n\n"
            f"> 共 {len(news_items)} 条要闻，点击标题直接跳到原文位置"
        ),
    })

    # Each news item as separate markdown element
    # Link to GitHub Pages summary at the item's anchor
    year, month, day = date_str.split("-")
    summary_page_url = (
        f"{gh_pages_base.rstrip('/')}/{year}/{month}/{day}/summary-zh.html"
    )

    for item in news_items:
        # 直接用锚点 URL 跳到该条新闻在 GitHub Pages 的位置
        item_url = f"{summary_page_url}#{item['anchor']}"
        title_link = f"[{item['title']}]({item_url})"
        summary_clean = item["summary"] or "（无摘要）"
        content_block = (
            f"**⭐️ {item['score']}/10** · {title_link}\n"
            f"_{summary_clean}_"
        )
        elements.append({
            "tag": "markdown",
            "content": content_block[:MAX_CONTENT_CHARS],
        })

    # Footer
    elements.append({
        "tag": "markdown",
        "content": f"📚 [全部 7 天日报]({gh_pages_base.rstrip('/')}/) · [RSS 订阅]({gh_pages_base.rstrip('/')}/feed-zh.xml)",
    })

    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": f"📡 Horizon 医药日报 · {date_str}"},
            "template": "blue",
        },
        "elements": elements,
    }


def main():
    import re  # imported here to keep module top-level clean

    parser = argparse.ArgumentParser(
        description="Send Horizon daily report to Feishu via Open API (each news as clickable link)"
    )
    parser.add_argument("--report", required=True, help="Path to daily report .md file")
    parser.add_argument("--app-id", required=True, help="Feishu app_id (cli_xxx)")
    parser.add_argument("--app-secret", required=True, help="Feishu app_secret")
    parser.add_argument("--chat-id", required=True, help="Feishu chat_id (oc_xxx)")
    parser.add_argument(
        "--pages-base",
        default="https://liaoguogang-hub.github.io/horizon-news-radar",
        help="Base URL of the GitHub Pages deployment",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=15,
        help="Maximum news items to send (default 15, fit within Feishu 50K element limit)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.report):
        print(f"⚠️  Report not found: {args.report}", file=sys.stderr)
        print("   (skipped — Horizon may have produced no items today)", file=sys.stderr)
        sys.exit(0)

    # 从文件名提取日期
    filename = os.path.basename(args.report)
    date_str = filename.split("-summary-")[0] if "-summary-" in filename else filename.replace(".md", "")

    with open(args.report, encoding="utf-8") as f:
        content = f.read()

    # 解析每条新闻
    news_items = parse_news_items(content, max_items=args.max_items)
    if not news_items:
        print(f"⚠️  No news items parsed from {args.report}", file=sys.stderr)
        sys.exit(0)

    # 构建飞书卡片
    gh_pages_link = args.pages_base.rstrip("/")
    card = build_feishu_card(date_str, news_items, gh_pages_link)

    title = f"📡 Horizon 医药日报 · {date_str}"

    # 获取 token + 发送
    try:
        token = get_tenant_access_token(args.app_id, args.app_secret)
        result = send_interactive_card(
            token=token,
            chat_id=args.chat_id,
            title=title,
            card=card,
        )
    except Exception as e:
        print(f"❌ Feishu send failed: {e}", file=sys.stderr)
        sys.exit(1)

    if result.get("code") == 0:
        msg_id = result.get("data", {}).get("message_id", "?")
        print(f"✅ Feishu webhook sent: msg_id={msg_id}")
        print(f"   ({len(news_items)} news items as clickable links)")
    else:
        print(f"❌ Feishu webhook failed: {result}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()