# Chela One - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Chela One |
| **Designer** | Miguel Hernandez |
| **License** | OFL |
| **Category** | DISPLAY |
| **Date Added** | 2012-10-05 |
| **Repository URL** | https://github.com/librefonts/chelaone |
| **Commit Hash** | cb9b95fc0510c91bc45664e5a62ed3893c09bfba |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/chelaone` was identified from the librefonts organization on GitHub, which hosts mirrors/archives of many early Google Fonts families. The upstream repo is cloned at `upstream_repos/fontc_crater_cache/librefonts/chelaone/`.

The repository remote confirms: `origin https://github.com/librefonts/chelaone`.

## How Commit Determined

The repository has only a single commit:

```
cb9b95f update .travis.yml
```

HEAD is `cb9b95fc0510c91bc45664e5a62ed3893c09bfba`, which is the only commit in the repository. This makes commit verification trivial -- there is only one commit, so it must be the correct one.

The font was originally added to google/fonts in commit `90abd17b4` ("Initial commit") and was last updated for binary fixes in `c72712175` ("Updating ofl/chelaone/*ttf with nbspace and fsType fixes", 2015-04-27). A source block was added to METADATA.pb on a pending PR branch (`sources_info_2026-02-25`) via commit `9a14639f3`, but this has not yet been merged to google/fonts main.

## Config YAML Status

**No config.yaml possible.** The upstream repository contains only legacy source formats:
- `src/ChelaOne-Regular-TTF.sfd` (FontForge SFD format)
- `src/ChelaOne-Regular-OTF.vfb` (FontLab VFB format)

Neither SFD nor VFB formats are compatible with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` source files. A config.yaml cannot be created without first converting the sources to a modern format.

## Verification

- **Repository URL**: Verified - cloned and accessible at `upstream_repos/fontc_crater_cache/librefonts/chelaone/`
- **Commit hash**: Verified - matches HEAD, and is the only commit in the repo
- **Source block**: Pending merge via PR branch `sources_info_2026-02-25`
- **METADATA.pb on main**: Currently has no source block (pending PR)

## Confidence Level

**HIGH** for repository URL and commit hash. The librefonts repo is the recognized upstream, and with only one commit, the hash is unambiguous.

**N/A** for config.yaml -- SFD-only sources make this impossible without source conversion.

## Open Questions

- None. This is a legacy font with SFD-only sources. It would require source conversion to a modern format (e.g., .glyphs or .ufo) before a config.yaml could be created.
