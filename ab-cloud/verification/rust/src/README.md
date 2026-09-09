# 🦀 verification · rust · src — the Suite's Rust Sources

> **Navigation:** [`ab-cloud`](../../../README.md) › [`verification`](../../README.md) › [`rust`](../README.md) › **`src`**

![Snapshot](https://img.shields.io/badge/AB--Cloud-snapshot%20v1.2.0-blue?style=flat-square&logo=dicebear&logoColor=white) ![License](https://img.shields.io/badge/License-IPL--RP--1.0-red?style=flat-square) ![Lang](https://img.shields.io/badge/Language-Rust-CE422B?style=flat-square&logo=rust&logoColor=white)

The **Rust sources of the AB-Cloud verification suite**: `main.rs` (suite entry), `verify_en.rs` (the English-language verification program) and `verify_ru.rs` (the Russian-language twin — the suite is bilingual by design). Together they implement the three-objection checks in memory-safe Rust with std-only numerics; the crate manifest lives in the parent folder and the frozen datasets in [`data/`](../README.md).

## 📂 Contents — What Lives Here

| File | Size | Description |
|---|---|---|
| [`main.rs`](main.rs) | 17.0 KB | suite entry point (Rust) |
| [`verify_en.rs`](verify_en.rs) | 7.5 KB | verification program — English output |
| [`verify_ru.rs`](verify_ru.rs) | 9.0 KB | verification program — Russian output |

## 🔗 Cross-References

- [Rust layer README](../README.md)
- [Suite root](../../README.md)

## 🇷🇺 Краткое резюме (Russian Summary)

Исходники Rust-верификации ab-cloud: main.rs + двуязычные verify_en.rs / verify_ru.rs; манифест крейта — в родительской папке.

---

<div align="center">

**[⬆ Back to top](#-verification--rust--src--the-suites-rust-sources)** · 
**[Repository root](../../../README.md)**

*Part of [wild8highlander/research-papers](https://github.com/wild8highlander/research-papers) · Licensed under [IPL-RP-1.0](https://github.com/wild8highlander/research-papers/blob/main/LICENSE.md) — All Rights Reserved*

</div>