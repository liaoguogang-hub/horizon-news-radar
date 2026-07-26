---
title: horizon-news-radar（Thysrael/Horizon 中文本地化）· 项目状态卡
date: 2026-07-26
type: 项目状态卡
status: 已 Clone，待部署
local_path: raw/AI/horizon-news-radar/
github: https://github.com/Thysrael/Horizon
tags: [horizon, AI新闻雷达, 项目状态, 克隆]
---

# horizon-news-radar（Thysrael/Horizon）· 项目状态

## 1. 基础信息

| 项目 | 数据 |
|------|------|
| **名称** | Thysrael/Horizon（中文本地化名：horizon-news-radar）|
| **GitHub** | https://github.com/Thysrael/Horizon |
| **Demo** | https://thysrael.github.io/Horizon/ |
| **Star** | 3,100+（2025-7-26）|
| **本地路径** | `raw/AI/horizon-news-radar/` |
| **Clone 时间** | 2026-07-26 |
| **Clone 方式** | `git clone https://github.com/Thysrael/Horizon.git` |

## 2. 项目定位

> "Your own AI-powered news radar. Generates daily briefings in English & Chinese. 用AI 构建你专属的新闻雷达"

## 3. 技术栈（从仓库代码读出）

| 维度 | 技术 |
|------|------|
| **语言** | Python 3.11+ |
| **包管理** | uv（现代 Python 包管理器）|
| **容器化** | Dockerfile（python:3.11-slim）|
| **AI 提供方** | Claude / OpenAI / Azure OpenAI / Google Gemini / MiniMax / DashScope（阿里）/ 豆包 / DeepSeek（默认）|
| **数据源** | GitHub · Hacker News · RSS · GDELT · Google News · OpenBB · Telegram · Twitter/X |
| **AI 评分** | 多 LLM 共识 + 阈值过滤 |
| **CI/CD** | GitHub Actions（`daily-summary.yml` + `deploy-docs.yml`）|
| **扩展协议** | MCP（Model Context Protocol）— `src/mcp/` |
| **内容提取** | trafilatura（开源 web 内容提取）|

## 4. 项目结构（关键目录）

```
horizon-news-radar/
├── .github/workflows/        # GitHub Actions
│   ├── daily-summary.yml    # 每日汇总
│   └── deploy-docs.yml      # 文档部署
├── data/
│   ├── config.example.json  # 配置模板
│   ├── config.github.json   # GitHub 数据源配置
│   └── presets.json         # 预设
├── docs/                     # 文档（含中英 RSS feed）
│   ├── configuration.md
│   ├── extractors.md
│   ├── feed-en.xml
│   └── feed-zh.xml
├── src/
│   ├── ai/                  # AI 处理层（8 个文件）
│   │   ├── analyzer.py
│   │   ├── client.py
│   │   ├── enricher.py
│   │   ├── prompts.py
│   │   └── ...
│   ├── scrapers/            # 数据抓取（5 个源）
│   │   ├── github.py
│   │   ├── hackernews.py
│   │   ├── gdelt.py
│   │   ├── google_news.py
│   │   └── openbb.py
│   ├── extractors/          # 内容提取
│   │   └── trafilatura.py
│   ├── mcp/                 # MCP 协议集成
│   ├── services/
│   ├── storage/
│   ├── orchestrator.py     # 编排
│   ├── models.py            # 数据模型
│   ├── main.py              # 入口
│   └── url_security.py
├── tests/                    # 测试
├── pyproject.toml           # 项目配置
├── uv.lock                  # 依赖锁
├── Dockerfile
└── docker-compose.yml
```

## 5. 默认数据源配置（config.github.json 摘录）

```json
{
  "ai": {
    "provider": "deepseek",
    "model": "deepseek-v4-flash",
    "base_url": "https://api.deepseek.com",
    "api_key_env": "DEEPSEEK_API_KEY",
    "temperature": 0.3,
    "max_tokens": 8192,
    "languages": ["zh", "en"]
  },
  "sources": {
    "github": [
      {"type": "user_events", "username": "karpathy", "enabled": true},
      {"type": "repo_releases", "owner": "vllm-project", "repo": "vllm"},
      {"type": "repo_releases", "owner": "sgl-project", "repo": "sglang"},
      {"type": "repo_releases", "owner": "triton-lang", "repo": "triton"}
    ],
    "hackernews": {"enabled": true, "fetch_top_stories": 30, "min_score": 150},
    "rss": [...]
  }
}
```

> 🎯 **关键发现**：默认数据源已关注 **karpathy 的 GitHub 动态** — 与 B 站视频主题"卡帕西同款知识库"完美对应！

## 6. 部署选项

| 方式 | 成本 | 难度 | 备注 |
|------|------|------|------|
| **GitHub Actions** | 完全免费 | 中 | 推荐（需配置 Secrets）|
| **Docker（自托管）** | 服务器成本 | 低 | NAS / 家用服务器 |
| **本地 Python 运行** | 0 | 中 | 需 `uv sync` |

## 7. 关联资源

- **官方文档**：`README.md`（已 git checkout 恢复至原版）+ `README_zh.md` + `README_ja.md`
- **MCP 协议文档**：`src/mcp/integration.md`
- **配置文档**：`docs/configuration.md`
- **提取器文档**：`docs/extractors.md`
- **Hub 设计文档**：`docs/horizon-hub-design.md`
- **Bilibili 视频**（你分享）："Codex联动Obsidian，搭建卡帕西同款知识库"
  `https://player.bilibili.com/player.html?bvid=BV1MJVb6cETR`

## 8. 下一步行动（待你决策）

1. **读 README_zh.md** — 详细了解部署流程
2. **配置 data/config.github.json** — 改数据源为医药 / 集采 / 行业相关
3. **GitHub Actions 部署** — 推送 .github/workflows 配置
4. **配置 API Key** — DeepSeek（最便宜）/ MiniMax / Claude
5. **集成 MCP** — 接入 vault（Ollama / 本地 LLM）
6. **视频研究** — Karpathy 知识库方法论 → 应用于本项目
