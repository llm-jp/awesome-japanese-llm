---
paths:
  - "parts/references_model.md"
  - "parts/references_training.md"
---

# Reference (Paper) Addition Guidelines

These files are chronological tables of foundational papers/methods. Columns:
`モデル・手法名 | 日付 | 会議 | 論文リンク`.

> Note: the main trigger for editing this file is a **model addition** — when you add a model whose base architecture is not yet listed here, add the architecture paper as part of that same change. See `model-addition.md` ("Architecture Reference Paper"). This file only covers *how* to format the row.

## Ordering (Most Important)

- Rows are sorted in **ascending chronological order by the 日付 column**. Insert a new row at the position matching its date — do NOT append to the end.
- The 日付 is the **arXiv v1 submission date**, formatted `YYYY.MM.DD`. It is NOT the publication/conference date. Check the arXiv abstract page's `[v1]` timestamp (e.g., "Tue, 29 Dec 2020" → `2020.12.29`).
- For papers without arXiv (e.g., OpenAI tech reports), use the public release date of the document.

## 会議 (Venue) column

- Write the **publication venue**, not arXiv. Use the conference abbreviation + year:
  - Examples: `ACL 2021`, `EMNLP 2020`, `NAACL 2022`, `NeurIPS 2022`, `ICLR 2023`, `ICML 2023`, `ICCV 2023`, `CVPR 2024`, `ACM MM 2022` (= ACM Multimedia), `KDD 2020`.
  - Findings tracks: `EMNLP 2023 (Findings)`. Workshops: `<Workshop> at <Conf> YYYY`.
- If the paper is a preprint only (no venue), use `-`.

## 論文 (Paper) link

- Prefer the **ACL Anthology** URL when the paper is in it; otherwise use the **arXiv abstract** URL (`https://arxiv.org/abs/XXXX.XXXXX`).
- Link the paper's full title as the anchor text.

## Verification

- Confirm both the v1 date and the venue from the arXiv abstract page (the "Comments" / "Journal reference" field often names the venue). Do not infer the venue from memory.
