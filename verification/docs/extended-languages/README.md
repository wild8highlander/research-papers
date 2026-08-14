# Extended Languages

7 new verification languages added to the framework:

## Formal Proof Languages
- **Lean 4** - Mathlib4 hybrid, formal proofs
- **Coq** - Reals + Lra, formal proofs
- **Isabelle/HOL** - Complex_Main, formal proofs
- **Agda** - dependent types, formal proofs

## Numerical Languages
- **Rust** - ndarray, numerical verification
- **C++** - STL only, numerical verification
- **Haskell** - base only, numerical verification

## Build Commands

```bash
make verify-extended  # all 7 languages
make verify-formal    # Lean 4 + Coq + Isabelle + Agda
make verify-numerical # Rust + C++ + Haskell
```
