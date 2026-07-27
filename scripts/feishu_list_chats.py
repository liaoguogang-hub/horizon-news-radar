#!/usr/bin/env python3
"""One-shot helper: list Feishu chats the bot is in.

Usage:
    uv run python scripts/feishu_list_chats.py --app-id "cli_xxx" --app-secret "xxx"

Output: prints a table of chats the bot has access to, so you can find
the chat_id (oc_xxx) for the group you want to push to.
"""

import argparse
import json
import urllib.error
import urllib.request


FEISHU_BASE = "https://open.feishu.cn/open-apis"


def get_tenant_access_token(app_id: str, app_secret: str) -> str:
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
        raise RuntimeError(f"Failed to get token: {body}")
    return body["tenant_access_token"]


def list_chats(token: str) -> dict:
    """List all chats the bot is in (up to 50)."""
    url = f"{FEISHU_BASE}/im/v1/chats?page_size=50"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"   ❌ HTTP {e.code}: {body[:1000]}", file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(description="List Feishu chats the bot is in")
    parser.add_argument("--app-id", required=True)
    parser.add_argument("--app-secret", required=True)
    args = parser.parse_args()

    print(f"🔑 Getting tenant_access_token...")
    token = get_tenant_access_token(args.app_id, args.app_secret)
    print(f"   ✓ token acquired (len={len(token)})\n")

    print(f"📋 Listing chats...")
    result = list_chats(token)

    if result.get("code") != 0:
        print(f"❌ Failed: {result}")
        return 1

    items = result.get("data", {}).get("items", [])
    if not items:
        print("⚠️  No chats found. Did you add the bot to a group yet?")
        print("   → In Feishu: group → group settings → bots → add bot → search your app → add")
        return 0

    print(f"\n{'Chat ID':<28} {'Type':<8} {'Name':<30} {'Description'}")
    print("-" * 100)
    for chat in items:
        chat_id = chat.get("chat_id", "?")
        chat_type = chat.get("chat_type", "?")
        name = chat.get("name", "(no name)")
        desc = chat.get("description", "")[:30]
        print(f"{chat_id:<28} {chat_type:<8} {name:<30} {desc}")

    print(f"\n💡 Copy the chat_id (oc_xxx) of your target group → use as FEISHU_CHAT_ID")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main() or 0)