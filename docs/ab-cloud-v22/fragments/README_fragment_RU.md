<!-- ab-cloud:v22 edition:2026-08-28 (managed block — replaces the legacy AB-Cloud section; heading/anchor preserved for the README TOC) -->
### AB-Cloud & Riemann Zeros

**AB-облако** — гамильтониан Хофштадтера с топологическими вихрями (фазами Ааронова–Бома). Издание v22 (2026-08-28): монография переписана с нуля на основе 37-тестовой верифицированной сюиты (v19); прежние docx/pdf этого раздела удалены, см. [REPLACE_GUIDE](docs/ab-cloud-v22/REPLACE_GUIDE.md).

- ⟨r⟩ = 0.5848 ± 0.0260 против GUE 0.5992 (отклонение −2.4%); сходимость по L: 0.548 → 0.595 при L: 10 → 50;
- топология с машинной точностью: потоки 10⁻¹⁴, Байерс–Янг 3.5·10⁻¹⁵, самодуальность Конна (4 нулевые моды), C₁ = 2;
- корреляционная дыра Монтгомери воспроизведена: R₂ облака ближе к GUE, чем к Пуассону (d_GUE = 0.140 < d_Pois = 0.227); конечновыборочные поправки Берри количественно объясняют отклонения на достижимых высотах;
- дираковская динамика: E_min ∝ 1/L (R² = 0.9997), провал DOS 20×, скин-эффект.

Документы: [RU](docs/ab-cloud-v22/ru/text) · [EN](docs/ab-cloud-v22/en/text) · [ZH](docs/ab-cloud-v22/zh/text) — docx + pdf + интерактивный html + презентация pptx + LaTeX-препринт (tex/pdf); 19 графиков 600 dpi на язык ([RU](docs/ab-cloud-v22/ru/figures) · [EN](docs/ab-cloud-v22/en/figures) · [ZH](docs/ab-cloud-v22/zh/figures)). Код: [ab_cloud_v19.jl](code/ab_cloud_v19.jl) · эталонный прогон: [37-тестовый лог](results/verification_run_v18_37tests_2026-08-28.txt).

Оригинальная авторская монография v21 (с верификацией) и её английская версия: [RU](docs/ab-cloud-v22/original-v21/ru/text) · [EN](docs/ab-cloud-v22/original-v21/en/text) — docx + pdf + интерактивный html + презентации (16 слайдов).
