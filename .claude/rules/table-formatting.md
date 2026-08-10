---
paths:
  - "README.md"
  - "en/README.md"
  - "fr/README.md"
---

# Table Formatting Rules

- **Parameter size ordering**: Descending order within each section (largest first)
- **Architecture column**: Base architecture name (e.g., "Llama 3.1", "Qwen2.5"), NOT attention mechanisms
- **Multiple sizes**: Use a **separate row per size**, in descending parameter-size order. Do NOT combine multiple sizes into a single row. This rule is about **sizes of one release**; successive versions of the same series are a different case — see the API table section below and check how the existing row for that series is written before splitting it.
- **License format**: Use official names with consistent capitalization
- **Release year bolding**: The latest/newest release year (e.g., the current year) should be **bolded** in the table. When the year is no longer the newest, the bold is removed (see commit history for precedent).
- **Developer column for individuals**: When the developer is an individual (not a company/university/research lab), use the format `個人 (name)` (JA) / `Individual (name)` (EN) / `Individuel (name)` (FR). Do NOT write the HuggingFace username alone.
- **Developer column — canonical organization names**: Use the project's established label for an organization, consistent across all three language files. When unsure, **grep an existing row for the same developer** rather than inventing a label from the HuggingFace org name. Notable case: LLM-jp models use 「大規模言語モデル研究開発センター」(JA) / "Research and Development Center for Large Language Models" (EN) / "Centre de recherche et développement pour les grands modèles de langage" (FR) — NOT "LLM-jp".

# 「APIとして提供されているモデル」 Table

Columns: `モデル | 公開年 | 入出力で扱えるトークン数 | 開発元 | プラットフォーム`. This table has no parameter-size column, so the rules above about size ordering do not apply.

- **Ordering**: by 公開年, **descending** (newest first). Within the same year, keep the existing relative order of rows.
- **One row per model series, not per version.** A new generation of a series already listed (e.g., tsuzumi → tsuzumi 2) goes into the **existing row** as an additional parenthesized link, following the `[series](announcement)<br>([variant](link), [variant](link))` pattern used by Syn / Syn Pro. Do NOT add a second row for it.
- **公開年 of a multi-version row**: the year of the **newest** version listed. Update the existing value when adding a newer version (and apply the bolding rule above).
- **公開年 means the year the developer started offering the model**, not the year it appeared on a particular platform. Example: tsuzumi 2 → 2025 (NTT 提供開始 2025-10-20), even though it reached Microsoft Foundry / Azure Marketplace on 2026-05-20.
- **トークン数**: leave the cell **empty** when the context length is not publicly documented (as with tsuzumi). Do not substitute a figure for a different variant of the same series.

# Cell Content Formatting

- **Do NOT use bullet-style lists inside table cells.** Avoid leading-hyphen pseudo-lists like `-項目A: 内容<br>-項目B: 内容<br>-項目C: 内容` — these read as Markdown bullets and clutter the table.
- **Preferred patterns for multi-item content within a cell:**
  - **`Label: content<br>Label: content`** — colon-delimited labels without a leading hyphen (e.g., `事前学習: ...<br>Instruction Tuning: ...<br>DPO (instruct3 only): ...`). The label is a training phase, method, or qualifier — not a model variant name.
  - **Prose** — when distinguishing among model variants in the same row (e.g., `-Jagle` / `-FineVision` suffixes), describe the distinction in a single sentence with parenthetical qualifiers, not stacked bullets.
- `<br>` itself is fine for line breaks; the rule is specifically about avoiding `-` at line starts and avoiding repeated label-style rows that mimic bullet lists for model variants.

# Link Checker (CI)

The `check-links` workflow runs lychee over the three README files with a bot user agent. Some sites answer bots with 403/415/429 or time out even though the URL is fine in a browser — those are listed in `.lycheeignore`.

- After adding a URL from a host not already in `.lycheeignore`, verify it the way CI will:
  `curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0 (compatible; lychee-link-checker)" -L <url>`
- If it fails only for the bot UA, add a `.lycheeignore` entry **in the same change**, following the existing `# Site (reason)` + regex format. Do not swap in a different URL just to appease the checker.

# Multilingual Consistency

- Update all three files (README.md, en/README.md, fr/README.md) simultaneously
- Same position/order across all versions
- Translations: 不明 → Undisclosed → Non divulgué
