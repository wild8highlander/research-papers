# Contributing to Research Papers

Thank you for your interest in contributing to this repository! We welcome contributions that improve the quality, accuracy, and accessibility of the research.

## How to Contribute

### Reporting Issues

If you find errors, inconsistencies, or have suggestions:

1. Open a [GitHub Issue](../../issues)
2. Use a clear, descriptive title
3. Specify which document or paper is affected
4. Describe the expected vs. actual behavior

### Submitting Changes

1. **Fork** the repository
2. Create a **feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Commit with a descriptive message:
   ```bash
   git commit -m "Add: description of your change"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a **Pull Request** against `main`

### Contribution Types

| Type | Description | Example |
|------|-------------|---------|
| **Errata** | Fix typos, errors, or inaccuracies | Correct a formula, fix a reference |
| **Translation** | Add translations to existing documents | Translate a chapter from EN to RU |
| **Enhancement** | Improve existing content | Add a figure, expand a section |
| **New Content** | Add new research documents | Add a new chapter or paper |

### File Naming Conventions

- **Papers (PDF)**: `descriptive_name.pdf` in the appropriate `papers/` subdirectory
- **Documents (DOCX)**: `descriptive_name.docx` in the appropriate `docs/` subdirectory
- **LaTeX Sources**: `descriptive_name.tex` in the appropriate `src/` subdirectory
- **Bilingual content**: Place in `en/` or `ru/` subdirectories within the topic folder

### Commit Message Format

```
<type>: <subject>

<body>
```

Types: `Add`, `Fix`, `Update`, `Translate`, `Remove`

Examples:
- `Add: KdV b-correction Chapter 16 (EN)`
- `Fix: typo in Section 3 of main paper`
- `Translate: monograph Chapter 4 to Russian`
- `Update: preprint v2 with corrected appendix`

### LaTeX Contributions

When contributing LaTeX sources:

1. Use **XeLaTeX** for compilation (required for `polyglossia` and `fontspec`)
2. Ensure the document compiles without errors
3. Run **twice** to resolve cross-references and TOC
4. Keep consistent formatting with existing `.tex` files

### Code of Conduct

- Be respectful and constructive in all interactions
- Focus on the scientific content and accuracy
- Provide references or evidence for claims
- Respect the intellectual property and licensing terms

---

Thank you for helping improve this research!
