---
name: Tech News Brief
description: Gather and summarize near real-time technology news from public feeds/search. Use when user asks for tech news, AI news, startup/engineering trends, or periodic tech brief push in Chinese.
---

# Tech News Brief

Collect latest technology headlines and output a short Chinese brief.

## Workflow

1. Pull latest items (prefer multiple sources):
   - Hacker News top/new
   - Tech media RSS (as available)
   - Web search for breaking items (if needed)
2. De-duplicate by URL/title.
3. Keep only last 24h–48h high-signal items.
4. Output in Chinese with:
   - 标题
   - 一句话摘要
   - 来源链接
   - 影响点评（1句）

## Output Template

- 今日科技快讯（时间）
- 1) 标题
  - 摘要：...
  - 影响：...
  - 链接：...

Keep it concise (5-10 items unless user asks otherwise).
