# プロジェクト指示（OpenCode / AI アシスタント向け）

このファイルは、このリポジトリを編集する際のルールとガイドラインを定めたものです。主に OpenCode（さくらのAIエンジン経由の Kimi など）およびその他のAIアシスタント向けに作成しています。

Claude-specific な条件付きルールについては `.claude/rules/` を参照してください。

---

## Contributing Rules

See CONTRIBUTING.md for:
- Minimum parameter threshold (≥110M)
- Exclusion of task-specific fine-tuned models
- Dataset/benchmark inclusion criteria

## Model Addition Guidelines

### Section Selection (Most Important)

Models are classified into sections based on training approach. **Evidence is required for classification.**

| Section | Criteria |
|---------|----------|
| スクラッチ学習モデル | Models pre-trained from scratch on Japanese data |
| 海外モデルに日本語で継続事前学習を行ったモデル | **Clear evidence** of continual pre-training on Japanese data (e.g., "Pre-training", "Continual pre-training", "Additional pre-training" in documentation) |
| 海外モデルに日本語で事後学習を行ったモデル（継続事前学習なし、または詳細不明） | Post-training only (SFT/DPO/RL), no continual pre-training, OR **training details unknown** |

**Critical Rules:**
- **When in doubt, use "事後学習のみ、または詳細不明"** - Do NOT assume continual pre-training without evidence
- Check HuggingFace README for explicit statements about training methodology
- "Optimized for Japanese" or "Japanese chat model" alone is NOT evidence of continual pre-training
- Models derived from Japanese continual pre-training models (e.g., Swallow, ELYZA) belong in 継続事前学習 section

### Non-generative (encoder / embedding) models

Encoder / embedding models (BERT, RoBERTa, DeBERTa, ELECTRA, LUKE, BigBird, ModernBERT, **LayoutLM / LayoutLMv2 / LayoutLMv3**, etc.) do **NOT** belong in the generative LLM sections above. They go in the **autoencoding (エンコーダ) section**, which is split into 汎用 and ドメイン特化型.

- Within 汎用, place a new model next to its **architecture family** (e.g., a new LayoutLM variant directly after the existing LayoutLM entry), following the section's existing grouping rather than strict size ordering.
- The table columns differ from the generative tables: `モデル | アーキテクチャ | 最大トークン長 | 学習テキスト | 開発元 | ライセンス | 公開`.
- **最大トークン長 gotcha**: RoBERTa-based models report `max_position_embeddings` with a +2 offset (e.g., `514` → effective **512**). Write the effective length, matching sibling rows.

### Architecture Reference Paper — add alongside the model (easy to forget)

Adding a model and adding its **base architecture's foundational paper** are **one task, not two**. Whenever you add a model, check whether its architecture already has a row in `parts/references_model.md`; if the paper is missing, **add it in the same change** without waiting to be asked.

- Example: adding `layoutlmv3-japanese-preview` requires a **LayoutLMv3** row in `references_model.md`. If absent, add the paper too — do not stop at the model row.
- Only the **architecture / method paper** belongs there (e.g., LayoutLMv3, Qwen3, ModernBERT), NOT every individual Japanese model. A new model whose architecture is already listed needs no reference addition.
- For the references row format/ordering, see the Reference Addition Guidelines below.

### Training Data Column

| Situation | What to write |
|-----------|---------------|
| Training data/method is documented | Specific datasets, methods (e.g., "SFT: dataset-name", "事前学習: corpus-name") |
| Training data/method is unknown | 「不明」(JA) / "Undisclosed" (EN) / "Non divulgué" (FR) |
| **Do NOT write** | Descriptive phrases like "日本語に最適化されたモデル" - this is not training data |

### License Column

Write the official license name (e.g., "Apache 2.0", "Llama 3 Community License", "Sarashina Model NonCommercial License").

**License caveats — add a footnote when the model card restricts use beyond what the license suggests.** Permissive licenses (Apache 2.0, MIT, etc.) imply commercial use is allowed, but model cards often add restrictions in their Limitations / Disclaimers / 利用上の注意 sections (e.g., research-only, no clinical use, contact developer for commercial use). When this gap exists, write the license normally and append a footnote noting the discrepancy.

**How to check:**
- Before adding, scan the model card for sections titled Limitations, Disclaimers, Use Restrictions, 利用上の注意, 制限事項, ご利用にあたって, etc.
- Look for phrases like "研究開発目的のみ", "research and development purposes only", "not for commercial use", "実臨床での利用は推奨しない", "商用利用には連絡が必要"
- For footnote style, mirror an existing `[^n]` footnote in the file.

### Information Verification Checklist

1. **HuggingFace Model tree** (right sidebar): **Authoritative source for `base_model`**. Always check this BEFORE relying on prose in the model card.
2. **HuggingFace config.json**: Parameter count, context length (`max_position_embeddings`)
3. **HuggingFace README**: Training methodology, license, **and Limitations/Disclaimers sections** (cross-check base model against Model tree; check for use restrictions that may warrant a license footnote)
4. **Official announcement/blog**: Release year, developer, training details
5. **LICENSE file**: Full official license name (e.g., "LFM Open License v1.0", not "lfm1.0")

