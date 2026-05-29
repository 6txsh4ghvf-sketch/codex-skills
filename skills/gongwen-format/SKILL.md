---
name: gongwen-format
description: Format messy Word `.docx` documents into Chinese 公文基本格式 and export clean `.docx` plus `.pdf` deliverables. Use when the user asks to adjust, normalize, typeset, or 排版 a Word document as 公文格式/公文基本格式/机关公文格式, especially files placed on the Desktop or another accessible folder.
---

# Gongwen Format

## Workflow

Use this skill with the `documents` skill whenever possible, because final output must be a verified Word document and PDF.

1. Locate the source `.docx` and preserve it unchanged.
2. Copy or create a new output file with a clear suffix such as `_公文格式.docx`; never overwrite the source unless the user explicitly asks.
3. Read `references/basic-gongwen-format.md` before editing.
4. Inspect the document structure and classify the main title, body paragraphs, first- through fourth-level headings, ending phrase, signature/date block, notes, attachments, and page numbers.
5. For ordinary single-file cleanup, prefer `scripts/format_gongwen_docx.py input.docx output.docx` as the starting deterministic formatter, then make any document-specific fixes.
6. Apply styles through Word styles or deterministic OOXML/docx operations rather than ad hoc visual edits. Keep content wording unchanged unless the user asks for text edits.
7. Export a PDF copy from the formatted DOCX.
8. Render and visually inspect pages if the document tooling is available. Iterate until title wrapping, spacing, page numbers, attachments, and body text are clean.
9. Deliver only the new `.docx` and `.pdf` unless the user asks for QA artifacts.

## Formatting Rules

Use the detailed baseline in `references/basic-gongwen-format.md`. Key requirements:

- Page margins: top 3.8 cm, bottom 3.5 cm, left/right 2.7 cm.
- Main title: 方正小标宋_GBK, 二号, centered, fixed 30 pt line spacing.
- Body: 方正仿宋_GBK, 三号, justified, fixed 28 pt line spacing, character spacing compressed 0.2 pt.
- Arabic numbers and English text: Times New Roman, 三号.
- Body paragraphs and numbered heading paragraphs use a two-character first-line indent, except recipient/addressee lines such as `各科室、各部门：`.
- Heading ladder:
  - `一、...`: 方正黑体_GBK, 三号.
  - `（一）...`: 方正楷体_GBK, 三号 for the heading text. If body content follows in the same paragraph after the heading sentence, keep that following content as 方正仿宋_GBK, 三号.
  - `1. ...`: 方正仿宋_GBK, 三号, bold, add one space after the number.
  - `（1）...`: 方正仿宋_GBK, 三号.
- Signature/date block: normally placed after three blank body lines.
- Page numbers: odd pages bottom right, even pages bottom left, 宋体四号 half-width style like `— 1 —`.
- Attachments: attachment marker at the first line of the text area, 黑体三号; attachment title centered on the third line; attachment body follows body formatting.

## Judgment Rules

- Preserve the user's original meaning, paragraph order, and evidence. This skill is for formatting, not rewriting.
- If a heading level is ambiguous, infer from numbering patterns first; otherwise keep it as body text and mention the uncertainty.
- Use official 公文 punctuation conventions where formatting requires it, but do not silently rewrite substantive wording.
- If required fonts are not installed, still set the DOCX font names to the required families and disclose any render-time font substitution risk.
- Do not generate or label the document as a verified formal filing unless the user explicitly provides human-reviewed content and asks for finalization.

## Final Response

Report completion status, created `.docx` and `.pdf` file paths, any skipped or uncertain items such as missing fonts or failed visual render QA, and a concise next-step suggestion when manual review is still needed.
