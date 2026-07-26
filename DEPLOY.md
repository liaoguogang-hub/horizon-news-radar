---
title: horizon-news-radar 部署指南（GitHub Actions 免费版 + Docker）
date: 2026-07-26
type: 部署指南
适用: LeoLiao vault · 医药行业雷达配置
字数: ~2,500 中文字符
tags: [horizon, 部署, GitHub Actions, Docker, 医药行业]
---

# horizon-news-radar 部署指南

> **目标**：让 horizon-news-radar（Thysrael/Horizon 中文本地化）每天自动运行，**完全免费**地把中国医药 / 医保 / 集采 / 国际医学动态汇总到 vault。
>
> **核心方案**：**GitHub Actions**（每天定时运行）+ **GitHub Pages**（日报展示）+ **Feishu/Obsidian Webhook**（每日推送）

---

## 一、5 大部署选项对比

| 方式 | 成本 | 难度 | 适用 | 推荐度 |
|------|------|------|------|--------|
| **GitHub Actions** | **完全免费** | 中（需配置 Secrets）| 个人 / 小团队 | ⭐⭐⭐⭐⭐ |
| **Docker（自托管）** | 服务器成本 | 低 | 已有服务器 / NAS | ⭐⭐⭐ |
| **本地 Python 运行** | 0 | 中 | 调试 / 临时使用 | ⭐⭐ |
| **威联通 NAS 部署** | 服务器电费 | 中 | 你的 NAS 环境 | ⭐⭐⭐⭐ |
| **Claude Code 集成** | API 成本 | 低 | 与 Obsidian 协同 | ⭐⭐⭐⭐ |

---

## 二、推荐方案：GitHub Actions（5 步完成）

### 步骤 1：Fork 仓库到自己的 GitHub

```bash
# 方式 A: GitHub 网页操作
# 1. 打开 https://github.com/Thysrael/Horizon
# 2. 点击右上角 Fork
# 3. 仓库名: horizon-news-radar（自定义）

# 方式 B: 本地推送（如果你已有同名空仓库）
cd /d/Obsidian/LeoLiao/raw/AI/horizon-news-radar
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/horizon-news-radar.git
git push -u origin main
```

### 步骤 2：配置 Secrets（API Keys）

