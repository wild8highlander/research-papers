# results — Run Artifacts and Reference Logs (455 files)

Everything the Julia suite produced on paper-worthy runs, committed so the
numbers in the monographs are checkable without running anything. Two kinds
of content live here:

1. **`run_20260902_134759/`** — the complete two-pass v19 run of 2026-09-02
   (37 tests, Julia 1.12.0, 50 000 Odlyzko zeros, pass 2 "HARDCORE" at
   96×96): per-test reports, logs, final report, cross-linking index.
   Committed without the run's PNG plots (453 files) — they regenerate
   deterministically from the suite.
2. **Two flat reference logs** — the 2026-08-28 37-test run (v18) and the
   v19 verification-report header/config dump from 2026-09-02.

## `run_20260902_134759/` — layout

```
run_20260902_134759/
├── index.html                  # browser index cross-linking all 37 tests + final report
├── FINAL_REPORT/               # aggregated two-pass verdict
│   ├── final_report.md / .pdf / .docx / .html
│   ├── logs/                   # run-level logs
│   └── reports/                # aggregated per-test blocks
├── test_01_bN_convergence/     # one folder per test (37 total)
│   ├── report.md / .pdf / .docx / .html
│   └── logs/
│       ├── computation_log.txt # the actual numbers: fits, statistics, thresholds
│       └── stdout_capture.txt  # raw console output of the test
├── test_02_bN_monotonicity/
│   …
└── test_37_half_factorial_gamma/
```

Every `report.md` opens with the verdict line
(`Verdict: PASS | Generated: … | Suite: AB-Cloud v19 (Julia 1.12.0)`),
explains what the test verifies, states the raw result (e.g.
`8 sub-checks, 0 failed, b(50000)=1.2126 → PASS`) and lists the plots that
the suite regenerates.

## The 37 tests (folder names are self-describing)

| # | Test | # | Test |
|---|---|---|---|
| 01 | bN_convergence | 20 | … |
| 02 | bN_monotonicity | … | full list: `ls results/run_20260902_134759/` |
| 03 | bN_rate | … | the suite's own docs: `code/ab_cloud_v19.jl` header |
| 04 | gue_ks_full | … | |
| … | | 36 | byte_robust |
| … | | 37 | half_factorial_gamma |

Highlights: GUE statistics of the 50 000-zero sample (⟨r⟩, KS, Σ², Δ₃),
Byers–Yang flux defect 3.5·10⁻¹⁵, Connes self-duality, Dirac cone
v_F ≈ 0.125 (R² = 0.9997), Berry R₂(0), Arf/orbit checks, robustness battery.

## Regenerating the plots

The plots were stripped from the committed run to keep the repository light
(the run writes ~600 dpi PNG + SVG + PDF + GIF per figure). Reproduce the
whole run including plots:

```bash
julia code/ab_cloud_v19.jl --test all      # 30–60 min; writes a NEW timestamped run folder
```

The committed `run_20260902_134759` numbers are reproducible because the
suite is seeded and reads the frozen data in `verification/data/`.

## Flat reference logs

| File | What it is |
|---|---|
| `verification_run_v18_37tests_2026-08-28.txt` | full console log of the 2026-08-28 v18 37-test run — the historical basis of monograph v22; includes the b(N) fit (b(N) ≈ 7.0312·N^(−0.1685), R² = 0.9895; alternative 1/log N fit R² = 0.9994) and the v23-notation caveat that α = 1/2 refers to the AB-phase, not the convergence rate |
| `ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt` | header/config dump of the v19 verification report: zeros = 50000, n_bootstrap = 1000, chi2_bins = 300, gue_matrix_size = 12000 (seed 112), rmt CDF table 32 768-pt (max|ΔF| = 4.9e-9), embedded-dataset note |

## How to read a run folder

1. Open `index.html` in a browser — it links every test and the final report.
2. For a single test, read `test_XX_*/logs/computation_log.txt` first (raw
   numbers), then `report.md` (verdict + interpretation).
3. `FINAL_REPORT/final_report.md` aggregates all 37 verdicts of both passes.

## Кратко (по-русски)

- Артефакты прогона v19 от 2026-09-02: 37 тестов, два прохода (второй —
  HARDCORE 96×96), Julia 1.12.0, 50 000 нулей Одлыжко.
- Структура: по папке на тест (report md/pdf/docx/html + computation_log +
  stdout), FINAL_REPORT, index.html; графики из прогона исключены и
  воспроизводятся набором `julia code/ab_cloud_v19.jl --test all`.
- Плюс два плоских журнала: прогон v18 от 2026-08-28 (основа монографии
  v22) и конфиг-дамп верификационного отчёта v19.
