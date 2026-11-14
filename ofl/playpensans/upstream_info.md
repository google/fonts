# Playpen Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Playpen Sans was investigated. The upstream repository is hosted at https://github.com/TypeTogether/Playpen-Sans and the pinned commit is `354fed4e5d1397aa3a092e6baa41b0064c8340b5` on the `main` branch.

## Font Description

Playpen Sans is a handwriting-style sans serif variable font developed by TypeTogether, a type foundry. The design team included Laura Meseguer, Veronika Burian, José Scaglione, Kostas Bartsokas, Vera Evstafieva, Tom Grace, and Yorlmar Campos. The font was added to Google Fonts on 2023-09-07.

It was designed with a broad, multi-script scope, supporting Latin, Cyrillic, Cyrillic Extended, Greek, Vietnamese, mathematical symbols, and emoji subsets. The variable font covered a weight range from ExtraLight (100) to ExtraBold (800). A minisite was maintained at https://www.type-together.com/making-playpen-sans detailing the design process.

## Repository

- **Repository**: https://github.com/TypeTogether/Playpen-Sans
- **Commit**: `354fed4e5d1397aa3a092e6baa41b0064c8340b5`
- **Branch**: main
- **Config**: `sources/config-LGC.yaml`

## Font Files

The Google Fonts distribution included one variable font file:
- `PlaypenSans[wght].ttf`

## Axes

| Axis | Min | Max |
|------|-----|-----|
| wght | 100.0 | 800.0 |

## Scripts and Subsets

The font supported Cyrillic, Cyrillic Extended, Emoji, Greek, Latin, Latin Extended, Math, and Vietnamese character sets.

## Designer

TypeTogether — a collaborative type foundry. Contributing designers: Laura Meseguer, Veronika Burian, José Scaglione, Kostas Bartsokas, Vera Evstafieva, Tom Grace, Yorlmar Campos.

## License

Open Font License (OFL).

## Notes

The config file used was `config-LGC.yaml` (Latin/Greek/Cyrillic), suggesting additional per-script configurations may exist in the repository for other writing systems. The minisite URL at type-together.com documented the making of the font in detail.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`354fed4e`](https://github.com/TypeTogether/Playpen-Sans/commit/354fed4e) to [`e9de3f5d`](https://github.com/TypeTogether/Playpen-Sans/commit/e9de3f5d), the commit named by [google/fonts `19d2b3eb`](https://github.com/google/fonts/commit/19d2b3eb) ("Playpen Sans: Version 2.000 added"). The back-fill ([google/fonts `1aeb8cfe`](https://github.com/google/fonts/commit/1aeb8cfe)) recorded `354fed4e`, an "Automated rebuild" 84 minutes later on the `builder2` line. That line branched off before [`491b4680`](https://github.com/TypeTogether/Playpen-Sans/commit/491b4680) ("Fix spacing tonos grek") and was merged back on 2025-03-19, so its LGC binary is not the shipped one.

The shipped `PlaypenSans[wght].ttf` (md5 `d0299b039058ae38768b242f46c40a93`) is byte-identical to `fonts/variable/PlaypenSans[wght].ttf` at `e9de3f5d` (on `main`). `sources/config-LGC.yaml` and the `files` paths exist there. The Arabic, Deva, Hebrew and Thai families were checked too: each one's shipped VF is byte-identical to the binary at its own pin.
