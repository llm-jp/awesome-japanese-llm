---
paths:
  - "parts/references_model.md"
  - "parts/references_training.md"
---

# Reference (Paper) Addition Guidelines

Chronological tables of foundational papers/methods. Columns: `モデル・手法名 | 日付 | 会議 | 論文リンク`.

> Trigger: this is usually edited as part of a **model addition** — when a model's base architecture is not yet listed, add the architecture paper in the same change. See `model-addition.md` ("Architecture Reference Paper").

- **Order**: ascending by 日付; insert at the matching position, don't append.
- **日付**: arXiv v1 submission date as `YYYY.MM.DD` (the `[v1]` timestamp, NOT the publication date). For papers without arXiv, use the document's release date.
- **会議**: publication venue as abbreviation + year (`ACL 2021`, `NeurIPS 2022`, `ACM MM 2022` = ACM Multimedia, `EMNLP 2023 (Findings)`); preprint-only → `-`. Confirm from the arXiv "Comments" / "Journal reference" field, not from memory.
- **論文 link**: ACL Anthology URL if available, else arXiv abstract URL; anchor on the paper's full title.
