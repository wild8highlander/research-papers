# Coq — Формальная верификация

Формальные доказательства для всех 6 исследовательских разделов.

## Что внутри

- `section1_correction_b/CorrectionB.v` — поправка b, Rodrigues
- `section2_preprint/ProofChain.v` — цепочка PSL(2,7) → α → L_min → b → γ
- `section3_ab_cloud/Hofstadter.v` — гамильтониан Хофштадтера, GUE
- `section4_kdv/KdV.v` — солитон, KdV
- `section5_klein_attractor/Klein.v` — квартика Клейна
- `section6_riemann_zeros/RiemannZeros.v` — нули Римана

## Сборка

```
cd coq
coq_makefile -f _CoqProject -o Makefile
make
```
