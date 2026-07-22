# Istok Web — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/m4rc1e/Istok-Web |
| Commit | `f995ade61785c37629bed658e1898096ad934ec5` |
| Confidence | High |

## Source Types

The repository contains Glyphs sources:
- `sources/IstokWeb.glyphs` — Roman styles
- `sources/IstokWeb-Italic.glyphs` — Italic styles

## Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs sources could potentially be built with gftools-builder given an override config.

## Investigation Notes

This is Marc Foley's community maintenance repository for Istok Web. The original font was designed by Andrey V. Panov. The binary in google/fonts dates from the initial commit (2015-03-07). Marc Foley's repo contains modernized Glyphs sources suitable for future rebuilds.

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Marc Foley (m4rc1e) is a well-known Google Fonts contributor who maintains community repos for many fonts.

## Correction (2026-05-28) — override config source path

**Model**: Claude Opus 4.8

fontc_crater reported `missing source 'IstokWeb-Italic.glyphs'` for this family. The override `config.yaml` listed the sources as `IstokWeb.glyphs` / `IstokWeb-Italic.glyphs`, paths that fontc_crater resolves relative to the repository root, where no such files exist. In the upstream tree at the pinned build commit `f995ade6` the Glyphs sources are under `sources/`: **`sources/IstokWeb.glyphs`** and **`sources/IstokWeb-Italic.glyphs`**.

The override `config.yaml` source paths were corrected to add the `sources/` prefix. The pinned commit is unchanged. Verified: `git -C <Istok-Web> ls-tree f995ade6 -- sources/` lists both `sources/IstokWeb.glyphs` and `sources/IstokWeb-Italic.glyphs`.
