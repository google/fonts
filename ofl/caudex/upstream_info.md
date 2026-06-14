# Investigation Report: Caudex

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Caudex |
| **Designer** | Nidud (Hjort Nidudsson) |
| **License** | OFL |
| **Date Added** | 2011-05-18 |
| **Repository URL** | https://github.com/librefonts/caudex |
| **Commit Hash** | `901fb15160f96cb5a2b91e48a6d89d9c18c6f6d5` |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config (SFD-only sources) |

## How URL Was Found

The repository URL `https://github.com/librefonts/caudex` is a well-known librefonts archive repository. The cached clone at `upstream_repos/fontc_crater_cache/librefonts/caudex/` confirms the remote URL matches. The repo contains TTX decompositions and SFD sources from the original font.

## How Commit Was Determined

The upstream repository has only a single commit:
- `901fb15160f96cb5a2b91e48a6d89d9c18c6f6d5` - "update .travis.yml"

Since there is only one commit in the entire repository, this is the only possible commit to reference. The librefonts archive was created as a snapshot of existing fonts, so this single commit represents the complete state of the project.

## Config YAML Status

**No config.yaml exists and none is possible.** The upstream repo contains only SFD (FontForge Spline Font Database) source files:
- `src/Caudex-Regular.sfd`
- `src/Caudex-Italic.sfd`
- `src/Caudex-Bold.sfd`
- `src/Caudex-BoldItalic.sfd`

SFD is a FontForge-native format that is not compatible with gftools-builder. Building from these sources would require FontForge, not the standard Google Fonts build toolchain.

## Verification

- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/caudex/`
- **Commit exists**: Yes, it is the only commit in the repo
- **Font file history in google/fonts**: The TTF files were part of the initial commit (`90abd17b4`) and were never updated (the only other touch was the large deploy restructure `76adaf1d2` which reorganized the repo but did not change font binaries)
- **No override config.yaml** exists in `google/fonts/ofl/caudex/`
- **METADATA.pb** does not have a source block

## Confidence Level

**HIGH** - The repository URL and commit are unambiguous. Single commit repo, SFD-only sources. The status of "missing_config" is correct but expected since SFD sources cannot use gftools-builder.

## Open Questions

None. This is a legacy font with SFD-only sources. A config.yaml would only be possible if the font were to be converted to a gftools-builder-compatible format (e.g., .glyphs or .ufo).
