# Content-Driven Backgrounds

Use this workflow when the user wants a polished AI news video, says the visual quality matters, or asks for backgrounds/images that match each news item.

## Decision

Prefer updating the existing HyperFrames video project instead of creating a separate slideshow or image-only artifact. The goal is:

`news content -> dedicated background image -> editable text overlay -> rendered video`

## Successful Pattern

1. Finalize the news item list first.
2. For each item, identify the visual category:
   - industry application: factory, energy, logistics, lab, enterprise workflow
   - governance/safety: policy room, security operations, transparency, audit, risk review
   - infrastructure/model capability: chips, data centers, fiber optics, model/network nodes
   - summary/closing: convergence paths, city/data horizon, signal map
3. Generate or select one dedicated 16:9 background per news item.
4. Copy backgrounds into the project, for example:

```text
public/assets/backgrounds/generated-news/news-01-energy.png
public/assets/backgrounds/generated-news/news-02-legislation.png
...
```

5. Bind backgrounds by news order in `src/app.js`, using explicit file paths rather than relying only on generic keyword classes.
6. Keep all Chinese text as HTML/CSS overlay: title, source, date, keywords, facts, verification status, captions.
7. Run `npm run check`.
8. Render and extract contact-sheet frames for visual QA.

## Prompt Template

```text
Create one 16:9 cinematic background image for a Chinese AI news video item about [specific news topic].
No readable text, no Chinese characters, no logos, no brand names, no official uniforms, no badges, no emblems, no fake UI text.
Scene: [specific visual scene tied to the item].
Composition: left 45 percent clean dark low-detail area for editable Chinese text; main visual subject center-right/right/lower-right.
Style: realistic foundation, premium cinematic lighting, restrained high-end modern technology news aesthetic, deep navy and charcoal base, cyan light accents, subtle warm gold highlights, uncluttered, subtle depth of field.
```

## Wiring Pattern

Keep the mapping simple and auditable:

```javascript
const newsBackgrounds = [
  "./public/assets/backgrounds/generated-news/news-01-energy.png",
  "./public/assets/backgrounds/generated-news/news-02-legislation.png",
];
```

Each generated scene object should carry its image path:

```javascript
{
  kind: "news",
  item,
  image: newsBackgrounds[index],
  html: renderNewsCard(item, index, "weekly extended"),
}
```

Then apply it to the background layer:

```javascript
const imageStyle = scene.image ? ` style="background-image:url('${scene.image}')"` : "";
return `<div class="scene-bg"${imageStyle} data-layout-ignore></div>`;
```

## Visual QA

After rendering, extract representative frames:

```powershell
ffmpeg -y -ss 00:00:08 -i renders\latest.mp4 -frames:v 1 renders\review\frame-01.jpg
```

Check:

- The correct news item uses the correct background.
- The left text zone remains readable.
- The background contains no readable generated text or logos.
- The subject is visible enough after the dark overlay.
- Different news items do not feel like repeated generic tech wallpaper.

## Lessons From The Successful Version

- Content-specific backgrounds made the video feel like each news item had its own visual scene.
- The unified style came from repeating composition rules, not from reusing the same image.
- Keeping Chinese text out of the generated image avoided乱码 and made later editing easy.
- A contact sheet was the fastest way to confirm the sequence worked before presenting the video.
