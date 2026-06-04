# Investigation: Carter One

## Source Data

| Field | Value |
|---|---|
| Family Name | Carter One |
| Designer | Vernon Adams |
| License | OFL |
| Date Added | 2011-05-04 |
| Repository URL | https://github.com/librefonts/carterone |
| Commit Hash | `9943144e585a736a95509a85b92fbf2bb29060c2` |
| Branch | master |
| Config YAML | None |
| Override Config | No |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/carterone` was recorded in the tracking data and added to the METADATA.pb source block in commit `9a14639f3` on branch `sources_info_2026-02-25` (not yet merged to main). This is a librefonts mirror repository.

## How Commit Determined

The commit hash `9943144e585a736a95509a85b92fbf2bb29060c2` is the HEAD (and only) commit of the upstream repository, with the message "update .travis.yml". The repository has only a single commit.

The font was part of the initial google/fonts commit (`90abd17b4`). No subsequent updates to the font binary have been made in google/fonts -- the TTF has remained unchanged since the initial commit.

## Verification

- **Commit exists in upstream repo**: Yes. `9943144` is the HEAD and sole commit.
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/carterone/`.
- **Source files present**: The `src/` directory contains:
  - `CarterOne-TTF.sfd` -- FontForge SFD format (buildable)
  - `CarterOne.vfb` -- FontLab Studio binary format (not buildable by gftools-builder)
  - `METADATA_comments.txt` and `VERSIONS.txt` -- documentation files

## Config YAML Status

**SFD source available but no config.yaml.** Unlike the Carrois Gothic families which only have VFB files, Carter One has an SFD (FontForge Spline Font Database) file at `src/CarterOne-TTF.sfd`. SFD files can potentially be used with gftools-builder.

However, no config.yaml exists in the upstream repository, and no override config.yaml exists in the google/fonts family directory.

An override config.yaml could be created with:

```yaml
buildVariable: false
sources:
  - src/CarterOne-TTF.sfd
```

This would make the family buildable, similar to what was done for Carme.

## Confidence Level

**HIGH** -- The commit hash is the only commit in the single-commit repository. The repository URL is a standard librefonts mirror. The font binary in google/fonts has been unchanged since the initial commit, consistent with using the HEAD of the upstream.

## Open Questions

- An override config.yaml could be created in google/fonts to make this family buildable from SFD sources. This would change the status from `missing_config` to `complete`.
- It should be verified that building from the SFD source produces output matching (or acceptably close to) the current binary in google/fonts before creating such an override.
- Vernon Adams, the original designer, passed away in 2014. Any updates to this font would need to be handled by the community.
