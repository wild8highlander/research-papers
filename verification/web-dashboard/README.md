# 🖥 verification · web-dashboard — the Dashboard Package Manifest

> **Navigation:** [`verification`](../README.md) › **`web-dashboard`**

![Type](https://img.shields.io/badge/Type-Node%20Package-339933?style=flat-square&logo=nodedotjs&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **package manifest of the web dashboard** — the Node/Next.js front-end that visualises verification results. This folder currently carries `package.json` (the dependency and script manifest); the dashboard's visualisation surface is developed in the AB-Cloud snapshot's [`apps/ab-cloud-dashboard`](../../ab-cloud/apps/README.md), which this manifest relates to. Treat this directory as the in-framework hook for dashboard builds; `package.json` pins the tooling so `npm install && npm run build` is reproducible.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`package.json`](package.json) | 456 B | dashboard package manifest — pinned tooling and build scripts |

## 🔗 Cross-References

- [AB-Cloud dashboard app](../../ab-cloud/apps/README.md)
- [Framework root](../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Манифест веб-дашборда (package.json): зафиксированные зависимости и скрипты сборки; визуальная часть развита в ab-cloud/apps/ab-cloud-dashboard.

---

<div align="center">

**[⬆ Back to top](#-verification--web-dashboard--the-dashboard-package-manifest)** · 
**[Repository root](../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>