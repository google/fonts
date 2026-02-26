# Investigation Report: Bree Serif

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Bree Serif |
| Designer | TypeTogether |
| License | OFL |
| Date Added | 2011-12-19 |
| Repository URL | https://github.com/librefonts/breeserif |
| Commit Hash | `86684a17aaa88ce2d9d85d77f9e9ce1f64c06462` |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/breeserif` was identified from the `librefonts` organization on GitHub, which hosts many libre font projects. It was added to the tracking data and a source block was prepared on branch `sources_info_2026-02-25` (commit `9a14639f3`), though this has not yet been merged to google/fonts main.

## How Commit Determined

The commit hash `86684a17aaa88ce2d9d85d77f9e9ce1f64c06462` is the only commit in the upstream repository, authored on 2014-10-17 by hash3g with message "update .travis.yml". Since the repo has only one commit, this is definitively the latest (and only) available state.

The font was originally added to google/fonts in the initial commit (`90abd17b4`) and later updated via hotfix in PR #866 (`faaf4889d`: "hotfix-breeserif: v1.002 added"). These early hotfix commits did not include upstream repo or commit hash references.

## Config YAML Status

- **No `config.yaml` exists** in the upstream repository
- **No override `config.yaml`** exists in google/fonts
- The upstream sources are in SFD (FontForge) format only: `src/BreeSerif-Regular-TTF.sfd` and `src/BreeSerif-Regular-OTF.vfb`
- These formats are not compatible with gftools-builder, so no config.yaml can be created
- The family is correctly marked as `missing_config` with note "SFD-only sources (FontForge format), not gftools-builder compatible"

## Verification

1. **Commit exists in upstream**: Confirmed. `86684a17aaa88ce2d9d85d77f9e9ce1f64c06462` is the sole commit in the cached repo at `upstream_repos/fontc_crater_cache/librefonts/breeserif`
2. **Source format**: SFD and VFB files only - no `.glyphs`, `.ufo`, or `.designspace` files
3. **No config.yaml possible**: Not gftools-builder compatible due to legacy source format
4. **METADATA.pb source block**: Currently not present on google/fonts main branch; prepared on branch `sources_info_2026-02-25` with `repository_url` and `commit` only (no `config_yaml` field)

## Confidence Level

**HIGH** - The repo has only one commit, so the hash is unambiguous. The URL is the correct librefonts mirror. The lack of config.yaml is expected since the sources are in FontForge SFD format, which predates the gftools-builder workflow.

## Open Questions

1. The source block for this family has been prepared but is not yet merged to google/fonts main (pending PR on `sources_info_2026-02-25` branch).
2. TypeTogether may have more recent sources for Bree Serif in a different format (Glyphs/UFO), but the librefonts repository only contains the legacy SFD sources.
