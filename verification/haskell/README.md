# Haskell — Численная верификация

Численная и символьная верификация для всех 6 исследовательских разделов.

## Что внутри

- `Section1_CorrectionB/` — поправка b
- `Section2_PreprintNSE/` — цепочка NSE
- `Section3_ABCloud/` — AB-Cloud
- `Section4_KdV/` — KdV
- `Section5_KleinAttractor/` — Клейн
- `Section6_RiemannZeros/` — нули Римана

## Сборка

```
cd haskell
cabal build all
```

## Запуск

```
cabal run verify_section1_correctionb
```
