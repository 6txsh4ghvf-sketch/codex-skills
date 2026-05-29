---
name: yangguan-ai-news-video
description: Produce "扬关印记" AI热点资讯 videos with HyperFrames. Use when the user asks to create, plan, research, update, preview, render, or visually upgrade an AI news/hotspot/weekly/monthly observation video; when the user asks to collect recent domestic and international AI news for a video; when the video should use AI-generated or content-specific background images; or when working in the yangguan-ai-news-video-template project.
---

# 扬关 AI热点资讯视频

Use this skill to produce a verified, sober, data-driven AI news video from recent public sources. The default output project is:

`D:\codex_HyperFrames\yangguan-ai-news-video-template`

## Core Workflow

1. **Clarify scope only if missing.** Determine time range, video type, and target length. Defaults: recent week, `weekly`, 7-8 items, 16:9, 1920x1080, 110-120 seconds.
2. **Research with browsing.** Search domestic and international AI news within the requested range. Use official sources, government/agency sites, company blogs, reputable media, research institutions, papers, or standards bodies.
3. **Return candidates first unless the user explicitly says to proceed without confirmation.** Candidate lists should include title, source, date, link, summary, why it matters, suitability, and verification status.
4. **After approval or explicit go-ahead, back up data.** Copy `data/current.json` to `data/archive/YYYY-MM-DD-current-backup.json`.
5. **Write `data/current.json`.** Use the schema in `references/data-schema.md`. Mark all items `待核验` unless the user explicitly confirms they are verified.
6. **Design content-specific backgrounds when visual quality matters.** For polished videos, create one 16:9 background per news item, plus cover/summary/closing backgrounds as needed. Keep all Chinese text editable in HTML/CSS; never bake Chinese text into generated images. See `references/content-driven-backgrounds.md`.
7. **Check and preview.** Run `npm run check`, then start or reuse `npm run dev -- --port 3019`. Provide the Studio URL.
8. **Render only after audit unless the user explicitly asks for a sample or final render.** Require source/date/content review before formal MP4 export.

## Research Rules

- Always browse for recent AI news; do not rely on memory.
- Cover both China and international news unless the user requests otherwise.
- Prefer 3-4 domestic items and 3-4 international items for an 8-item extended weekly video.
- Include at least one governance/safety item, one industry application item, and one infrastructure/model capability item when available.
- Do not invent news, links, dates, sources, companies, data, or quotations.
- Avoid vague subjects: write dated, attributed sentences such as "5月22日，国家发展改革委新闻发言人李超表示..." instead of "相关方面表示..." when the source supports it.

## Writing Rules

- Each item must answer "what happened" without needing narration.
- Use dated, subject-led news sentences: "5月26日，国家能源局在深圳召开..."
- Avoid AI-ish filler such as "公开报道显示" unless no better attribution exists.
- Keep tone sober, institutional, clear, and non-promotional.
- Keep `screen_text` as a signal sentence and `fact` as a concrete dated event sentence.
- See `references/content-rules.md` for compression and audit rules.

## Video Defaults

- Visual style: dark, restrained technology, radar/signal language, glass panels, cyan highlights.
- Prefer the content-driven background workflow for polished videos: the news content decides the background scene, and the video layout overlays editable Chinese text.
- Background images must contain no readable Chinese text, no logos, no fake UI labels, no official emblems, and no uniforms unless the user supplies authoritative assets.
- Cover: only "AI热点观察" and date; avoid repeating "扬关印记".
- Weekly extended flow: cover -> news items -> signal summary -> closing.
- Skip standalone "本期雷达" pages for extended weekly videos.
- News page priority: large headline and event explanation; source/date should be a small information row, not a large top bar.
- See `references/video-style.md` for layout decisions.

## Useful References

- `references/workflow.md`: detailed end-to-end procedure.
- `references/data-schema.md`: JSON structure and examples.
- `references/content-rules.md`: source, safety, and writing constraints.
- `references/video-style.md`: visual and timing rules.
- `references/content-driven-backgrounds.md`: successful workflow for generating news-specific backgrounds and wiring them into the video.

## Useful Script

Run this after editing `data/current.json`:

```powershell
python C:\Users\admin\.codex\skills\yangguan-ai-news-video\scripts\validate_current_json.py D:\codex_HyperFrames\yangguan-ai-news-video-template\data\current.json
```

The script checks required fields, rough text length limits, item counts, and verification status.
