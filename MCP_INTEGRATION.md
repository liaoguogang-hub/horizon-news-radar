---
title: horizon-news-radar × LeoLiao vault · MCP 集成方案
date: 2026-07-26
type: 集成设计
适用: RealClaudian 插件 + Obsidian vault
字数: ~3,000 中文字符
tags: [horizon, MCP, Obsidian, Claudian, 集成, 医药雷达]
---

# horizon-news-radar × LeoLiao vault · MCP 集成方案

> **目标**：让 horizon-news-radar（医药行业 AI 新闻雷达）通过 **MCP（Model Context Protocol）** 协议与 Obsidian vault 双向联动：
> 1. **日报自动写入 vault**（无需手动复制）
> 2. **vault 内 Claudian 工具可调用 Horizon 实时查询**
> 3. **关键词触发的"研究助理"功能**

---

## 一、4 大集成目标

| 目标 | 价值 | 实现方式 |
|------|------|---------|
| **① 日报自动入库** | 每天 vault 有新内容 | Cron + Webhook 推送到 vault 目录 |
| **② 实时查询** | vault 内 Claudian 调用 horizon 工具 | MCP 协议 |
| **③ 关键词触发** | 提到"集采"时自动拉相关 | Webhook + 规则引擎 |
| **④ 双向引用** | vault 内可 wikilink 到 Horizon 日报 | 文件路径 + 双向链接 |

---

## 二、方案 1：日报自动入库（推荐先做）

### 2.1 推送路径设计

```
horizon-news-radar  →  GitHub Actions（每日 22:30 UTC）
   ↓ 自动生成 docs/daily/2026-07-26.md
   ↓ Webhook 推送（可选：飞书/钉钉）
   ↓ Obsidian 插件接受
   ↓ 写入 vault 目录
```

### 2.2 vault 接受目录

| 类型 | 路径 |
|------|------|
| 每日日报 | `raw/AI/horizon-news-radar/日报/2026-07-26-医药日报.md` |
| 月度汇总 | `raw/AI/horizon-news-radar/月报/2026-07.md` |
| 重要事件标记 | `02.内刊/转载/Horizon医药日报/2026-07-26-XXX.md` |

### 2.3 3 步实现

**步骤 1**：在 `.github/workflows/daily-summary-healthcare.yml` 中追加 push 步骤：

```yaml
      - name: Push daily report to vault via Obsidian Git
        if: env.HORIZON_WEBHOOK_URL != ''
        run: |
          git config user.name "horizon-bot"
          git config user.email "horizon@bot.local"
          git clone https://x-access-token:${{ secrets.VAULT_TOKEN }}@github.com/USER/LEOLIAO-VAULT.git /tmp/vault
          mkdir -p /tmp/vault/raw/AI/horizon-news-radar/daily
          cp docs/daily/2026-07-26.md /tmp/vault/raw/AI/horizon-news-radar/daily/
          cd /tmp/vault
          git add .
          git commit -m "📡 Horizon Healthcare Daily Report: ${{ env.DATE }}"
          git push origin main
```

**步骤 2**：设置 `VAULT_TOKEN` Secret（在 GitHub）：
- 创建一个 GitHub PAT（Personal Access Token），有 `repo` 权限
- 在 Actions Secrets 中设 `VAULT_TOKEN`

**步骤 3**：接受 webhook 推送（如不用 Git）：
- 飞书机器人：自动转发消息到 vault 同步目录
- 钉钉机器人：类似
- 邮件：每日发送日报到指定邮箱

---

## 三、方案 2：MCP 协议实时调用（高级）

### 3.1 Horizon MCP server 配置

参考 `src/mcp/integration.md`，启动 MCP server：

```bash
cd /d/Obsidian/LeoLiao/raw/AI/horizon-news-radar
uv run horizon-mcp
```

### 3.2 暴露的 MCP 工具（推测 + 建议）

| 工具名 | 功能 | 输入 | 输出 |
|--------|------|------|------|
| `horizon_search_news` | 按关键词搜索新闻 | query, days | JSON 列表 |
| `horizon_get_today` | 获取今日日报 | date | Markdown 内容 |
| `horizon_get_top` | 获取今日 Top 5 重要新闻 | limit | JSON 列表 |
| `horizon_filter_by_source` | 按来源过滤 | source, days | JSON 列表 |
| `horizon_summarize_url` | 对单条新闻做深度摘要 | url | Markdown 摘要 |

### 3.3 集成到 RealClaudian（vault 内的 Claudian 插件）

`~/.claude.json` 或 `~/.claudian/settings.json` 配置：

```json
{
  "mcpServers": {
    "horizon": {
      "command": "uv",
      "args": ["run", "horizon-mcp"],
      "cwd": "D:\\Obsidian\\LeoLiao\\raw\\AI\\horizon-news-radar"
    }
  }
}
```

之后在 Obsidian Claudian chat 中可以直接调用：

> 用户：「今日医药行业的医保政策更新」
> Claudian → 调 horizon_get_today → 拿最新日报 → 整合到回答

### 3.4 集成到 Claude Code（CLI）

`~/.claude.json`：
```json
{
  "mcpServers": {
    "horizon": {
      "command": "uv",
      "args": ["run", "horizon-mcp"],
      "cwd": "D:\\Obsidian\\LeoLiao\\raw\\AI\\horizon-news-radar"
    }
  }
}
```

