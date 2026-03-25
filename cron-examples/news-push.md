# 新闻推送 Cron 示例

这份示例记录了新闻推送在 OpenClaw 中的稳定做法，重点是**图文推送不要依赖本地 MEDIA 路径**，而应优先使用可直接访问的远程图片 URL。

## 为什么这样做

在隔离 cron 会话里，如果输出类似：

```text
MEDIA:./output/news-media/example.jpg
```

很容易触发：

```text
LocalMediaAccessError: Local media path is not under an allowed directory
```

更稳的做法是让任务直接输出：

```text
MEDIA:https://example.com/image.jpg
```

这样可以绕开本地媒体白名单问题。

---

## 单条图文推送（推荐）

适合在 12:00 / 22:00 的短时间窗口内，按固定间隔逐条推送重大新闻。

### Prompt 模板

```text
你是新闻发送器。每次运行只发送1条新闻，且必须是【1张图片 + 1条新闻文字】的单条消息，不得包含第二条。
严格输出模板（只允许这4行）：
MEDIA:https://...
标题：...
摘要：...
原文链接：https://...

硬约束：
1) 第一行必须是新闻封面图的真实可访问 HTTPS 图片地址，格式必须是 MEDIA:https://... 。
2) 不得下载到本地路径，不得输出 MEDIA:./... 或任何本地文件路径。
3) 不得输出任何总览、编号、列表、队列说明。
4) 不得输出“封面图：https://...”这类普通文本，第一行必须直接是 MEDIA:https://... 。
5) 抓不到可直接访问的封面图就换新闻，直到有图。
6) 优先科技/AI/芯片/互联网平台/宏观/市场/能源/利率/政策重大新闻。
7) 避免与本任务最近已发标题重复。
```

### 推荐 cron

```text
0,2,4,6,8,10,12,14,16,18 12,22 * * *
```

时区建议：

```text
Asia/Shanghai
```

---

## 每日摘要图文推送

适合中午 / 晚上定时汇总 10 条新闻。

### Prompt 模板

```text
你是新闻发送器，不是总结器。输出时禁止任何总览、前言、后记、队列说明。严格输出10条（科技5+财经5），每条都必须按以下模板连续输出：
MEDIA:https://...
标题：...
摘要：...
原文链接：https://...

硬约束：
1) 每条第一行必须是该新闻封面图的真实可访问 HTTPS 图片地址，格式必须是 MEDIA:https://... 。
2) 不得下载到本地路径，不得输出 MEDIA:./... 或任何本地文件路径。
3) 每条第2行起才是标题/摘要/链接。
4) 不允许输出“封面图：https://...”或任何图片URL文本代替第一行 MEDIA。
5) 不允许把10条先写成新闻文本再统一放图片。
6) 抓不到图就丢弃该条并换一条，直到凑满10条。
7) 时间窗口按 Asia/Shanghai：12:00 取当天 00:00-12:00；22:00 取当天 12:00-22:00。
8) 避免重复旧闻，优先重大科技、AI、芯片、互联网平台、宏观、市场、能源、利率、政策相关新闻。
```

### 推荐 cron

```text
0 12,22 * * *
```

---

## 相关 skill

可搭配这些 skill 使用：

- `news-summary`
- `tech-news-brief`
- `market-news-brief`

---

## 排障经验

### 1. 如果日志出现 ENOENT 找不到 skill
先确认运行环境里的 workspace 是否正确，尤其留意是否误指向：

```text
/home/istoreos/.openclaw/workspace
```

而实际 skill 可能在：

```text
/mnt/data_sda4/openclaw/data/.openclaw/workspace
```

### 2. 如果日志出现 LocalMediaAccessError
优先改成远程：

```text
MEDIA:https://...
```

不要继续依赖本地 `MEDIA:./...`。

### 3. 如果日志提示 rg not found
说明运行环境缺少 ripgrep，需要额外安装，或修改 skill 避免依赖 `rg`。
