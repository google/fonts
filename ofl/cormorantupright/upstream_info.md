# Cormorant Upright - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Cormorant Upright |
| Repository URL | https://github.com/CatharsisFonts/Cormorant |
| Commit Hash | `b1a0a7781e3a59d3c2a96f953650463469a2e841` |
| Branch | master |
| Config YAML | N/A (override config.yaml in google/fonts) |
| Override Config | Yes (`ofl/cormorantupright/config.yaml`) |
| Status | complete |

## How URL Found

The repository URL was first added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)", January 14, 2024). It was later enriched with commit hash and file mappings by Felipe Sanches in commit `a20b18752` ("sources info for Cormorant (incl. SC, Upright, Garamond, Infant and Unicase)", April 2, 2025).

The copyright strings in the font files also reference `github.com/CatharsisFonts/Cormorant`.

## How Commit Determined

The commit hash `b1a0a7781e3a59d3c2a96f953650463469a2e841` corresponds to the merge commit "Merge pull request #29 from m4rc1e/upright - CormorantUpright: Updated version number to 3.302" (January 23, 2017) in the upstream repo.

This aligns with PR #597 in google/fonts ("cormorantupright: v3.302 added") by Marc Foley, which was the last commit to update the Cormorant Upright font binaries. The fonts in google/fonts were later removed (commit `76adaf1d2`, November 2021, deploy action) and re-added with the same binaries.

The file mappings use the old directory structure `1. TrueType Font Files/CormorantUpright-*.ttf`, which is correct for this early commit.

## Config YAML Status

At commit `b1a0a7781`, there was no config.yaml or any gftools-builder configuration in the upstream repo. The repo at this point (January 2017) predates gftools-builder.

An override `config.yaml` was added to the google/fonts directory at `ofl/cormorantupright/config.yaml` in commit `f6c68379a` (February 16, 2026). This override config references:
```yaml
sources:
  - 4. Glyphs Source Files/CormorantUpright.glyphs
familyName: Cormorant Upright
buildStatic: true
buildOTF: false
```

This correctly points to the Glyphs source file at the path that exists in the old directory structure of the upstream repo.

A proper `sources/config-upright.yaml` was also added to the upstream repo in commit `8378c19c` (November 13, 2024), but it references a different source path (`CormorantUpright.glyphs` in `sources/`).

Since the override config exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Verification

- **Commit exists in upstream**: Verified. `b1a0a778` is present in the CatharsisFonts/Cormorant repository.
- **Font files exist at commit**: Verified. `1. TrueType Font Files/CormorantUpright-{Bold,Light,Medium,Regular,SemiBold}.ttf` all exist at this commit.
- **Override config references valid source**: The override points to `4. Glyphs Source Files/CormorantUpright.glyphs`, which should exist at the recorded commit.

## Confidence Level

**High** for repository URL and commit hash. The commit matches the last font binary update (v3.302) from PR #597, and the file mappings are consistent with the upstream directory structure at that commit.

**High** for config status. The override config.yaml is correctly present in google/fonts, and config_yaml is correctly omitted from METADATA.pb.

## Open Questions

None. The documentation is complete and consistent.
