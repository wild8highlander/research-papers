# C++ — Численная верификация

Численная верификация для всех 6 исследовательских разделов.

## Что внутри

- `section1_correction_b/main.cpp` — поправка b
- `section2_preprint/main.cpp` — цепочка NSE
- `section3_ab_cloud/main.cpp` — AB-Cloud
- `section4_kdv/main.cpp` — KdV
- `section5_klein_attractor/main.cpp` — Клейн
- `section6_riemann_zeros/main.cpp` — нули Римана

## Сборка

```
cd cpp
mkdir build && cd build
cmake ..
make -j$(nproc)
```

## Запуск

```
./verify_section1_correction_b
```
