# Video Style

## Default Format

- 16:9 horizontal.
- 1920x1080.
- 30fps.
- Short brief: about 60 seconds.
- Extended weekly: about 110-120 seconds.

## Visual Identity

- Dark institutional technology style.
- Restrained cyan highlights.
- Radar scan, signal nodes, trend lines, glass-like overlays.
- Clean, sober, credible; not cyberpunk, not marketing, not noisy.
- For high-quality versions, use content-specific background images rather than one generic technology background. The background should be a visual "news scene" derived from the item topic, while all Chinese copy remains editable overlay text.

## Current Preferred Flow

For extended weekly:

1. Cover: "AI热点观察" + date only.
2. News item pages directly; skip standalone "本期雷达" page.
3. Signal summary / trend convergence.
4. Closing observation.

## Cover

- Do not repeat "扬关印记" on cover.
- Use large title and date.
- Keep the frame uncluttered.

## News Page

- Main content must dominate the frame.
- Source/date/verification should be a small information row inside the main text area, not a large top bar.
- Use each news item's dedicated background image as the full-frame base layer.
- Reserve the left 40-45% as a clean text zone; place the main visual subject center-right/right/lower-right.
- Add a dark readability overlay, but keep enough of the scene visible to make the topic recognizable.
- Display:
  - short title
  - keywords
  - `screen_text`
  - `fact`
  - side panel with "关注点" and "工作启发"
- Avoid long paragraphs and tiny text.

## Motion

- Use GSAP timelines.
- Keep transitions calm: data sweep, gentle background zoom, node lighting, subtle line reveals.
- Avoid large shaking, exaggerated zooms, explosion effects, or short-video sticker style.
- Before final answer, run `npm run check`.
