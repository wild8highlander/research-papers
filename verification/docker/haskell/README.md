# 🐳 docker · Haskell — Pinned Toolchain Image

> **Navigation:** [`verification`](../../README.md) › [`docker`](../README.md) › **`haskell`**

![Type](https://img.shields.io/badge/Type-Dockerfile-2496ED?style=flat-square&logo=docker&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **Dockerfile pinning the Haskell (9.4) environment** for this framework layer. The image installs the toolchain (cabal build as the in-container flow), copies the verification sources, and defaults to running the Haskell verification — so `docker run` reproduces exactly what CI runs, byte-for-byte at toolchain level.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`Dockerfile`](Dockerfile) | 304 B | Haskell 9.4 environment — install + source copy + verification entrypoint |

## ▶️ How to Run

```bash
docker build -t rp-haskell verification/docker/haskell
docker run --rm rp-haskell
```

## 🔗 Cross-References

- [Docker layer](../README.md)
- [Language layer](../../haskell/README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Dockerfile со средой Haskell 9.4: установка тулчейна + запуск верификации по умолчанию.

---

<div align="center">

**[⬆ Back to top](#-docker--haskell--pinned-toolchain-image)** · 
**[Repository root](../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>