---

## 四、方案 3：关键词触发的"研究助理"

### 4.1 场景示例

> 用户在 vault 写笔记：
> "今天和医保局开会，讨论了**集采降价 20%** 的政策..."

自动触发：
1. Webhook 接收消息
2. 通过 horizon_search_news(query="集采降价") 拉取相关新闻
3. 自动插入到当前笔记底部

### 4.2 实现

需要外部触发器（如 vault 自动监听 + horizon_search_news）：

```python
# 在 vault 端的监听脚本
import re
from claude_code import call_mcp_tool

def on_note_save(content):
    keywords = re.findall(r'(集采|医保|药监|罗伐昔替尼|吉卡昔替尼)', content)
    if keywords:
        results = call_mcp_tool("horizon", "horizon_search_news", 
                                {"query": "+".join(keywords), "days": 7})
        # 把 results 插入到笔记底部
        content += "\n\n## 自动拉取的最新新闻\n" + results
        save(content)
```

---

## 五、5 大集成场景

### 场景 1：早晨 8 点自动看新闻

- GitHub Actions 22:30 UTC（北京时间 06:30）运行
- 生成日报 docs/daily/2026-07-26.md
- 自动入库到 vault
- 你打开 vault 就能看

### 场景 2：vault 内的 Claudian chat 实时查询

- 你在 Obsidian 内问：「最近医保集采有什么新消息？」
- Claudian 调 horizon_get_today(days=7)
- 整合到回答里

### 场景 3：飞书 bot 推送

- Horizon webhook 推送到飞书群机器人
- 团队成员在飞书看到每日医药雷达
- 点击链接跳转到 vault 详细日报

### 场景 4：vault 笔记自动引用

- 在写《集采策略分析》笔记时
- 用 `[[raw/AI/horizon-news-radar/日报/2026-07-26-医药日报|今日医药日报]]` 引用
- Obsidian 自动 wikilink

### 场景 5：Claude Code + vault 协同

- Claude Code 在 vault 内编码
- 通过 MCP 调用 horizon_search_news 拉取实时数据
- 写入 vault 笔记

---

## 六、3 步启动集成（推荐路径）

### 步骤 1：本地测试 MCP server（30 分钟）

```bash
cd /d/Obsidian/LeoLiao/raw/AI/horizon-news-radar
uv run horizon-mcp
# 应该看到 MCP server 启动消息
```

### 步骤 2：配置 .claudian/settings.json

```json
{
  "mcpServers": {
    "horizon": {
      "command": "uv",
      "args": ["run", "horizon-mcp"],
      "cwd": "D:\\Obsidian\\LeoLiao\\raw\\AI\\horizon-news-radar"
    }
  }
}
```

### 步骤 3：vault 内测试

打开 Obsidian → 启动 Claudian → 问：
> "用 horizon 工具查一下今天的医药新闻"

应该返回 5-10 条新闻 + 简明摘要。

---

## 七、vault 内相关文件位置

| 文件 | 用途 |
|------|------|
| `raw/AI/horizon-news-radar/DEPLOY.md` | 部署指南（你已创建）|
| `raw/AI/horizon-news-radar/data/config.healthcare.json` | 医药行业配置（已配置）|
| `raw/AI/horizon-news-radar/PROJECT_STATUS.md` | 项目状态卡（已创建）|
| `raw/AI/horizon-news-radar/.github/workflows/daily-summary-healthcare.yml` | 医药 workflow（已创建）|
| `raw/AI/horizon-news-radar/src/mcp/integration.md` | Horizon MCP 设计（已读）|

---

## 八、4 大未来增强方向

1. **本地 LLM（Ollama）** 替代云端 API（完全免费）
2. **双 MCP server** — 加上 `news-summary-mcp` 提供更深度摘要
3. **vault 自动分类** — 用 vault 内 dataview + 关键词自动归类日报条目
4. **3 大 vault 关联** — 02.内刊/转载/ + 03.工作报告/ + raw/AI/horizon-news-radar/ 三方交叉引用

---

## 九、关键代码位置（如要扩展）

| 文件 | 用途 |
|------|------|
| `src/mcp/server.py` | MCP server 入口 |
| `src/mcp/horizon_adapter.py` | 适配 Horizon 内部 API |
| `src/mcp/service.py` | MCP 服务实现 |
| `src/ai/prompts.py` | AI prompts（可改医药行业 prompt）|
| `src/ai/analyzer.py` | AI 评分逻辑 |
| `data/config.healthcare.json` | 医药配置 |

---

## 总结

**最简集成路径（推荐）**：
1. ✅ 第 1 周：配置 GitHub Actions + 启用 daily-summary-healthcare.yml + GitHub Pages
2. ✅ 第 2 周：vault 内创建日报目录，让日报自动入库
3. ✅ 第 3 周：配置 MCP 到 .claudian，让 vault 内 Claudian 实时查询
4. ✅ 长期：维护关键词 + 数据源 + 飞书 bot 推送

**5 大预期收益**：
- 每天节省 30-60 分钟医药行业信息搜集时间
- 团队成员在飞书群即可看到日报
- vault 内 Claudian chat 可调实时数据
- 笔记自动引用日报（双向链接）
- 长期形成"医药行业知识库"
