# 🐳 docker · Agda — Pinned Toolchain Image

> **Navigation:** [`verification`](../../README.md) › [`docker`](../README.md) › **`agda`**

![Type](https://img.shields.io/badge/Type-Dockerfile-2496ED?style=flat-square&logo=docker&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **Dockerfile pinning the Agda (2.6) environment** for this framework layer. The image installs the toolchain (agda --safe <Module>.agda as the in-container flow), copies the verification sources, and defaults to running the Agda verification — so `docker run` reproduces exactly what CI runs, byte-for-byte at toolchain level.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`Dockerfile`](Dockerfile) | 135 B | Agda 2.6 environment — install + source copy + verification entrypoint |

## ▶️ How to Run

```bash
docker build -t rp-agda verification/docker/agda
docker run --rm rp-agda
```

## 🔗 Cross-References

- [Docker layer](../README.md)
- [Language layer](../../agda/README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Dockerfile со средой Agda 2.6: установка тулчейна + запуск верификации по умолчанию.

---

<div align="center">

**[⬆ Back to top](#-docker--agda--pinned-toolchain-image)** · 
**[Repository root](../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>