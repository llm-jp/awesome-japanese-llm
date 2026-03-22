---
globs: ["README.md", "en/README.md", "fr/README.md"]
---

# Table Formatting Rules

- **Parameter size ordering**: Descending order within each section (largest first)
- **Architecture column**: Base architecture name (e.g., "Llama 3.1", "Qwen2.5"), NOT attention mechanisms
- **Multiple sizes**: Combine into single row: `([**7b**](url1), [**13b**](url2))`
- **License format**: Use official names with consistent capitalization
- **Release year bolding**: The latest/newest release year (e.g., the current year) should be **bolded** in the table. When the year is no longer the newest, the bold is removed (see commit history for precedent).
- **Developer column for individuals**: When the developer is an individual (not a company/university/research lab), use the format `個人 (name)` (JA) / `Individual (name)` (EN) / `Individuel (name)` (FR). Do NOT write the HuggingFace username alone.

# Multilingual Consistency

- Update all three files (README.md, en/README.md, fr/README.md) simultaneously
- Same position/order across all versions
- Translations: 不明 → Undisclosed → Non divulgué
