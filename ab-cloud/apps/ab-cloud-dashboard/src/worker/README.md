# ⚙️ dashboard · src · worker — the Statistics Web Worker

> **Navigation:** [`ab-cloud`](../../../../README.md) › [`apps`](../../../README.md) › [`ab-cloud-dashboard`](../../README.md) › [`src`](../README.md) › **`worker`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **Web Worker** of the dashboard: `stats.worker.js` receives the raw numeric arrays (spectra, spacings, zero tables) and computes the statistics — histograms, mean gap ratios, KS values — off the main thread, posting results back as messages. This keeps the UI responsive while large datasets (thousands of zeros) are processed in the browser.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`stats.worker.js`](stats.worker.js) | 8.0 KB | Web Worker — histogram/⟨r⟩/KS computations off-thread (≈8 KB) |

## 🔗 Cross-References

- [src tree](../README.md)
- [Dashboard root](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Web Worker дашборда: считает гистограммы, ⟨r⟩ и KS вне главного потока, чтобы UI не подвисал на больших массивах нулей.

---

<div align="center">

**[⬆ Back to top](#-dashboard--src--worker--the-statistics-web-worker)** · 
**[Repository root](../../../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>