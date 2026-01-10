# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation project that maintains a comprehensive list of Japanese Large Language Models (LLMs) and their evaluation benchmarks. The project uses VitePress for documentation site generation.

## Common Commands

```bash
yarn docs:dev      # Start development server
yarn docs:build    # Build documentation site
yarn docs:preview  # Preview built documentation
```

## Project Structure

- **README.md** - Main Japanese documentation (primary content)
- **en/README.md** - English translation
- **fr/README.md** - French translation
- **parts/references_model.md** - Model reference chronology
- **parts/references_training.md** - Training method references

## Model Addition Guidelines

### Section Selection (Most Important)

Models are classified into sections based on training approach. **Evidence is required for classification.**

| Section | Criteria |
|---------|----------|
| フルスクラッチ学習モデル | Models pre-trained from scratch on Japanese data |
| 海外モデルに日本語で継続事前学習を行ったモデル | **Clear evidence** of continual pre-training on Japanese data (e.g., "Pre-training", "Continual pre-training", "Additional pre-training" in documentation) |
| 海外モデルに日本語で追加学習を行ったモデル（事後学習のみ、または詳細不明） | Post-training only (SFT/DPO/RL), OR **training details unknown** |

**Critical Rules:**
- **When in doubt, use "事後学習のみ、または詳細不明"** - Do NOT assume continual pre-training without evidence
- Check HuggingFace README for explicit statements about training methodology
- "Optimized for Japanese" or "Japanese chat model" alone is NOT evidence of continual pre-training
- Models derived from Japanese continual pre-training models (e.g., Swallow, ELYZA) belong in 継続事前学習 section

### Training Data Column

| Situation | What to write |
|-----------|---------------|
| Training data/method is documented | Specific datasets, methods (e.g., "SFT: dataset-name", "事前学習: corpus-name") |
| Training data/method is unknown | 「不明」(JA) / "Undisclosed" (EN) / "Non divulgué" (FR) |
| **Do NOT write** | Descriptive phrases like "日本語に最適化されたモデル" - this is not training data |

### Information Verification Checklist

1. **HuggingFace config.json**: Parameter count, context length (`max_position_embeddings`)
2. **HuggingFace README**: Training methodology, base model, license
3. **Official announcement/blog**: Release year, developer, training details
4. **LICENSE file**: Full official license name (e.g., "LFM Open License v1.0", not "lfm1.0")

### Table Formatting

- **Parameter size ordering**: Descending order within each section (largest first)
- **Architecture column**: Base architecture name (e.g., "Llama 3.1", "Qwen2.5"), NOT attention mechanisms
- **Multiple sizes**: Combine into single row: `([**7b**](url1), [**13b**](url2))`
- **License format**: Use official names with consistent capitalization

### Multilingual Consistency

- Update all three files (README.md, en/README.md, fr/README.md) simultaneously
- Same position/order across all versions
- Translations: 不明 → Undisclosed → Non divulgué

## VLM Addition Guidelines

### VLM Sections

1. **スクラッチ学習モデル**: New VLM combining Japanese LLM + vision encoder
2. **海外モデルに日本語で追加学習**: Existing foreign VLM with Japanese training added
3. **マージモデル**: VLMs created by merging techniques

### VLM Ordering

- Same parameter size ordering as LLMs (descending)
- Model family similarity does NOT override parameter size

## Contributing Notes

See CONTRIBUTING.md for:
- Minimum parameter threshold (≥110M)
- Exclusion of task-specific fine-tuned models
- Dataset/benchmark inclusion criteria
