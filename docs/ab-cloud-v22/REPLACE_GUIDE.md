# REPLACE GUIDE — замена AB-cloud раздела в репозитории `wild8highlander/research-papers`

Пошаговая инструкция: что удалить, что добавить, что поправить в корневом README.
Все пути ниже — от корня репозитория.

---

## Шаг 1. Удалить старые AB-cloud документы (docx и pdf)

```bash
# монографии (docx) — docs/ab-cloud
git rm docs/ab-cloud/en/AB_Cloud_Monograph.docx
git rm docs/ab-cloud/en/AB_Cloud_Monograph_v1.docx
git rm docs/ab-cloud/en/AB_Cloud_Monograph_v23.docx
git rm docs/ab-cloud/ru/AB_Cloud_Monograph.docx
git rm docs/ab-cloud/ru/AB_Cloud_Monograph_v1.docx
git rm docs/ab-cloud/ru/AB_Cloud_Monograph_v23.docx

# результаты верификации (docx)
git rm ab-cloud-verification/AB_Cloud_Verification_Results.docx
git rm ab-cloud-verification/AB_Cloud_Verification_Results_RU.docx

# статьи-пдф — papers/ab-cloud и препринты riemann-zeros
git rm papers/ab-cloud/AB_Cloud_Monograph_EN.pdf
git rm papers/ab-cloud/AB_Cloud_Monograph_v23_EN.pdf
git rm papers/ab-cloud/AB_Cloud_Monograph_v23_RU.pdf
git rm papers/riemann-zeros/AB_Cloud_Preprint_v1.pdf
git rm papers/riemann-zeros/AB_Cloud_Preprint_v2.pdf

# старые 2D-фигуры препринтов (заменяются новым набором)
git rm papers/riemann-zeros/figures/01_P_s_zeta.png
git rm papers/riemann-zeros/figures/03_sigma2_L.png
git rm papers/riemann-zeros/figures/05_fss_ab_cloud.png
```

Смешанные монографии (`papers/monographs/Monograph_full_*.pdf`, `docs/choptuik-riemann/…`,
`docs/kdv/…`) **не удаляются**: в них AB-cloud — только глава. В них нужно обновить
заголовок главы и ссылку (см. Шаг 4) либо оставить указание «AB-cloud chapter superseded
by v22, see docs/ab-cloud-v22».

## Шаг 2. Добавить новый пакет

```bash
mkdir -p docs/ab-cloud-v22 code results
# тексты и графики трёх языков
cp -r <путь-к-пакету>/monographs/ru  docs/ab-cloud-v22/ru
cp -r <путь-к-пакету>/monographs/en  docs/ab-cloud-v22/en
cp -r <путь-к-пакету>/monographs/zh  docs/ab-cloud-v22/zh
# исправленный код и эталонный прогон
cp <путь-к-пакету>/code/ab_cloud_v19.jl code/
cp <путь-к-пакету>/results/verification_run_v18_37tests_2026-08-28.txt results/
git add docs/ab-cloud-v22 code/ab_cloud_v19.jl results/
```

Рекомендация: чтобы репозиторий не разрастался, слайд-исходники
(`docs/ab-cloud-v22/<lang>/text/presentation_html/`) можно не коммитить —
достаточно самих `.pptx`.

## Шаг 3. Обновить ab-cloud-verification/README.md

Заменить в нём ссылку на результаты:

```markdown
Latest verified run: results/verification_run_v18_37tests_2026-08-28.txt
Monograph (RU/EN/ZH, docx+pdf+html+pptx+tex): docs/ab-cloud-v22/
Suite: julia code/ab_cloud_v19.jl --test all   (two-pass, v19 report engine fixed)
Quick check: julia code/ab_cloud_v19.jl --quick (16×16→32×32, ζ≤5000, both passes)
```

## Шаг 4. Готовый фрагмент для корневого README.md

Замените содержимое секции `### AB-Cloud & Riemann Zeros` на:

**RU:**

```markdown
### AB-облако и нули Римана (v22, трёхъязычная монография)

**AB-облако** — гамильтониан Хофштадтера с топологическими вихрями (фазами
Ааронова–Бома). Полная 37-тестовая верификация (v19):

- ⟨r⟩ = 0.5848 ± 0.0260 против GUE 0.5992 (отклонение −2.4%); сходимость по L:
  0.548 → 0.595 при L: 10 → 50;
- топология с машинной точностью: потоки 10⁻¹⁴, Байерс–Янг 3.5·10⁻¹⁵,
  самодуальность Конна (4 нулевые моды), C₁ = 2;
- корреляционная дыра Монтгомери воспроизведена: R₂ облака ближе к GUE, чем к
  Пуассону (d_GUE = 0.140 < d_Pois = 0.227); конечновыборочные поправки Берри
  количественно объясняют отклонения на достижимых высотах;
- дираковская динамика: E_min ∝ 1/L (R² = 0.9997), провал DOS 20×, скин-эффект.

Документы: [RU](docs/ab-cloud-v22/ru/text) · [EN](docs/ab-cloud-v22/en/text) ·
[ZH](docs/ab-cloud-v22/zh/text) — docx + pdf + интерактивный html + презентация
pptx + LaTeX-препринт (tex/pdf); 19 графиков 600 dpi на язык
([RU figures](docs/ab-cloud-v22/ru/figures) · [EN](docs/ab-cloud-v22/en/figures) ·
[ZH](docs/ab-cloud-v22/zh/figures)). Код: [ab_cloud_v19.jl](code/ab_cloud_v19.jl),
эталонный прогон: [37-тестовый лог](results/verification_run_v18_37tests_2026-08-28.txt).
```

**EN / ZH:** аналогичные блоки лежат в пакете — `docs/ab-cloud-v22/en/text/README_fragment_EN.md`
и `docs/ab-cloud-v22/zh/text/README_fragment_ZH.md` (см. Шаг 6).

## Шаг 5. Технические правки

1. `mkdocs.yml` — если раздел `docs/ab-cloud` упомянут в навигации, заменить путь
   на `docs/ab-cloud-v22`.
2. `.github/workflows/link-checker.yml` — прогонится автоматически; битых ссылок на
   удалённые файлы в README не останется после Шага 4.
3. Zenodo / CITATION.cff — при желании поднять версию на 1.4.0 (monograph v22).

## Шаг 6. Отдельные мелкие файлы

```bash
cp <путь-к-пакету>/README_FRAGMENT_EN.md docs/ab-cloud-v22/en/text/
cp <путь-к-пакету>/README_FRAGMENT_ZH.md docs/ab-cloud-v22/zh/text/
```

(Фрагменты приложены к пакету этим скриптом распространения.)

## Чек-лист результата

- [ ] В `docs/` нет ни одного старого AB-cloud docx
- [ ] В `papers/` нет ни одного старого AB-cloud pdf
- [ ] `docs/ab-cloud-v22/{ru,en,zh}/text/` содержат md + html + docx + pdf + pptx + preprint/{tex,pdf}
- [ ] `docs/ab-cloud-v22/{ru,en,zh}/figures/` — по 19 PNG 600 dpi
- [ ] `code/ab_cloud_v19.jl` заменяет предыдущую версию сюиты; `--quick` выполняет оба прохода
- [ ] Корневой README указывает на новые пути
