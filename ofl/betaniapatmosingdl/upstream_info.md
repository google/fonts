# Betania Patmos In GDL - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos In GDL |
| Repository URL | https://github.com/huertatipografica/betania-patmos |
| Commit Hash | 08c83ac9540b0b2bf86ddf6b632651142f31a93c |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | HANDWRITING |

## How the Repository URL Was Found

The repository URL `https://github.com/huertatipografica/betania-patmos` is present in the METADATA.pb `source{}` block, which was set when the font was first added to google/fonts. It is also referenced in the copyright field of the font metadata and confirmed by PR #10151, which explicitly states it was "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos".

## How the Commit Hash Was Determined

The commit hash `08c83ac9540b0b2bf86ddf6b632651142f31a93c` was recorded directly in the METADATA.pb when the font was added to google/fonts in commit `e7a90689` (2026-01-23) by Emma Marichal. The commit message explicitly states: "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c."

PR #10151 (by emmamarichal) confirms this same commit hash in its body. The upstream commit is a merge commit: "Merge pull request #4 from emmamarichal/main - build fonts".

## Config YAML Status

The upstream repository has `sources/config.yaml` at the recorded commit. Verified via GitHub API, the config contains:

```yaml
sources:
  - betania-patmos.glyphs
buildVariable: false
buildStatic: true
buildTTF: true
buildOTF: true
buildWebfont: true
checkCompatibility: false
interpolate: false
cleanUp: true
```

The `config_yaml: "sources/config.yaml"` field is not yet in the METADATA.pb on the main branch of google/fonts, but it exists in a pending PR branch (`sources_info_2026-02-25`). No override config.yaml exists in the google/fonts family directory.

Note: The METADATA.pb uses `files{}` blocks to copy pre-built TTFs directly from the upstream repo, rather than building from source.

## Verification

- **Repository exists**: Yes, confirmed via GitHub API
- **Commit hash exists**: Yes, verified via GitHub API (sha matches)
- **Upstream repo NOT in local cache**: The repo is not cloned to `upstream_repos/fontc_crater_cache/`
- **Config.yaml exists at recorded commit**: Yes, at `sources/config.yaml`
- **Font was recently added**: Date added 2026-01-23, making this a very recent onboarding

## Confidence Level

**High** - The commit hash was set at onboarding time by the font engineer (Emma Marichal) and is explicitly referenced in both the METADATA.pb and the PR body. The font was added very recently (January 2026), so the provenance trail is clear and well-documented.

## Open Questions

- The upstream repo is not yet cloned to the local cache. Should it be cloned?
- The `config_yaml` field in METADATA.pb is pending in a PR branch; once merged, this family will be fully documented.
