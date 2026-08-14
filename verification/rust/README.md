# Rust — Численная верификация

Численная верификация для всех 6 исследовательских разделов.

## Что внутри

- `section1_correction_b/` — поправка b
- `section2_preprint/` — цепочка доказательства NSE
- `section3_ab_cloud/` — AB-Cloud
- `section4_kdv/` — KdV
- `section5_klein_attractor/` — Клейн
- `section6_riemann_zeros/` — нули Римана

## Сборка

```
cd rust
cargo build --release
```

## Запуск

```
cargo run --release -p section1_correction_b
```
