# codex-skills

Personal Codex skills.

## Skills

- `customs-compile-reference`: evaluate foreign-language source materials, prepare article outlines, extract translation highlights, and review drafts for customs compilation reference work.
- `gongwen-format`: format messy Word `.docx` files into Chinese gongwen document style and produce clean `.docx` / `.pdf` deliverables.
- `ppt-background-image-director`: create, select, and refine text-friendly Keynote-style PPT background images for Chinese government/business presentations.
- `yangguan-ai-news-video`: research, structure, visually design, preview, and render "扬关印记" AI热点资讯 videos with HyperFrames, including content-specific background images.
- `yangzhou-trade-watch`: monitor, verify, structure, and transform public international trade and economic information for Yangzhou foreign trade analysis briefs.

## Local Installation

Clone or download this repository, then copy the desired skill folders under `skills/` into your local Codex skills directory:

```powershell
git clone https://github.com/6txsh4ghvf-sketch/codex-skills.git
Copy-Item -Recurse .\codex-skills\skills\* "$env:USERPROFILE\.codex\skills\"
```

After copying, restart Codex so it can discover the new skills.
