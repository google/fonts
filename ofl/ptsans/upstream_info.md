# PT Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream GitHub repository was found for PT Sans. ParaType does not maintain a public GitHub repository for the PT font families. No METADATA.pb changes were made.

## Designer

ParaType (yakupov@paratype.com). Copyright 2009 ParaType Ltd.

## Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry.
- **GitHub organization**: The `paratype` GitHub organization exists but contains only two unrelated repositories (`paratype/paratype.github.io` and `paratype/MauiLifecycleEvents`) — no font source repositories.
- **GitHub search**: Searches for "PT Sans paratype OFL", "PT fonts paratype sans serif", and "PT Sans cyrillic OFL" returned no canonical designer-owned repository.
- **Third-party mirrors**: The `openela-main/paratype-pt-sans-fonts` repository was found (updated January 2024) but is a Linux distribution packaging mirror for OpenELA, not a canonical designer repository.
- **paratype.com**: The ParaType website is an Angular application; no source repository link was found.

## Context

PT Sans is part of the PT (Public Type) family, commissioned by the Federal Agency on Press and Mass Communications of the Russian Federation. Designed by Alexandra Korolkova with assistance from Olga Umpeleva and Vladimir Yefimov under the leadership of Paratype, it was released in 2009. PT Sans covers Latin and Cyrillic scripts with Regular, Bold, Italic, Bold Italic variants plus PT Sans Caption and PT Sans Narrow optical sizes.

## Verdict

**No canonical upstream repository found.** PT Sans is distributed by ParaType but no public source repository exists. No METADATA.pb changes were made.
