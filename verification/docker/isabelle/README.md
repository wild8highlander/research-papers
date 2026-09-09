# 🐳 docker · Isabelle-HOL — Pinned Toolchain Image

> **Navigation:** [`verification`](../../README.md) › [`docker`](../README.md) › **`isabelle`**

![Type](https://img.shields.io/badge/Type-Dockerfile-2496ED?style=flat-square&logo=docker&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **Dockerfile pinning the Isabelle-HOL (2024) environment** for this framework layer. The image installs the toolchain (isabelle build -D . as the in-container flow), copies the verification sources, and defaults to running the Isabelle-HOL verification — so `docker run` reproduces exactly what CI runs, byte-for-byte at toolchain level.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`Dockerfile`](Dockerfile) | 169 B | Isabelle-HOL 2024 environment — install + source copy + verification entrypoint |

## ▶️ How to Run

```bash
docker build -t rp-isabelle verification/docker/isabelle
docker run --rm rp-isabelle
```

## 🔗 Cross-References

- [Docker layer](../README.md)
- [Language layer](../../isabelle/README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Dockerfile со средой Isabelle-HOL 2024: установка тулчейна + запуск верификации по умолчанию.

---

<div align="center">

**[⬆ Back to top](#-docker--isabelle-hol--pinned-toolchain-image)** · 
**[Repository root](../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>