# Newsreader — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/productiontype/NewsReader
- **Branch**: master
- **Pinned commit**: `1ece6a8bfe5db1a2b90c76cc1fe5d3b2eed5dcf3`
- **Designer**: Production Type
- **License**: OFL

The repository URL resolves correctly (HTTP 200). The METADATA.pb uses `https://github.com/productiontype/NewsReader` (capital R in NewsReader). The copyright notice uses `http://github.com/productiontype/Newsreader` (lowercase r, http) — a mismatch in both protocol and casing. The HTTPS version of the lowercase URL (`https://github.com/productiontype/Newsreader`) also resolves correctly (GitHub redirects case-insensitively). No local cache exists at `/mnt/shared/upstream_repos/fontc_crater_cache/productiontype/`.

## Source Files

The METADATA.pb maps:
- `OFL.txt` → `OFL.txt`
- `DESCRIPTION.en_us.html` → `DESCRIPTION.en_us.html`
- `fonts/variable/ttf/Newsreader[opsz,wght].ttf` → `Newsreader[opsz,wght].ttf`
- `fonts/variable/ttf/Newsreader-Italic[opsz,wght].ttf` → `Newsreader-Italic[opsz,wght].ttf`
- 36 static TTF files from `fonts/static/ttf/` spanning 6pt, 16pt, and 72pt optical sizes

The family is a variable font with two axes: `opsz` (6–72, default 16) and `wght` (200–800). Both upright and italic variable fonts are present. Static instances cover three optical sizes (6pt, 16pt, 72pt) across the full weight range in both styles.

## Build System

A `config.yaml` is present in the `ofl/newsreader/` directory in google/fonts. It references four designspace files:

```yaml
buildVariable: true
sources:
  - sources/NewsreaderVF-upright.designspace
  - sources/NewsreaderVF-italics.designspace
  - sources/NewsreaderStatic-upright.designspace
  - sources/NewsreaderStatic-italics.designspace
```

This is a fully specified gftools/fontmake build pipeline producing both variable and static fonts. The build is driven by multiple designspace files in the upstream `sources/` directory.

Sources info was introduced via PR #2837 (`db2573db8`).

## config.yaml Status

**Present** in `ofl/newsreader/config.yaml`. The build configuration is complete and up to date, specifying variable builds from designspace sources. No changes needed to the config.yaml.

## Notes

- The copyright notice uses `http://` (not `https://`) and lowercase `Newsreader` while the `repository_url` in METADATA.pb uses `https://` and `NewsReader` (capital R). The copyright line is embedded in the font binary and cannot be corrected here; the METADATA.pb `repository_url` is correctly using HTTPS.
- DESCRIPTION.en_us.html is present and links to the GitHub repo correctly.
- The family includes Vietnamese subset in addition to Latin/Latin-ext.
- This is one of the more fully documented families in this batch, with complete source metadata and a working config.yaml.
- No upstream repo cache is available locally; investigation is based on METADATA.pb, directory contents, and config.yaml.
