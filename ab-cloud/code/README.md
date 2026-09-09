# Canonical Julia Suite — `ab_cloud_v19.jl` (37 Tests, Two-Pass Protocol)

This folder holds the **canonical numerical program** of the project: a
single-file, dependency-free Julia suite that produces every number the
monographs quote. Language: Julia ≥ 1.10 (reference runs: Julia 1.12.0);
stdlib only — nothing to `Pkg.add()`.

## Files

| File | Size | What it is |
|---|---|---|
| `ab_cloud_v19.jl` | 16 110 lines | **canonical suite** — 37 tests, two-pass protocol, report engine (md/html/pdf/docx/png/svg/gif), interactive menu, Physics Lab (22 experiments), 3D lab (30 experiments) |
| `julia/` | 5 files, ~122 K lines | historical versions supplied by the author — see `julia/README.md` |

## The 37 tests, grouped

| Group | Tests | Verifies |
|---|---|---|
| Convergence | 1–3 | b(N) = (1/N)Σ|γₖ−γ̃ₖ| — table, monotonicity, rate; b(50000) = 1.2126, empirical law b(N) ≈ 7.0312·N^(−0.1685) (R² = 0.9895) |
| GUE statistics | 4–5, 9–17 | KS/CvM vs the GUE surmise, ⟨r⟩ = 0.5848 ± 0.0260 (GUE 0.5992), Σ²(L), Δ₃(L), K(τ), bootstrap CIs |
| Physics of the cloud | 6–8, 18–22 | Byers–Yang flux defect 3.5·10⁻¹⁵, Connes self-duality zero modes, AIII class, Dirac cone v_F ≈ 0.125 (R² = 0.9997), Berry R₂(0) |
| Spinor / topology | 23–28 | Arf invariant, PSL(2,7) orbit structure, zero-mode counts 2/3/3/3/7 |
| Robustness | 29–37 | chaos/decay rate, half-factorial γ, byte-level robustness, form factor K(τ), residual diagnostics |

(Verdict semantics: PASS / WARN / FAIL against thresholds printed with each
test; the WARN band is calibration, documented in the run reports.)

## Running

```bash
# fast CI check: 16×16 → 32×32, ζ ≤ 5000, both passes, ~3–5 min
julia code/ab_cloud_v19.jl --quick

# the full two-pass 37-test suite (30–60 min, 50 000 zeros, 72×72 → 96×96)
julia code/ab_cloud_v19.jl --test all

# one test only, single pass
julia code/ab_cloud_v19.jl --test 33 --no-two-pass

# interactive menu: 37 tests + Physics Lab (E-experiments) + 3D lab (30 tests)
julia code/ab_cloud_v19.jl
```

Useful flags: `--zeros N` (default 50000), `--source NAME`, `--matrix-size`,
`--quick`, `--test all|N`, `--no-two-pass`, `--lang en|ru`. `make quick-test`,
`make test-all`, `make menu` from the repository root do the same.

## What it writes

A timestamped run folder under `results/` (`run_YYYYMMDD_HHMMSS/`):
per-test subfolders with `report.{md,pdf,docx,html}`, `logs/` (computation
log + captured stdout), `plots/` (600 dpi PNG + SVG + PDF + GIF animations),
plus `FINAL_REPORT/` and an `index.html` cross-linking everything. The
committed example of such a run is `results/run_20260902_134759/` (plots
stripped for size — they regenerate).

## The two-pass protocol

Pass 1 runs every test on a moderate lattice; pass 2 ("HARDCORE") re-runs
the decisive checks at higher resolution (96×96) with the full 50 000-zero
sample. Only a test that passes **both** passes is reported PASS; this is
the anti-overfitting backbone of the monograph claims.

## Кратко (по-русски)

- `code/ab_cloud_v19.jl` — канонический набор: 37 тестов, двухпроходный
  протокол, генератор отчётов (md/html/pdf/docx/графика), интерактивное меню,
  Physics Lab и 3D-лаборатория; 16 тыс. строк, без внешних пакетов Julia.
- Запуск: `--quick` (быстрый CI), `--test all` (полный прогон 30–60 мин),
  `--test N`, меню без аргументов.
- Результаты пишутся в `results/run_<метка>/` с отчётами, логами и
  графиками; образец — `results/run_20260902_134759/`.
- `julia/` — авторские исторические версии (v19_v1, v20, v21) для прослеживания.

---
---

## 💾 The Code Layer in Depth

### Canonical vs Historical

The folder holds **both** the current suite entry points and the historical Julia versions:

- historical (provenance): `julia/ab_cloud_v19_v1.jl`, `ab_cloud_v20.jl`, `ab_cloud_v21.jl`, `ab_cloud_v21_v1.jl` — exactly as supplied, never edited;
- current: the consolidated suite lives one level down in `verification/` (10 languages); the Julia folder's README documents the runners and the v19_v1 zero-table extraction history.

Why keep both? Because every number in every monograph traces to a code state. The historical files are the executable provenance of the published results; deleting them would break the traceability chain the snapshot exists to provide.

### The 50 000-Zero Extraction Story

The frozen dataset `verification/data/zeta_zeros_50000_embedded.txt` was extracted **verbatim from the embedded array** of the historical `ab_cloud_v19_v1.jl` source — the story (why the array was embedded, how the extraction was verified) is told in [`julia/README.md`](julia/README.md). This is why the dataset is byte-frozen: it *is* the source's array, relocated, not a re-download or a regeneration.

## 🇷🇺 Краткое резюме (Russian Summary)

**ab-cloud/code/** — канонический и исторический код: архив Julia-версий (v19_v1, v20, v21, v21_v1) «как есть» для происхождения результатов и текущий набор в `verification/`. Датасет 50 000 нулей извлечён дословно из встроенного массива v19_v1 — история в `julia/README.md`.

---
## 🏛 The Version Lineage, Precisely

| Version | Role in the lineage |
|---|---|
| v19_v1 | the source whose embedded array yielded the 50 000-zero table; the two-pass discipline's origin |
| v20 | intermediate evolution of the suite (registry growth) |
| v21 | the spinor-programme era; source state of the v21 monographs' numbers |
| v21_v1 | the corrected/revised v21 state; pairs with the original-v21 monograph tree |

Rule of use: read the historical sources to *understand where a number came from*; run the current suite to *reproduce the numbers today*. The two activities meet in the archive — historical runs and fresh runs diff test-by-test.

---
## 🚫 The Editing Rule

The historical sources (`v19_v1`, `v20`, `v21`, `v21_v1`) are **read-only by convention**: no formatting passes, no language-version modernisation, no "small fixes". Their value is being exactly what produced the published numbers; any edit destroys that. Fixes belong in the current suite; the diff between "what was" and "what is" is the changelog's job, not a rewrite of the archive.

<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../README.md)
- 📖 [Как верифицируются утверждения](../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../papers/README.md) · 📚 [Монографии](../../../docs/README.md) · 🧾 [LaTeX](../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

