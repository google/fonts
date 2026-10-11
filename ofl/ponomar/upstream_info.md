# Ponomar — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The source metadata for Ponomar was investigated. The upstream repository is hosted at https://github.com/slavonic/Ponomar and the pinned commit is `a3023c5d838ee65b5617f3f9179269160bd177e5` on the `main` branch.

## Font Description

Ponomar is a contemporary Church Slavonic display font designed by Aleksandr Andreev. It was added to Google Fonts on 2024-12-06, on the same date as its sibling font Pochaevsk. Ponomar reproduces the typeface used in editions published by the Synodal Press of the Russian Orthodox Church in the early twentieth century, and is presently used in various liturgical books published by the Moscow Patriarchate.

Beyond Church Slavonic, the font also contained characters needed to typeset liturgical texts in Romanian (Moldovan) Cyrillic, Aleut, and Sakha (Yakut), reflecting its use across a range of Eastern Orthodox liturgical traditions.

## Repository

- **Repository**: https://github.com/slavonic/Ponomar
- **Commit**: `a3023c5d838ee65b5617f3f9179269160bd177e5`
- **Branch**: main
- **Config**: `sources/config.yaml`

## Font Files

The Google Fonts distribution included one static font file:
- `Ponomar-Regular.ttf`

## Scripts and Subsets

The font supported Cyrillic, Cyrillic Extended, and Latin character sets. The primary script was Cyrillic (`Cyrl`) and the primary language was Church Slavonic (`cu_Cyrl`).

## Designer

Aleksandr Andreev.

## License

Open Font License (OFL). Copyright 2025 The Ponomar Project Authors.

## Notes

The repository URL in the METADATA.pb used a capital "P": `https://github.com/slavonic/Ponomar`, which is the canonical casing. The source block included a `DESCRIPTION.en_us.html` in the files mapping, indicating the description was managed upstream. The font was part of the `slavonic` GitHub organization, which also maintained Pochaevsk and other Church Slavonic typography resources.
