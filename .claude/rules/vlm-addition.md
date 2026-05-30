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
| スクラッチ学習モデル | New VLM assembled from an LLM + vision encoder (+ projector) — i.e., a VLM that did not previously exist. The LLM may be Japanese (e.g., LLM-jp, PLaMo, Sarashina) OR foreign (e.g., Phi-4, Qwen3-1.7B); what matters is that the **VLM itself is new**, not pre-existing. Multi-stage training is typical but not required. |
| 海外モデルに日本語で追加学習 | Fine-tuned from an existing foreign VLM (e.g., Qwen2.5-VL, Qwen3-VL, InternVL). If the base model is already a foreign VLM, it belongs here regardless of training scale. |
| マージモデル | VLMs created by merging techniques |

**Critical Rule:** Always check the base model. If a model is fine-tuned from a foreign VLM (e.g., `Qwen3-VL-8B-Thinking`), it belongs in 「海外モデルに日本語で追加学習」, even if other models from the same developer are in a different section.

**Distinguishing scratch vs. foreign-fine-tuned (common source of confusion):**
- Base is a **foreign LLM** (text-only, e.g., Qwen3-1.7B, Phi-4) + vision encoder newly attached → **スクラッチ学習モデル** (the VLM is new, even if the LLM is foreign). Precedents: NABLA-VL (Phi-4 + SigLIP), Jagle-VL (Qwen3-1.7B + SigLIP2), LLM-jp-4-VL (LLM-jp-4 + SigLIP2).
- Base is a **foreign VLM** (already vision-capable, e.g., Qwen2.5-VL, Qwen3-VL, InternVL2) → **海外モデルに日本語で追加学習**. Precedents: KARAKURI VL 2 (Qwen3-VL-8B), Stockmark-DocReasoner (Qwen2.5-VL-32B).

**How to identify the base model:** Use the HuggingFace **Model tree** (right sidebar) — this is the structured ground truth. Do NOT rely solely on model card prose like "○○および△△をもとに開発" / "based on A and B", which often lists multiple models for acknowledgment even when only one is the technical base. See `model-addition.md` for the full verification checklist.

## VLM Ordering

- Same parameter size ordering as LLMs (descending)
- Model family similarity does NOT override parameter size
