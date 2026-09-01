# Beiruti - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Beiruti |
| Repository URL | https://github.com/googlefonts/beiruti |
| Commit Hash | bd45772aeff26f3ed83faa1efbb52a30b39608f2 |
| Config YAML | (none in upstream; override in google/fonts) |
| Status | complete |
| Category | SANS_SERIF |
| Designer | Boutros Fonts, Arlette Boutros, Volker Schnebel |
| Date Added | 2024-06-07 |
| Primary Script | Arab (Arabic) |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/beiruti` was recorded in the gftools-packager commit messages when the font was both initially added and later updated. The initial commit `2a93129ba` ("Beiruti: Version 1.00 added", June 2024) states:

> "Taken from the upstream repo https://github.com/googlefonts/beiruti at commit https://github.com/googlefonts/beiruti/commit/f6d75f1afbc5a0315a426a62dd7e6bf123ca218c."

The subsequent update commit `9b9cbd55e` ("Beiruti: Version 1.41 added") references the current commit hash.

## How the Commit Hash Was Determined

The commit hash `bd45772aeff26f3ed83faa1efbb52a30b39608f2` was recorded in the gftools-packager commit message for the Version 1.41 update (commit `9b9cbd55e` in google/fonts, by Emma Marichal):

> "Taken from the upstream repo https://github.com/googlefonts/beiruti at commit https://github.com/googlefonts/beiruti/commit/bd45772aeff26f3ed83faa1efbb52a30b39608f2."

**Notable discrepancy**: PR #7892, which proposed this update, originally referenced a different commit (`1d848d465d697dc6c61782818a382b80bc78c40c`, dated June 27, 2024). However, the final merge commit uses `bd45772` (dated July 22, 2024). Investigation confirms that `1d848d4` is an ancestor of `bd45772`, meaning the PR was updated during review to use a newer upstream commit. The commit `bd45772` is titled "Updated the Source Files and fonts to Version 1.41".

### Font Update History

1. **Version 1.00** (June 7, 2024): Initial addition, commit `2a93129ba` by Yanone, upstream commit `f6d75f1afbc5a0315a426a62dd7e6bf123ca218c`
2. **Version 1.41** (October 17, 2024): Update, commit `9b9cbd55e` by Emma Marichal (PR #7892), upstream commit `bd45772aeff26f3ed83faa1efbb52a30b39608f2`

## Config YAML Status

**No config.yaml exists** in the upstream repository at the recorded commit. The upstream repo at commit `bd45772` contains:
- `Source/` directory with source files
- `build.sh` script
- `fonts/` directory with built fonts
- No `config.yaml` or `builder.yaml`

However, an **override config.yaml exists** in the google/fonts family directory at `ofl/beiruti/config.yaml`:

```yaml
buildVariable: true
sources:
  - Source/2-Production/BeirutiVF.designspace
```

This override was added in commit `e40f28ec0` ("sources info for Beiruti: Version 1.41 (PR #7892)") in google/fonts. Since the override exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb `source` block.

## Verification

- **Repository exists**: Yes, cached at `upstream_repos/fontc_crater_cache/googlefonts/beiruti/`
- **Commit exists**: Yes, `bd45772` confirmed ("Updated the Source Files and fonts to Version 1.41", dated 2024-07-22)
- **Commit hash matches merge commit reference**: Yes, the final merge commit `9b9cbd55e` references `bd45772` (even though the PR body originally referenced an earlier commit `1d848d4`)
- **Override config.yaml exists**: Yes, at `ofl/beiruti/config.yaml` pointing to `Source/2-Production/BeirutiVF.designspace`
- **Source block in METADATA.pb**: Has repository_url, commit, branch, and file mappings (config_yaml correctly omitted due to override)
- **Ancestry verified**: `1d848d4` (PR body reference) is confirmed ancestor of `bd45772` (actual used commit)

## Confidence Level

**High** - The commit hash is verified through the merge commit message in google/fonts. The discrepancy between the PR body and the actual merge commit is explained by the PR being updated during review. The override config.yaml properly references the designspace source. All data is consistent.

## Open Questions

None. This family is fully documented and verified.
