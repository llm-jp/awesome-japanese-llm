---
paths:
  - "README.md"
  - "en/README.md"
  - "fr/README.md"
---

# Table Formatting Rules

- **Parameter size ordering**: Descending order within each section (largest first)
- **Architecture column**: Base architecture name (e.g., "Llama 3.1", "Qwen2.5"), NOT attention mechanisms
- **Multiple sizes**: Combine into single row: `([**7b**](url1), [**13b**](url2))`
- **License format**: Use official names with consistent capitalization
- **Release year bolding**: The latest/newest release year (e.g., the current year) should be **bolded** in the table. When the year is no longer the newest, the bold is removed (see commit history for precedent).
- **Developer column for individuals**: When the developer is an individual (not a company/university/research lab), use the format `個人 (name)` (JA) / `Individual (name)` (EN) / `Individuel (name)` (FR). Do NOT write the HuggingFace username alone.

# Cell Content Formatting

- **Do NOT use bullet-style lists inside table cells.** Avoid leading-hyphen pseudo-lists like `-項目A: 内容<br>-項目B: 内容<br>-項目C: 内容` — these read as Markdown bullets and clutter the table.
- **Preferred patterns for multi-item content within a cell:**
  - **`Label: content<br>Label: content`** — colon-delimited labels without a leading hyphen (e.g., `事前学習: ...<br>Instruction Tuning: ...<br>DPO (instruct3 only): ...`). The label is a training phase, method, or qualifier — not a model variant name.
  - **Prose** — when distinguishing among model variants in the same row (e.g., `-Jagle` / `-FineVision` suffixes), describe the distinction in a single sentence with parenthetical qualifiers, not stacked bullets.
- `<br>` itself is fine for line breaks; the rule is specifically about avoiding `-` at line starts and avoiding repeated label-style rows that mimic bullet lists for model variants.

# Multilingual Consistency

- Update all three files (README.md, en/README.md, fr/README.md) simultaneously
- Same position/order across all versions
- Translations: 不明 → Undisclosed → Non divulgué
