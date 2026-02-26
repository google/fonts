# Acme

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Juan Pablo del Peral, Huerta Tipografica
**METADATA.pb path**: `ofl/acme/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/acme |
| Commit | `fa0a4445feb570b5cfc7ce4b8f6dbacc6ae5ad73` |
| Config YAML | -- |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/acme` was identified from the upstream repo cache at `upstream_repos/fontc_crater_cache/librefonts/acme`. There is no `source { }` block in METADATA.pb at all. Like Abril Fatface, the `librefonts` organization hosts a TTX-decomposed mirror of this font.

The original designer is "Juan Pablo del Peral, Huerta Tipografica". The Huerta Tipografica organization on GitHub (`huertatipografica`) has repos for several of their other fonts (Alegreya, Andada Pro, etc.) but does not have a dedicated repo for Acme. The font's copyright string references `info@huertatipografica.com.ar`.

## How the Commit Hash Was Identified

The upstream repo has only a single commit: `fa0a4445feb570b5cfc7ce4b8f6dbacc6ae5ad73` (dated 2014-10-17, message: "update .travis.yml"). This is the HEAD and only commit of the repository. The commit hash was selected as it represents the complete state of this single-commit repo.

The last font-modifying commit on the main branch of google/fonts is `a84ec9834c42` from 2017-05-01, associated with PR #743 ("hotfix-acme: v1.002 added"). PR #743's body discusses removing latin-ext from metadata.pb because it didn't match the Google Fonts API. This was a metadata hotfix, not a font binary update per se, though the TTF file was modified.

The font was added to Google Fonts on 2011-12-19 according to METADATA.pb, significantly predating the librefonts repo (2014).

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in the google/fonts family directory (`ofl/acme/`).

The upstream repo contains only legacy source formats:
- `src/Acme-Regular-TTF.sfd` (FontForge SFD format)
- `src/Acme-Regular-OTF.vfb` (FontLab VFB format)
- `src/Acme-Regular.vfb` (FontLab VFB format)
- Various `.ttx` decomposed table files

These source formats are not compatible with gftools-builder. A config.yaml cannot be meaningfully created without first converting the sources to a modern format (`.glyphs`, `.ufo`, or `.designspace`).

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2014-10-17 13:27:37 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Acme-Regular-TTF.sfd`, `src/Acme-Regular-OTF.vfb`, `src/Acme-Regular.vfb`, various `.ttx` files

## Confidence

**Medium**: The repository URL is confirmed and the commit is verified in the upstream repo. However, `librefonts/acme` is a legacy TTX mirror, not a true design source repository. The original designer (Juan Pablo del Peral / Huerta Tipografica) may have the original design sources elsewhere. The font binary in google/fonts predates this repo (2011 vs 2014), and was last updated in 2017 via a hotfix. The relationship between this repo and the font production is indirect.

## Open Questions

- Does Huerta Tipografica or Juan Pablo del Peral maintain an original source repository for Acme with `.glyphs` or `.ufo` sources?
- Since the source formats (SFD/VFB) are not gftools-builder compatible, is there a plan to convert the sources to a modern format?
- Should METADATA.pb be updated to include a `source { }` block pointing to this repo, even though it cannot be built with gftools-builder?
- PR #743 was a hotfix in 2017. Has the font had any substantive updates since its original release?
