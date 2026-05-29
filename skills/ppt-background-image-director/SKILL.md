---
name: ppt-background-image-director
description: Use when creating, selecting, or refining PowerPoint background images for Chinese government/business presentation decks, especially Keynote-style PPTs where background images must support editable Chinese text, reserve clean text areas, avoid generated Chinese text, avoid official uniforms/logos unless explicitly supplied, and map speaker-script sentences or leadership feedback into suitable slide visuals.
---

# PPT Background Image Director

Use this skill when the task involves designing, generating, selecting, or replacing PPT background images for a Chinese government/business deck.

This skill captures the working method developed for leadership-facing PPT revision: realistic base, premium lighting, restrained art direction, clean text zones, and slide-by-slide alignment with the speech script.

## Core Rules

1. Do not put Chinese text into generated background images.
   - Titles, body copy, data, slogans, quotes, labels, and page numbers must remain editable PPT elements.
   - Avoid readable text on screens, boxes, documents, signs, maps, or product packaging.

2. Always reserve a text area.
   - The text zone should be visually quiet, not a crude blank white board.
   - Use low-detail walls, sky, glass, soft gradients, blurred light, shadow, or empty depth.
   - Text must be readable after overlaying normal PPT title/body styles.

3. Keep text-zone placement consistent.
   - Ordinary content pages: reserve left-side main text area and upper title area.
   - Put main visual subjects in the center/right or lower/right.
   - Opening and closing pages may reserve a central title area, but the area must stay clean.

4. Prefer enterprise and scene implication over literal official imagery.
   - Do not generate customs uniforms, badges, official emblems, official seals, government buildings, or fake logos unless the user explicitly requests and supplies authoritative assets.
   - For customs-service themes, express meaning through enterprises, workshops, logistics, testing, digital service, meetings, market expansion, or public-service atmosphere.

5. Style direction.
   - Realistic foundation + premium light + moderate artistic polish + whitespace friendly + Keynote style.
   - High-end, restrained, modern, clean; avoid gaudy, overfilled, cheap AI, stock-photo, or overly dreamy visuals.
   - Do not make the page visually busy behind text.

## Slide Diagnosis Workflow

When revising an existing PPT:

1. Read the PPT and speaker script together when available.
2. Map leadership comments to slide functions:
   - clutter/readability issue: keep theme, simplify background and masks.
   - replacement photo issue: generate or select a new scene.
   - unclear metaphor issue: make the visual subject more direct.
   - template issue: fix layout, title position, font hierarchy, and mask consistency.
   - quote/conclusion issue: usually needs layout and typography, not only a photo.
3. Note whether the user is using actual slide numbers or visible page markers; verify before replacing if numbering is offset.
4. For each target slide, decide:
   - Is this a cover, chapter opener, content page, case page, data page, quote page, or closing page?
   - Where should editable text go?
   - What visual evidence or metaphor should appear?
   - Which elements must be excluded?

## Background Types

Use these common mappings:

- Cover: clean central or left-center title zone, strong but uncluttered city/port/enterprise visual, clear room for logo if the user supplies one.
- Chapter opener: bold visual subject on right, large quiet title zone on left, minimal secondary detail.
- Enterprise immersion: production line, workshop, export goods, business staff from side/back, no official uniforms.
- Policy/service delivery: enterprise meeting, documents/tablets with unreadable abstract charts, factory/warehouse nearby, practical communication.
- E-commerce/logistics: warehouse, parcels, cross-border platform atmosphere, product flow; avoid fake brand text.
- Service radius/map: unlabeled map-like network, nodes/arcs/radiation, no readable geography labels unless added later in PPT.
- Testing/certification: lab equipment, inspection instruments, sample materials, clean technical light.
- Digital service/AI: service terminal, abstract interface glow, enterprise user context; no readable UI text.
- Summary/conclusion: converging paths, port/logistics/lab/digital-service horizon, broad and calm, suitable for a large quote.

## Image Prompt Pattern

For generated images, include:

```text
Create a 16:9 PowerPoint Keynote-style background image for [deck/theme].
Theme: [slide meaning].
Scene: [specific realistic visual].
Composition: left 40-45% clean low-detail area for editable Chinese text; upper left clean title zone; main visual subject center-right/right/lower-right.
Style: realistic, premium cinematic lighting, restrained, high-end, modern, uncluttered, subtle depth of field.
Exclusions: no readable text, no Chinese characters, no logos, no brand names, no official uniforms, no badges, no emblems, no official symbols, no fake screens with text.
```

Adjust composition for cover/closing pages:

```text
Composition: center or center-left clean area for a large editable title/quote, with visual energy around the edges or right side.
```

## Selection Checklist

Before recommending or inserting a background:

- Does it follow the no-text/no-logo rule?
- Is the reserved text zone actually clean enough?
- Is the subject aligned with the speaker-script sentence, not just pretty?
- Is the metaphor direct enough for leadership to understand quickly?
- Does it avoid official imagery unless provided by the user?
- Will it still work after adding PPT title/body text?
- Is it visually consistent with nearby slides?
- If two slides use similar scenes, can one be cropped or regenerated to avoid repetition?

## PPT Integration Guidance

When editing a PPT:

- Keep original PPT untouched; work on a copy.
- Insert the new background as a full-slide image behind editable text.
- Prefer deleting/replacing only the old full-slide background picture; keep user-supplied logos and editable text unless asked to change them.
- After replacement, render slide previews and inspect readability.
- Adjust masks, title positions, and text color only after seeing the rendered result.

## Output Style

When reporting to the user:

- Group backgrounds by slide or sentence.
- Say which image best fits which page and why in one short sentence.
- Flag risks such as generated readable text, brand marks, repeated imagery, or weak text zones.
- Provide local file paths and contact sheets when available.
