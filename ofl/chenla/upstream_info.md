# Chenla - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Chenla |
| **Designer** | Danh Hong |
| **License** | OFL |
| **Category** | DISPLAY |
| **Date Added** | 2011-03-02 |
| **Repository URL** | https://github.com/librefonts/chenla |
| **Commit Hash** | e90a349be27913a318f18470ac16c358ea316fa4 |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | no_upstream_repo (needs update) |

## How URL Found

The repository was discovered at `https://github.com/librefonts/chenla`, which is already cloned in the upstream cache at `upstream_repos/fontc_crater_cache/librefonts/chenla/`. The remote URL was verified via `git remote -v`.

The tracking JSON currently shows `no_upstream_repo` status with no repository_url, but the librefonts archive does exist and contains this font.

## How Commit Determined

The repository has only a single commit:

```
e90a349 update .travis.yml
```

HEAD is `e90a349be27913a318f18470ac16c358ea316fa4`. As the sole commit, this is the only possible reference point.

In google/fonts, the font history shows:
1. `90abd17b4` - Initial commit (original onboarding)
2. `84b31698c` - "Fix cmaps for Chenla and Palanquin (#4041)" (2021-11-08, by Marc Foley) - a hotfix to the cmap table in the binary font

The cmap fix PR (#4041) was a direct binary fix by Marc Foley, not based on an upstream source rebuild.

## Config YAML Status

**No config.yaml possible.** The upstream repository contains only TTX (XML) decompositions of the binary font. There are no editable source files:
- No `.sfd`, `.glyphs`, `.ufo`, `.designspace`, or `.vfb` files
- The `src/` directory contains only `VERSIONS.txt`
- The repository is purely an archive of decomposed TTX tables

This is a Khmer script font (primary_script: "Khmr") by Danh Hong, originally from the NiDA (National ICT Development Authority) Khmer font project. The original source files may have been created in a format not preserved in this archive.

## Verification

- **Repository URL**: Verified - cloned and accessible, remote points to `https://github.com/librefonts/chenla`
- **Commit hash**: Verified - is the only commit in the repo
- **Tracking data**: Needs update - tracking JSON says `no_upstream_repo` but the librefonts archive exists

## Confidence Level

**HIGH** for repository URL and commit hash. The librefonts repo is the recognized archive, and with only one commit there is no ambiguity.

**N/A** for config.yaml -- no buildable source files exist in the upstream repo.

## Open Questions

1. The tracking JSON should be updated to reflect the known upstream URL (`https://github.com/librefonts/chenla`) and commit hash (`e90a349be27913a318f18470ac16c358ea316fa4`). The status should change from `no_upstream_repo` to `missing_config`.
2. The original source files for this Khmer font were not preserved. The designer (Danh Hong) may have used a tool like FontCreator or another Khmer-specific font editor.
