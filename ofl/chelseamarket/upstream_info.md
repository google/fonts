# Chelsea Market - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Chelsea Market |
| **Designer** | Tart Workshop |
| **License** | OFL |
| **Category** | DISPLAY |
| **Date Added** | 2012-01-04 |
| **Repository URL** | https://github.com/librefonts/chelseamarket |
| **Commit Hash** | cb0d8b1186fc376de4d6be06a568c25362e381dd |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/chelseamarket` was identified from the librefonts organization on GitHub. The upstream repo is cloned at `upstream_repos/fontc_crater_cache/librefonts/chelseamarket/`.

The repository remote confirms: `origin https://github.com/librefonts/chelseamarket`.

## How Commit Determined

The repository has only a single commit:

```
cb0d8b1 update .travis.yml
```

HEAD is `cb0d8b1186fc376de4d6be06a568c25362e381dd`, which is the only commit in the repository. As with other librefonts archives that have a single commit, there is no ambiguity about which commit to reference.

The font was originally added to google/fonts in the "Initial commit" (`90abd17b4`). Unlike Chela One, it was never updated with binary fixes -- the original binary has remained unchanged. A source block was added on a pending PR branch (`sources_info_2026-02-25`) via commit `9a14639f3`, not yet merged to main.

## Config YAML Status

**No config.yaml possible.** The upstream repository's source directory contains only:
- `src/ChelseaMarket-Regular-TTF.vfb` (FontLab VFB format)

VFB is a proprietary FontLab format that is not compatible with gftools-builder. There are no `.glyphs`, `.ufo`, `.sfd`, or `.designspace` source files. A config.yaml cannot be created without first converting the source to a modern format.

## Verification

- **Repository URL**: Verified - cloned and accessible at `upstream_repos/fontc_crater_cache/librefonts/chelseamarket/`
- **Commit hash**: Verified - matches HEAD, and is the only commit in the repo
- **Source block**: Pending merge via PR branch `sources_info_2026-02-25`
- **METADATA.pb on main**: Currently has no source block (pending PR)

## Confidence Level

**HIGH** for repository URL and commit hash. The librefonts repo is the recognized upstream, and with only one commit, the hash is unambiguous.

**N/A** for config.yaml -- VFB-only sources make this impossible without source conversion.

## Open Questions

- None. This is a legacy font with VFB-only sources. It would require conversion to a modern format before a config.yaml could be created.
