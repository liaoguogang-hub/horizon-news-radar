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
    token: str, chat_id: str, title: str, markdown_content: str, link_url: str | None = None
) -> dict:
    """Send an interactive card message to a Feishu chat.

    Returns the parsed JSON response from Feishu.
    """
    elements: list[dict] = [
        {"tag": "markdown", "content": markdown_content[:MAX_CONTENT_CHARS]}
    ]
    if link_url:
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "查看完整日报 → GitHub Pages"},
                        "url": link_url,
                        "type": "primary",
                    }
                ],
            }
        )

    card = {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": title},
            "template": "blue",
        },
        "elements": elements,
    }

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


def main():
    parser = argparse.ArgumentParser(
        description="Send Horizon daily report to Feishu via Open API"
    )
    parser.add_argument("--report", required=True, help="Path to daily report .md file")
    parser.add_argument("--app-id", required=True, help="Feishu app_id (cli_xxx)")
    parser.add_argument("--app-secret", required=True, help="Feishu app_secret")
    parser.add_argument("--chat-id", required=True, help="Feishu chat_id (oc_xxx)")
    parser.add_argument(
        "--pages-base",
        default="https://liaoguogang-hub.github.io/horizon-news-radar",
        help="Base URL of the GitHub Pages deployment (for the 'view full report' button)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.report):
        print(f"⚠️  Report not found: {args.report}", file=sys.stderr)
        print("   (skipped — Horizon may have produced no items today)", file=sys.stderr)
        sys.exit(0)

    # 从文件名提取日期（文件名格式：YYYY-MM-DD-summary-zh.md）
    filename = os.path.basename(args.report)
    # e.g. "2026-07-27-summary-zh.md" -> "2026-07-27"
    date_str = filename.split("-summary-")[0] if "-summary-" in filename else filename.replace(".md", "")

    with open(args.report, encoding="utf-8") as f:
        content = f.read()

    # 截断（飞书 markdown element 单元素 4K 上限）
    summary = content
    truncated = False
    if len(content) > MAX_CONTENT_CHARS:
        summary = content[:MAX_CONTENT_CHARS]
        truncated = True

    # 标题
    title = f"📡 Horizon 医药日报 · {date_str}"

    # GitHub Pages 链接：指向根 URL（永远 200，永不 404）
    # 之前用 /YYYY/MM/DD/summary-zh.html，依赖 Pages 实时构建状态
    # 现在用根 URL：用户在首页可看到 7 天内所有 summary
    gh_pages_link = args.pages_base.rstrip("/")

    # 获取 token + 发送
    try:
        token = get_tenant_access_token(args.app_id, args.app_secret)
        result = send_interactive_card(
            token=token,
            chat_id=args.chat_id,
            title=title,
            markdown_content=summary,
            link_url=gh_pages_link,
        )
    except Exception as e:
        print(f"❌ Feishu send failed: {e}", file=sys.stderr)
        sys.exit(1)

    if result.get("code") == 0:
        msg_id = result.get("data", {}).get("message_id", "?")
        print(f"✅ Feishu webhook sent: msg_id={msg_id}")
        if truncated:
            print(f"   (truncated to {MAX_CONTENT_CHARS} chars — see full report at {gh_pages_link})")
    else:
        print(f"❌ Feishu webhook failed: {result}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()