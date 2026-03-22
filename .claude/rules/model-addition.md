---
globs: ["README.md", "en/README.md", "fr/README.md"]
---

# Model Addition Guidelines

## Section Selection (Most Important)

Models are classified into sections based on training approach. **Evidence is required for classification.**

| Section | Criteria |
|---------|----------|
| スクラッチ学習モデル | Models pre-trained from scratch on Japanese data |
| 海外モデルに日本語で継続事前学習を行ったモデル | **Clear evidence** of continual pre-training on Japanese data (e.g., "Pre-training", "Continual pre-training", "Additional pre-training" in documentation) |
| 海外モデルに日本語で追加学習を行ったモデル（事後学習のみ、または詳細不明） | Post-training only (SFT/DPO/RL), OR **training details unknown** |

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

## Information Verification Checklist

1. **HuggingFace config.json**: Parameter count, context length (`max_position_embeddings`)
2. **HuggingFace README**: Training methodology, base model, license
3. **Official announcement/blog**: Release year, developer, training details
4. **LICENSE file**: Full official license name (e.g., "LFM Open License v1.0", not "lfm1.0")

**Cross-source verification**: When numeric values (e.g., token counts) appear in multiple sources, always cross-check. HuggingFace READMEs may contain approximations or unit errors (e.g., "~1.8B tokens" vs actual "1.8億トークン" = 0.18B). Prefer official blog posts or papers for precise numbers.
