# 🖥 dashboard · src — React Source of the AB-Cloud Dashboard

> **Navigation:** [`ab-cloud`](../../../README.md) › [`apps`](../../README.md) › [`ab-cloud-dashboard`](../README.md) › **`src`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Type](https://img.shields.io/badge/Type-React%20%2B%20Vite-61DAFB?style=flat-square&logo=react&logoColor=black)

The **React source tree of the AB-Cloud dashboard** — the web front-end that renders verification reports, the spinor-64 classification and the ζ-zero statistics in a browser. The app is built with Vite (`../` holds the manifest and the committed production bundle in `dist/`, ready for GitHub Pages). The architecture is deliberately small: one `App.jsx` shell, three page components, a shared UI kit, one stylesheet, and a Web Worker that keeps heavy statistics off the main thread.

Pages: **RunReport** (renders an archived verification run — the same report format `ab-cloud/results/` archives), **Spinor64** (the 64-structure PSL(2,7) classification viewer), **ZerosStats** (spacing histograms, ⟨r⟩ statistics and KS comparisons over the embedded ζ-zero datasets). The statistics themselves are computed in `worker/stats.worker.js` so scrolling stays smooth while the Web Worker crunches the arrays.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`App.jsx`](App.jsx) | 1.7 KB | app shell — routing between the three pages, global state |
| [`components/`](components/) | — | shared UI kit (ui.jsx) |
| [`main.jsx`](main.jsx) | 188 B | React entry point (mounts App) |
| [`pages/`](pages/) | — | the three pages — RunReport, Spinor64, ZerosStats |
| [`styles.css`](styles.css) | 2.4 KB | global stylesheet |
| [`worker/`](worker/) | — | Web Worker for off-thread statistics |

## 🗂 Directory Layout

```
src/
├── components/   # 2 files
│   ├── README.md  (this file)
│   └── ui.jsx
├── pages/   # 4 files
│   ├── README.md  (this file)
│   ├── RunReport.jsx
│   ├── Spinor64.jsx
│   └── ZerosStats.jsx
├── worker/   # 2 files
│   ├── README.md  (this file)
│   └── stats.worker.js
├── App.jsx
├── main.jsx
├── README.md  (this file)
└── styles.css
```

## 🔗 Cross-References

- [Dashboard root (build & bundle)](../README.md)
- [Apps layer](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

React-исходники дашборда AB-Cloud (Vite): оболочка App.jsx, страницы RunReport / Spinor64 / ZerosStats, UI-кит и Web Worker для статистики вне главного потока. Прод-сборка уже в ../dist/.

---

<div align="center">

**[⬆ Back to top](#-dashboard--src--react-source-of-the-ab-cloud-dashboard)** · 
**[Repository root](../../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>