在 GitHub 仓库页面：`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

按需配置（最少 1 个 AI key）：

| Secret 名称 | 必填 | 用途 | 推荐 |
|------------|------|------|------|
| `DEEPSEEK_API_KEY` | ⭐ 必填 1 | 默认 AI 提供方 | ✅ **推荐（最便宜）** |
| `OPENAI_API_KEY` | 可选 | GPT 评分 | o3-mini 等 |
| `ANTHROPIC_API_KEY` | 可选 | Claude 评分 | claude-3.5-haiku |
| `GOOGLE_API_KEY` | 可选 | Gemini | gemini-2.0-flash |
| `DASHSCOPE_API_KEY` | 可选 | 阿里 Qwen | 国产替代 |
| `DOUBAO_API_KEY` | 可选 | 字节豆包 | — |
| `MINIMAX_API_KEY` | 可选 | MiniMax | 你已有 |
| `GITHUB_TOKEN` | ⭐ 强烈推荐 | 提高 GitHub API 限速到 5000/h | 自动生成 |
| `APIFY_TOKEN` | 可选 | Twitter 抓取 | 选填 |
| `HORIZON_WEBHOOK_URL` | 可选 | Feishu 飞书机器人 URL | 后续 3.0 配置 |

### 步骤 3：定制 daily-summary-healthcare.yml（已完成）

仓库**已包含**`.github/workflows/daily-summary-healthcare.yml`：

- 默认使用 `data/config.healthcare.json`（医药行业配置）
- 每天 06:30 北京时间（22:30 UTC）自动运行
- 输出到 `docs/` → GitHub Pages 自动部署
- 可手动触发（workflow_dispatch）

启用方法：
1. 推送仓库到 GitHub
2. 进入 `Actions` 标签页
3. 启用 workflows（默认需要手动启用一次）

### 步骤 4：启用 GitHub Pages

1. 仓库 `Settings` → `Pages`
2. Source: **Deploy from a branch**
3. Branch: **gh-pages** / **(root)**
4. 等待 5-10 分钟 → 日报页面可用

### 步骤 5：首次手动运行（验证）

1. `Actions` 标签 → `Daily Horizon Summary (Healthcare Edition)`
2. 点击 `Run workflow` → `Run workflow`
3. 查看运行日志 → 确认无错误
4. 检查 GitHub Pages → 看到首份日报

---

## 三、配置详解（4 类必改 + 2 类选改）

### 必改 1：数据源（修改 `data/config.healthcare.json`）

文件已包含 17 个医药 RSS 源：

- **国家医保局** · 政策法规
- **国家药监局** · 公告通告
- **CDE** · 政策法规
- **集采网** · 公告
- **国家组织高值医用耗材联合采购**
- **中国医药企业管理协会**
- **中国药学会**
- **E 药经理人 / 新康界 / 医药魔方**
- **WHO / FDA / EMA** · 国际机构
- **NEJM / Lancet / Blood / Nature Medicine** · 医学期刊
- **Simon Willison** · AI 跨行业洞察

**自定义数据源**（在 `data/config.healthcare.json` 的 `sources.rss` 数组中）：
```json
{
  "name": "你的源名称",
  "url": "https://example.com/rss.xml",
  "enabled": true,
  "category": "类别标签"
}
```

### 必改 2：AI 提供方

`data/config.healthcare.json` 默认：
```json
"ai": {
  "provider": "deepseek",
  "model": "deepseek-v4-flash",
  ...
}
```

**修改为 MiniMax**（你已有的）：
```json
"ai": {
  "provider": "minimax",
  "model": "MiniMax-Text-01",
  "base_url": "https://api.MiniMax.chat/v1",
  "api_key_env": "MINIMAX_API_KEY",
  ...
}
```

### 必改 3：AI 评分阈值

```json
"filtering": {
  "ai_score_threshold": 7.5,    // 0-10，越高越严格
  "time_window_hours": 48      // 看过去 48 小时的新闻
}
```

- 阈值 7.5：保留约 30-50% 的新闻（推荐）
- 阈值 8.0：更严格，只保留最关键的
- 阈值 7.0：宽松，适合探索期

### 必改 4：关键词

`data/config.healthcare.json` 已包含 30+ 关键词（包括 "罗伐昔替尼" / "芦可替尼" / "吉卡昔替尼" / "贝泽昔替尼"）

**添加你的领域关键词**：
```json
"custom_keywords": [
  "你的领域关键词 1",
  "你的领域关键词 2"
]
```

### 选改 5：Webhook 配置（飞书/钉钉/Slack 推送）

详见 `docs/configuration.md` 中 webhook 部分。

### 选改 6：自定义系统提示词

`data/config.healthcare.json` 中 `ai.system_prompt_suffix`：

```json
"system_prompt_suffix": "你是中国医药行业的资深政策分析师..."
```

**修改为你的领域**（如财务分析、临床研究等）。

---

## 四、Docker 自托管方案（可选）

```bash
# 1. 准备 .env 文件
cd /d/Obsidian/LeoLiao/raw/AI/horizon-news-radar
cp .env.example .env
nano .env   # 填入 DEEPSEEK_API_KEY 等

# 2. 准备 config.json
cp data/config.healthcare.json data/config.json

# 3. Docker 启动
docker-compose up -d

# 4. 验证
docker logs -f horizon-news-radar
```

---

## 五、威联通 NAS 部署方案（你已有 NAS）

参考你之前的部署经验（"威联通NAS部署Claude Code+MiniMax+CC-connect飞书"），在 NAS 上：

```bash
# SSH 登录 NAS
ssh admin@nas-ip

# 用 Container Station 部署 Docker
# 或用 SSH + crontab 每日运行
0 23 * * * cd /volume1/docker/horizon-news-radar && \
  docker run --rm -v $(pwd)/data:/app/data \
  -e DEEPSEEK_API_KEY=xxx horizon-news-radar:latest
```

---

## 六、6 大故障排查

| 问题 | 排查 |
|------|------|
| **Actions 一直失败** | 检查 Secrets 是否正确设置（注意拼写） |
| **RSS 抓取失败** | 用浏览器打开该 RSS URL，看是否 200 OK |
| **AI 评分超时** | 调整 `throttle_sec`（如 2-3）|
| **Webhook 不推送** | 检查 webhook URL 是否含 access_token |
| **日报空白** | `ai_score_threshold` 调低（如 6.5）|
| **GitHub Pages 不显示** | 等待 5-10 分钟；检查 `gh-pages` 分支 |

---

## 七、4 大优化方向（部署后）

1. **MCP 集成** — 推日报到 vault 的特定目录
2. **本地 LLM 替代** — 用 Ollama 跑免费模型
3. **数据源扩展** — 添加更多行业 RSS（按需）
4. **日报订阅** — 用 RSS 订阅器（Feedly、Reeder）订阅 gh-pages

---

## 八、相关文档

- `README.md` · 官方文档
- `docs/configuration.md` · 详细配置文档
- `docs/extractors.md` · 抓取器文档
- `src/mcp/integration.md` · MCP 协议集成
- `PROJECT_STATUS.md` · 项目状态卡
- `data/config.healthcare.json` · 医药行业配置
