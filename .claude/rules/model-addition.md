---
paths:
  - "README.md"
  - "en/README.md"
  - "fr/README.md"
---

# Model Addition Guidelines

## Section Selection (Most Important)

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

## Training Data Column

| Situation | What to write |
|-----------|---------------|
| Training data/method is documented | Specific datasets, methods (e.g., "SFT: dataset-name", "事前学習: corpus-name") |
| Training data/method is unknown | 「不明」(JA) / "Undisclosed" (EN) / "Non divulgué" (FR) |
| **Do NOT write** | Descriptive phrases like "日本語に最適化されたモデル" - this is not training data |

## License Column

Write the official license name (e.g., "Apache 2.0", "Llama 3 Community License", "Sarashina Model NonCommercial License").

**License caveats — add a footnote when the model card restricts use beyond what the license suggests.** Permissive licenses (Apache 2.0, MIT, etc.) imply commercial use is allowed, but model cards often add restrictions in their Limitations / Disclaimers / 利用上の注意 sections (e.g., research-only, no clinical use, contact developer for commercial use). When this gap exists, write the license normally and append a footnote noting the discrepancy.

**How to check:**
- Before adding, scan the model card for sections titled Limitations, Disclaimers, Use Restrictions, 利用上の注意, 制限事項, ご利用にあたって, etc.
- Look for phrases like "研究開発目的のみ", "research and development purposes only", "not for commercial use", "実臨床での利用は推奨しない", "商用利用には連絡が必要"

**Existing precedents** (consult these for footnote style):
- `[^13]` — KARAKURI LM: 商用利用には開発元への直接連絡が必要
- `[^14]` — マージモデル: 研究および教育を目的とした利用を念頭に置く
- `[^25]` — SIP-med-LLM: 研究開発目的のみでの使用想定、実臨床利用は非推奨

## Information Verification Checklist

1. **HuggingFace Model tree** (right sidebar): **Authoritative source for `base_model`**. Always check this BEFORE relying on prose in the model card.
2. **HuggingFace config.json**: Parameter count, context length (`max_position_embeddings`)
3. **HuggingFace README**: Training methodology, license, **and Limitations/Disclaimers sections** (cross-check base model against Model tree; check for use restrictions that may warrant a license footnote)
4. **Official announcement/blog**: Release year, developer, training details
5. **LICENSE file**: Full official license name (e.g., "LFM Open License v1.0", not "lfm1.0")

**Base model verification**: Model card prose may list multiple models (e.g., "based on A and B" / "AおよびBをもとに開発") as acknowledgment, even when only one is the technical base. The HuggingFace Model tree's `base_model` field is the structured ground truth — trust it over prose. If the Model tree is gated/inaccessible, ask the user for a screenshot rather than guessing.

**Cross-source verification**: When numeric values (e.g., token counts) appear in multiple sources, always cross-check. HuggingFace READMEs may contain approximations or unit errors (e.g., "~1.8B tokens" vs actual "1.8億トークン" = 0.18B). Prefer official blog posts or papers for precise numbers.

**Press release scope check**: Press releases often describe a model family (e.g., 32B + 8B). Training details quoted from a press release may apply only to the flagship variant. Match each claim to the specific size/variant being added.

**WebFetch summary caveats**: WebFetch returns AI-summarized content that can:
- Conflate future plans ("will utilize X") with applied techniques ("used X")
- Flatten "based on (acknowledgment)" into "merged from / fine-tuned from"
- Drop tense and conditional markers
When a WebFetch summary mentions "merged", "based on multiple", or any training method, re-fetch with a quote-only prompt or read the page directly to verify.
