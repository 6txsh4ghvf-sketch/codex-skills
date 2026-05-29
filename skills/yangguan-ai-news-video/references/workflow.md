# Workflow

## 1. Scope

Default assumptions:

- Time range: recent week, based on the user's timezone/date.
- Video type: `weekly`.
- Item count: 7-8 for an extended weekly video; 3 for a short brief.
- Aspect ratio: 16:9, 1920x1080.
- Output: preview first, no render unless explicitly requested.

If the user says "开始制作本期 AI热点资讯", first collect candidates. Do not write `data/current.json` until the user confirms selected items.

## 2. Research

Search separately for:

- China AI policy, governance, industry applications, large models, compute, products.
- International AI company/product updates, governance/safety, infrastructure, research.

Use source priority:

1. Official government/agency/company/research sources.
2. Reputable media and wire services.
3. Industry media only as supplement.

Record each candidate:

- title
- source
- date
- url
- concise fact
- why it matters
- suitability for institutional display
- verification status

## 3. Candidate Review

Return a table before editing files. Recommend a balanced set, but let the user approve.

Good 8-item mix:

- 3-4 domestic China items.
- 3-4 international items.
- At least one governance/safety item.
- At least one industry application item.
- At least one infrastructure/model capability item.

## 4. Production

After approval:

1. Back up `data/current.json` to `data/archive/YYYY-MM-DD-current-backup.json`.
2. Write approved items to `data/current.json`.
3. For polished videos, generate one dedicated background image per news item and wire the image paths into the scene data. Follow `references/content-driven-backgrounds.md`.
4. Run the validation script.
5. Run `npm run check`.
6. Start or reuse preview:

```powershell
cd D:\codex_HyperFrames\yangguan-ai-news-video-template
npm run dev -- --port 3019
```

Return:

- project path
- preview URL
- selected item list
- audit checklist
- render command, but do not render unless asked

If the user explicitly asks to see a finished video without intermediate approval, render a visual sample after `npm run check`, but keep source/content status as `待核验`.

## 5. Rendering

Only render after the user confirms content and source review.

```powershell
cd D:\codex_HyperFrames\yangguan-ai-news-video-template
npm run render -- --output output\YYYY-MM-DD-yangguan-ai-news.mp4 --fps 30 --quality standard
```
