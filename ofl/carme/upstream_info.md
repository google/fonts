# Investigation: Carme

## Source Data

| Field | Value |
|---|---|
| Family Name | Carme |
| Designer | Ruben Prol |
| License | OFL |
| Date Added | 2011-07-27 |
| Repository URL | https://github.com/librefonts/carme |
| Commit Hash | `823391960931cedd0b9cb7caf0fcae71c4bd59ba` |
| Branch | (not specified) |
| Config YAML | None in upstream |
| Override Config | Yes (in google/fonts) |
| Status | complete |

## How URL Found

The repository URL `https://github.com/librefonts/carme` was added by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)") on 2024-01-14. This is a librefonts mirror repository containing the font sources.

## How Commit Determined

The commit hash `823391960931cedd0b9cb7caf0fcae71c4bd59ba` was added in a later commit `655a112a5` by Felipe Sanches on 2025-12-11, referencing google/fonts original commit `90abd17b4f97671435798b6147b698aa9087612f` (the "Initial commit" of the google/fonts repository).

This commit is the HEAD (latest) commit of the upstream repository, with the message "update .travis.yml". The repository has 12 commits total, starting from "Move carme font files to separate repository" up through various Travis CI configuration updates.

Since the font was in the initial google/fonts commit (2014, predating the librefonts repo migration), the HEAD commit is a reasonable reference as the librefonts repo represents the full history of the font project.

## Verification

- **Commit exists in upstream repo**: Yes. `8233919` is the HEAD of the master branch.
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/carme/`.
- **Source files**: The repo contains `src/Carme-Regular-TTF.sfd` (FontForge SFD format) and various TTX decomposed files.

## Config YAML Status

**Override config.yaml exists in google/fonts.** The file `google/fonts/ofl/carme/config.yaml` contains:

```yaml
buildVariable: false
sources:
  - src/Carme-Regular-TTF.sfd
```

This override was added in commit `655a112a5` on 2025-12-11. There is no config.yaml in the upstream repository itself. The override points to the SFD file in the upstream repo, which is the only buildable source.

Per project policy, when an override config.yaml exists in the google/fonts family directory, the `config_yaml` field can be omitted from the METADATA.pb source block.

## Confidence Level

**HIGH** -- The repository URL is a well-known librefonts mirror. The commit hash points to the latest commit (HEAD), which is appropriate since the font was part of the initial google/fonts commit before the librefonts repos existed. The override config.yaml correctly references the SFD source file.

## Open Questions

- None. This family is complete with the override config.yaml providing build configuration.
