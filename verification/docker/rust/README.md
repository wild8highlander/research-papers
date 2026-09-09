# 🐳 docker · Rust — Pinned Toolchain Image

> **Navigation:** [`verification`](../../README.md) › [`docker`](../README.md) › **`rust`**

![Type](https://img.shields.io/badge/Type-Dockerfile-2496ED?style=flat-square&logo=docker&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square)

The **Dockerfile pinning the Rust (1.75+) environment** for this framework layer. The image installs the toolchain (cargo build --release as the in-container flow), copies the verification sources, and defaults to running the Rust verification — so `docker run` reproduces exactly what CI runs, byte-for-byte at toolchain level.

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`Dockerfile`](Dockerfile) | 286 B | Rust 1.75+ environment — install + source copy + verification entrypoint |

## ▶️ How to Run

```bash
docker build -t rp-rust verification/docker/rust
docker run --rm rp-rust
```

## 🔗 Cross-References

- [Docker layer](../README.md)
- [Language layer](../../rust/README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Dockerfile со средой Rust 1.75+: установка тулчейна + запуск верификации по умолчанию.

---

<div align="center">

**[⬆ Back to top](#-docker--rust--pinned-toolchain-image)** · 
**[Repository root](../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>