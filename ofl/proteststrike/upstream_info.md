# Protest Strike — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Protest Strike was investigated. The upstream repository is hosted at https://github.com/octaviopardo/Protest and the pinned commit is `094e74050a0547c8decd760b4f926321a5e72c6e` on the `master` branch. All four Protest family members (Guerrilla, Revolution, Riot, Strike) shared the same repository and commit.

## Font Description

Protest Strike is a display typeface and part of the Protest Types project by designer Octavio Pardo. The project began as a personal exploration of the shapes and voices of protest signage. Protest Strike was described as a solid but peaceful sans serif typeface — the most restrained voice in the family.

Strike, Guerrilla, and Riot all shared identical spacing and kerning, enabling designers to switch between these three voices without altering line lengths or page layouts. Strike served as the baseline design from which Guerrilla (a stencil version) was derived.

The font was added to Google Fonts on 2023-12-13.

## Repository

- **Repository**: https://github.com/octaviopardo/Protest
- **Commit**: `094e74050a0547c8decd760b4f926321a5e72c6e`
- **Branch**: master
- **Config**: `sources/config-Strike.yaml`

## Font Files

The Google Fonts distribution included one static font file:
- `ProtestStrike-Regular.ttf`

The source files mapping pointed to `fonts/ProtestStrike/ttf/ProtestStrike-Regular.ttf` in the repository.

## Scripts and Subsets

The font supported Latin, Latin Extended, Math, Symbols, and Vietnamese character sets.

## Designer

Octavio Pardo.

## License

Open Font License (OFL). Copyright 2020 The Protest Project Authors.

## Notes

The repository contained all four Protest family variants. Each variant used its own per-family config YAML (`config-Strike.yaml`, etc.) and stored fonts in separate subdirectories under `fonts/`. The repository was hosted under the `octaviopardo` personal GitHub account.
