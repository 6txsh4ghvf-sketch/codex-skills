# Data Schema

Default file:

`D:\codex_HyperFrames\yangguan-ai-news-video-template\data\current.json`

## Top-Level Fields

```json
{
  "column_name": "扬关印记",
  "issue_type": "weekly",
  "issue_title": "AI热点观察",
  "subtitle": "扬关印记·数智观察",
  "issue_date": "2026-05-28",
  "disclaimer": "本期内容基于公开来源整理，正式发布前请逐条人工核验。",
  "issue_keywords": ["应用落地", "可信治理", "算力基础"],
  "intro": "最近一周，AI热点集中在行业应用、治理规则与基础设施协同推进。",
  "news_items": [],
  "ending_observation": "AI正在从模型竞争，走向应用、算力与治理协同推进。",
  "footer": "关注AI新趋势，理解数智新变化。"
}
```

## News Item

```json
{
  "title": "国家能源局推进“人工智能+能源”",
  "short_title": "AI+能源推进",
  "source": "中新网",
  "date": "2026-05-26",
  "url": "https://example.com/source",
  "keywords": ["能源", "场景", "应用"],
  "fact": "5月26日，国家能源局在深圳召开全国“人工智能+”能源现场推进会，发布相关报告和高价值场景。",
  "why_matters": "这显示AI应用正在从通用能力展示，进入重点行业的具体场景。",
  "work_relevance": "可关注公开业务场景梳理、流程优化和低风险辅助应用。",
  "screen_text": "AI应用正在进入能源高价值场景",
  "verify_status": "待核验"
}
```

## Field Rules

- `issue_type`: `weekly`, `monthly`, or `single`.
- `news_items`: 3 items for short brief; 7-8 for extended weekly; 4-6 for medium video.
- `short_title`: preferably <= 16 Chinese characters.
- `screen_text`: 18-32 Chinese characters; signal sentence.
- `fact`: dated, subject-led event sentence; can be longer than `screen_text`.
- `why_matters`: why this matters for AI trends.
- `work_relevance`: concise institutional/work/study relevance; not a work deployment.
- `verify_status`: use `待核验` by default; use `已核验` only when the user confirms.