- Читать так: index.html → computation_log.txt теста → report.md →
  FINAL_REPORT.

---
---

## 🗄 The Archive in Depth

### What the Two Archived Runs Are

**v18, 37 tests, 2026-08-28** (`verification_run_v18_37tests_2026-08-28.txt`) — the complete console output of the 37-test registry: the three objections' tests, the extended RMT diagnostics (Anderson–Darling, two-sample KS, Σ²(L), Δ₃(L)), the Hamiltonian structural tests (Dirac string, Byers–Yang, Chern number, chiral symmetries), and the closing robustness checks. Its WARN lines are self-explaining — e.g. the full-range KS rejection is printed *with* the remedy (high-T subrange, convergence-watch) — which makes the file readable as an audit narrative.

**v19, 2026-09-02** (`ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt`) — the full two-pass run (72×72 → 96×96 with the HARDCORE audit, Julia 1.12.0): 32 PASS / 5 WARN, with per-test reports in the linked run directory.

### How to Use the Archive

1. **As reference values.** Run the suite fresh, diff test-by-test against the archive; any drift is a finding, not a nuisance.
2. **As methodology documentation.** The console output shows the tests' *logic* (why each control exists), which the raw test code alone does not convey as directly.
3. **As citation anchors.** Cite a result as "v19 run of 2026-09-02, test N" — the archive pins it to a date, a code state and a machine-readable summary.

### Append-Only Discipline

The archive grows by append: new runs arrive as new files (or new run directories), and nothing already archived is ever rewritten. This is what makes "diff against historical behaviour" possible years later — the history has no rewrite holes.

## 🇷🇺 Краткое резюме (Russian Summary)

**ab-cloud/results/** — архив эталонных прогонов: консольный вывод v18 (37 тестов, 2026-08-28) и полный двухпроходный отчёт v19 (72×72 → 96×96, HARDCORE-аудит, Julia 1.12.0, 32 PASS / 5 WARN, 2026-09-02). Архив пополняется только добавлением файлов; сверьте свежий прогон с архивом тест-в-тест — любое расхождение является находкой.

---
## 🔍 Navigating the v18 Archive

The v18 file is long (37 tests with plots and tables in console form). Its map:

- **Tests 1–2** — baseline and environment self-checks (banners, config echo);
- **Tests 3–9** — the objections' first battery: convergence rate, KS (full/high-T), χ², decay slope/residuals/bootstrap;
- **Test 10** — the cross-validation stability check;
- **Tests 11–14** — the advanced RMT battery (AD, 2-sample KS, Σ²(L), Δ₃(L));
- **Tests 15–26** — the Hamiltonian structural block (DIRAC-STRING fix, spacing → GUE, Connes self-duality, chiral symmetries, Dirac cone, Chern number, spinorial phase, AB phase, fractal factor, Dirac string flux, Byers–Yang, PBC torus);
- **Tests 27–32** — the second structural block (binary chiral symmetry, Berry correction, f_GUE, Dirac dip, v_F, Hatano–Nelson skin);
- **Tests 33–37** — the closing battery (⟨r⟩ bootstrap, L-scaling, direct AB-vs-ζ-5000, form factor K(t), byte-level robustness).

Every WARN in the file carries its explanation inline — the archive is written to be read.

---
## 📎 Citing a Run

Cite a result as: *archive file, test number, repository commit (or Zenodo version DOI)*. Example form: "v18 run of 2026-08-28 (`verification_run_v18_37tests_2026-08-28.txt`), Test 5, repo @ `<commit>`". The test numbering is stable across languages and time, so the triple (file, test, commit) pins the claim completely.

<!-- doc-enhancer:block v1 (автоматический блок; файлы лицензии не затрагиваются) -->

---

## 🧭 Навигация и быстрые ссылки (auto)

- 🏠 [Корень репозитория](../../../README.md)
- 📖 [Как верифицируются утверждения](../../../verification/README.md)
- ☁️ [Комплекс AB-Cloud](../../../ab-cloud/README.md)
- 📄 [Статьи (PDF)](../../../papers/README.md) · 📚 [Монографии](../../../docs/README.md) · 🧾 [LaTeX](../../../src/README.md)
- ⚖️ [Лицензия IPL-RP-1.0](../../../LICENSE.md) — просмотр, одна резервная копия и цитирование с атрибуцией разрешены; остальное — только с письменного согласия автора.

*Блок добавлен автоматически (`doc-enhancer v1`); к лицензии отношения не имеет и её не изменяет. Повторный запуск скрипта блок не дублирует.*

