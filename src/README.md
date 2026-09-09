# 🧾 src — LaTeX Sources of the Papers

> **Navigation:** **`src`**

![Format](https://img.shields.io/badge/Format-LaTeX-008080?style=flat-square&logo=latex) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Repo](https://img.shields.io/badge/Repo-wild8highlander%2Fresearch--papers-181717?style=flat-square&logo=github&logoColor=white)

This directory holds the **compilable LaTeX sources** behind the PDFs published in [`papers/`](../papers/README.md). Two groups live here:

- **[`main/`](main/README.md)** — the source of the full correction-b paper: `main.tex` (~55 KB, the primary document) and `main_v2.tex` (the revision-stamped copy), complete with a custom accent-coloured sectioning setup (`	itleformat` with the `accent` colour) and running headers;
- **[`preprint/`](preprint/README.md)** — `preprint.tex`, the source of the compact NSE regularity preprint whose title page reads *"Correction b as Polarization Twisting: Analytical Proof of 3D Navier–Stokes Regularity without Dissipation"*.

The sources are the authoritative textual record: any wording in the PDFs can be traced, diffed and quoted against them. They are intentionally plain LaTeX — no exotic packages beyond standard formatting needs — so the documents compile in any modern TeX distribution. The monograph figures referenced by the manuscripts are preserved with the Word editions in [`docs/`](../docs/README.md), and the AB-Cloud monograph sources (md/tex for all three languages) are in [`ab-cloud/monographs/`](../ab-cloud/monographs/README.md).

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`main/`](main/) | — | source of the full correction-b paper (main.tex + main_v2.tex) |
| [`preprint/`](preprint/) | — | source of the NSE preprint |

## 🗂 Directory Layout

```
src/
├── main/   # 3 files
│   ├── main.tex
│   ├── main_v2.tex
│   └── README.md  (this file)
├── preprint/   # 2 files
│   ├── preprint.tex
│   └── README.md  (this file)
└── README.md  (this file)
```

## 🇷🇺 Краткое резюме (Russian Summary)

**src/** — компилируемые LaTeX-исходники статей: `main/` — полная статья о поправке b (main.tex ~55 КБ + main_v2.tex) и `preprint/` — препринт о регулярности NSE (preprint.tex). Позволяют проследить и процитировать любую формулировку из PDF.

---

<div align="center">

**[⬆ Back to top](#-src--latex-sources-of-the-papers)** · 
**[Repository root](README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>