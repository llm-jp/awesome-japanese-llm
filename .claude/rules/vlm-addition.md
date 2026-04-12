---
paths:
  - "README.md"
  - "en/README.md"
  - "fr/README.md"
---

# VLM Addition Guidelines

## VLM Section Classification

Classify each model independently based on its own training approach. Do NOT assume section placement based on other models from the same developer.

| Section | Criteria |
|---------|----------|
| スクラッチ学習モデル | New VLM built from scratch, typically combining a Japanese LLM + vision encoder with substantial multi-stage training |
| 海外モデルに日本語で追加学習 | Fine-tuned from an existing foreign VLM (e.g., Qwen-VL, InternVL). If the base model is a foreign VLM, it belongs here regardless of training scale |
| マージモデル | VLMs created by merging techniques |

**Critical Rule:** Always check the base model. If a model is fine-tuned from a foreign VLM (e.g., `Qwen3-VL-8B-Thinking`), it belongs in 「海外モデルに日本語で追加学習」, even if other models from the same developer are in a different section.

## VLM Ordering

- Same parameter size ordering as LLMs (descending)
- Model family similarity does NOT override parameter size