**Base model verification**: Model card prose may list multiple models (e.g., "based on A and B" / "AおよびBをもとに開発") as acknowledgment, even when only one is the technical base. The HuggingFace Model tree's `base_model` field is the structured ground truth — trust it over prose. If the Model tree is gated/inaccessible, ask the user for a screenshot rather than guessing.

**Cross-source verification**: When numeric values (e.g., token counts) appear in multiple sources, always cross-check. HuggingFace READMEs may contain approximations or unit errors (e.g., "~1.8B tokens" vs actual "1.8億トークン" = 0.18B). Prefer official blog posts or papers for precise numbers.

**Press release scope check**: Press releases often describe a model family (e.g., 32B + 8B). Training details quoted from a press release may apply only to the flagship variant. Match each claim to the specific size/variant being added.

**WebFetch summary caveats**: WebFetch returns AI-summarized text that may flatten "based on (acknowledgment)" into "merged/fine-tuned from", conflate future plans with applied techniques, or drop tense. When a summary mentions "merged", "based on multiple", or any training method, re-fetch with a quote-only prompt or read the page directly.

## VLM Addition Guidelines

### VLM Section Classification

Classify each model independently based on its own training approach. Do NOT assume section placement based on other models from the same developer.

| Section | Criteria |
|---------|----------|
| スクラッチ学習モデル | New VLM assembled from an LLM + vision encoder (+ projector) — i.e., a VLM that did not previously exist. The LLM may be Japanese (e.g., LLM-jp, PLaMo, Sarashina) OR foreign (e.g., Phi-4, Qwen3-1.7B); what matters is that the **VLM itself is new**, not pre-existing. Multi-stage training is typical but not required. |
| 海外モデルに日本語で追加学習 | Fine-tuned from an existing foreign VLM (e.g., Qwen2.5-VL, Qwen3-VL, InternVL). If the base model is already a foreign VLM, it belongs here regardless of training scale. |
| マージモデル | VLMs created by merging techniques |

**Critical Rule:** Always check the base model. If a model is fine-tuned from a foreign VLM (e.g., `Qwen3-VL-8B-Thinking`), it belongs in 「海外モデルに日本語で追加学習」, even if other models from the same developer are in a different section.

**Distinguishing scratch vs. foreign-fine-tuned (common source of confusion):**
- Base is a **foreign LLM** (text-only, e.g., Qwen3-1.7B, Phi-4) + vision encoder newly attached → **スクラッチ学習モデル** (the VLM is new, even if the LLM is foreign). Precedents: NABLA-VL (Phi-4 + SigLIP), Jagle-VL (Qwen3-1.7B + SigLIP2), LLM-jp-4-VL (LLM-jp-4 + SigLIP2).
- Base is a **foreign VLM** (already vision-capable, e.g., Qwen2.5-VL, Qwen3-VL, InternVL2) → **海外モデルに日本語で追加学習**. Precedents: KARAKURI VL 2 (Qwen3-VL-8B), Stockmark-DocReasoner (Qwen2.5-VL-32B).

**How to identify the base model:** Use the HuggingFace **Model tree** (right sidebar) — this is the structured ground truth. Do NOT rely solely on model card prose like "○○および△△をもとに開発" / "based on A and B", which often lists multiple models for acknowledgment even when only one is the technical base. See Model Addition Guidelines for the full verification checklist.

### VLM Ordering

- Same parameter size ordering as LLMs (descending)
- Model family similarity does NOT override parameter size

## Benchmark/Tool Addition Guidelines

### Ordering within sections

- Comprehensive tools or frameworks that integrate multiple benchmarks should be placed at the **top** of the section
- Individual benchmarks follow after comprehensive tools

## Table Formatting Rules

- **Parameter size ordering**: Descending order within each section (largest first)
- **Architecture column**: Base architecture name (e.g., "Llama 3.1", "Qwen2.5"), NOT attention mechanisms
- **Multiple sizes**: Use a **separate row per size**, in descending parameter-size order. Do NOT combine multiple sizes into a single row. This rule is about **sizes of one release**; successive versions of the same series are a different case — see the API table section below and check how the existing row for that series is written before splitting it.
- **License format**: Use official names with consistent capitalization
- **Release year bolding**: The latest/newest release year (e.g., the current year) should be **bolded** in the table. When the year is no longer the newest, the bold is removed (see commit history for precedent).
- **Developer column for individuals**: When the developer is an individual (not a company/university/research lab), use the format `個人 (name)` (JA) / `Individual (name)` (EN) / `Individuel (name)` (FR). Do NOT write the HuggingFace username alone.
- **Developer column — canonical organization names**: Use the project's established label for an organization, consistent across all three language files. When unsure, **grep an existing row for the same developer** rather than inventing a label from the HuggingFace org name. Notable case: LLM-jp models use 「大規模言語モデル研究開発センター」(JA) / "Research and Development Center for Large Language Models" (EN) / "Centre de recherche et développement pour les grands modèles de langage" (FR) — NOT "LLM-jp".

### 「APIとして提供されているモデル」 Table

Columns: `モデル | 公開年 | 入出力で扱えるトークン数 | 開発元 | プラットフォーム`. This table has no parameter-size column, so the rules above about size ordering do not apply.

- **Ordering**: by 公開年, **descending** (newest first). Within the same year, keep the existing relative order of rows.
- **One row per model series, not per version.** A new generation of a series already listed (e.g., tsuzumi → tsuzumi 2) goes into the **existing row** as an additional parenthesized link, following the `[series](announcement)<br>([variant](link), [variant](link))` pattern used by Syn / Syn Pro. Do NOT add a second row for it.
- **公開年 of a multi-version row**: the year of the **newest** version listed. Update the existing value when adding a newer version (and apply the bolding rule above).
- **公開年 means the year the developer started offering the model**, not the year it appeared on a particular platform. Example: tsuzumi 2 → 2025 (NTT 提供開始 2025-10-20), even though it reached Microsoft Foundry / Azure Marketplace on 2026-05-20.
- **トークン数**: leave the cell **empty** when the context length is not publicly documented (as with tsuzumi). Do not substitute a figure for a different variant of the same series.

### Cell Content Formatting

- **Do NOT use bullet-style lists inside table cells.** Avoid leading-hyphen pseudo-lists like `-項目A: 内容<br>-項目B: 内容<br>-項目C: 内容` — these read as Markdown bullets and clutter the table.
- **Preferred patterns for multi-item content within a cell:**
  - **`Label: content<br>Label: content`** — colon-delimited labels without a leading hyphen (e.g., `事前学習: ...<br>Instruction Tuning: ...<br>DPO (instruct3 only): ...`). The label is a training phase, method, or qualifier — not a model variant name.
  - **Prose** — when distinguishing among model variants in the same row (e.g., `-Jagle` / `-FineVision` suffixes), describe the distinction in a single sentence with parenthetical qualifiers, not stacked bullets.
- `<br>` itself is fine for line breaks; the rule is specifically about avoiding `-` at line starts and avoiding repeated label-style rows that mimic bullet lists for model variants.

### Link Checker (CI)

The `check-links` workflow runs lychee over the three README files with a bot user agent. Some sites answer bots with 403/415/429 or time out even though the URL is fine in a browser — those are listed in `.lycheeignore`.

- After adding a URL from a host not already in `.lycheeignore`, verify it the way CI will:
  `curl -s -o /dev/null -w "%{http_code}\n" -A "Mozilla/5.0 (compatible; lychee-link-checker)" -L <url>`
- If it fails only for the bot UA, add a `.lycheeignore` entry **in the same change**, following the existing `# Site (reason)` + regex format. Do not swap in a different URL just to appease the checker.

### Multilingual Consistency

- Update all three files (README.md, en/README.md, fr/README.md) simultaneously
- Same position/order across all versions
- Translations: 不明 → Undisclosed → Non divulgué

## Reference (Paper) Addition Guidelines

Chronological tables of foundational papers/methods. Columns: `モデル・手法名 | 日付 | 会議 | 論文リンク`.

> Trigger: this is usually edited as part of a **model addition** — when a model's base architecture is not yet listed, add the architecture paper in the same change. See Model Addition Guidelines ("Architecture Reference Paper").

- **Order**: ascending by 日付; insert at the matching position, don't append.
- **日付**: arXiv v1 submission date as `YYYY.MM.DD` (the `[v1]` timestamp, NOT the publication date). For papers without arXiv, use the document's release date.
- **会議**: publication venue as abbreviation + year (`ACL 2021`, `NeurIPS 2022`, `ACM MM 2022` = ACM Multimedia, `EMNLP 2023 (Findings)`); preprint-only → `-`. Confirm from the arXiv "Comments" / "Journal reference" field, not from memory.
- **論文 link**: ACL Anthology URL if available, else arXiv abstract URL; anchor on the paper's full title.

## Frontend Component Guidelines

### Implement in TypeScript

- New components and theme logic under `.vitepress/` **must be implemented in TypeScript**, not plain JavaScript.
  - Prefer a standalone `.ts` file using `defineComponent` + the `h()` render function over a `.vue` SFC.
  - If a `.vue` SFC is genuinely necessary (e.g. heavy template/scoped-style needs), its script block must use `<script setup lang="ts">`.
- When converting a `.vue` SFC to a `.ts` file, move `<style scoped>` into a sibling `.css` file and import it from `.vitepress/theme/index.mts`. Because the scope is lost, **rename generic transition/animation class names** (e.g. `fade` → a component-specific prefix like `btt-fade`) to avoid clashing with VitePress default-theme styles.
- Annotate function signatures with return types (e.g., `(): void`).
- After changes, verify with `yarn docs:build`.
