# Investigation Report: Enriqueta

## Family Details

- **Family name**: Enriqueta
- **Designer**: FontFuror (Viviana Monsalve & Gustavo Ibarra)
- **License**: OFL
- **Category**: SERIF
- **Date added**: 2011-12-13
- **Styles**: Regular (400), Medium (500), SemiBold (600), Bold (700)
- **Path in google/fonts**: `ofl/enriqueta/`

## Repository URL

- **URL**: https://github.com/vv-monsalve/Enriqueta_2019
- **Source**: METADATA.pb `source {}` block, added by Simon Cozens in commit `cd5db6b6e` ("Update upstreams", 2023-12-14)
- **Confirmed by**: PR #1933 body and commit message both explicitly reference this repo
- **Status**: Valid, accessible, repo is clean and up-to-date in cache at `upstream_repos/fontc_crater_cache/vv-monsalve/Enriqueta_2019/`

## Commit Hash

- **Commit**: `c1dbf07dd69dc7146e073a549810166587c65de3`
- **Date**: 2019-04-10
- **Message**: "Merge pull request #1 from m4rc1e/gf-mastering" -- merges Marc Foley's "v2.000 mastered for Google Fonts" PR into the upstream repo
- **Source of hash**: Explicitly stated in both the google/fonts commit message (`58c23711f`) and the PR #1933 body: "Taken from the upstream repo https://github.com/vv-monsalve/Enriqueta_2019 at commit c1dbf07dd69dc7146e073a549810166587c65de3"
- **Confidence**: HIGH

### Cross-verification

The binary font files in google/fonts (74K each) are **larger** than the fonts stored in the upstream repo at commit `c1dbf07` (71K each). This indicates Marc Foley rebuilt the fonts from the `.glyphs` source file (using Google Fonts tooling which adds metadata like `DSIG`, `GDEF`, etc.) rather than simply copying the pre-built TTFs from the upstream `fonts/` directory. This is normal onboarding behavior -- the commit hash references the source state, not necessarily a binary match.

### Post-onboarding upstream changes

After commit `c1dbf07` (2019-04-10), the upstream repo had further activity:
- 2019-04-10: Deleted `fonts/text` file
- 2019-04-20: Renamed source file from `enriqueta_masters_-GOOGLE.glyphs` to `enriqueta_masters_GOOGLE.glyphs` (removed dash), added AUTHORS.txt and CONTRIBUTORS.txt, uploaded new source file
- 2019-04-23: Deleted the TTF files from the `fonts/` directory (cleanup)
- 2019-08-07: Updated OFL.txt (PR #2, branch `qavv5`)

These post-onboarding changes did NOT affect the source design itself (the `.glyphs` file was re-uploaded with a name fix, not content changes), so the commit hash `c1dbf07` accurately represents the design state used for onboarding.

## Build Configuration

- **Upstream config.yaml**: None. The upstream repo has no `config.yaml` file.
- **Override config.yaml in google/fonts**: Yes, exists at `ofl/enriqueta/config.yaml`
  - Added in commit `5ddf312e6` ("Add config_yaml enrichment for 82 font families", 2026-02-20)
  - Contents: `sources: [source/enriqueta_masters_GOOGLE.glyphs]`
  - **Note**: This references the **current** filename (without dash). At the onboarding commit `c1dbf07`, the file was named `enriqueta_masters_-GOOGLE.glyphs` (with dash). The override config uses the current HEAD filename, which is appropriate for building from the latest upstream state.
- **config_yaml field in METADATA.pb**: Not set (correctly omitted since override config exists in google/fonts, and google-fonts-sources auto-detects it)

## Source Files

At the onboarding commit `c1dbf07`:
- `source/enriqueta_masters_-GOOGLE.glyphs` -- Glyphs source file (note the dash in the name)
- `fonts/Enriqueta-{Regular,Medium,SemiBold,Bold}.ttf` -- Pre-built TTFs

At HEAD (`b089cc3`):
- `source/enriqueta_masters_GOOGLE.glyphs` -- Glyphs source file (dash removed from name)
- No pre-built TTFs (deleted in April 2019 cleanup)

## google/fonts History

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| `90abd17b4` | 2015-03-07 | Initial | Initial commit (Regular + Bold only) |
| `58c23711f` | 2019-04-10 | Marc Foley | v2.000 added (4 styles, from upstream `c1dbf07`) |
| `f113126dc` | 2019-07-12 | Marc Foley | Merge PR #1933 |
| `cd5db6b6e` | 2023-12-14 | Simon Cozens | Added `source { repository_url }` to METADATA.pb |
| `5ddf312e6` | 2026-02-20 | Felipe Sanches | Added override `config.yaml` |

## PR History

- **PR #1933** (google/fonts): "enriqueta: v2.000 added." by Marc Foley (@m4rc1e), merged 2019-07-12. Body explicitly states the upstream repo and commit hash.
- **PR #1** (upstream): "v2.000 mastered for Google Fonts" by Marc Foley, merged into vv-monsalve/Enriqueta_2019 on 2019-04-10. This is the commit referenced for onboarding.

## METADATA.pb Source Block

Current state:
```
source {
  repository_url: "https://github.com/vv-monsalve/Enriqueta_2019"
}
```

Recommended complete state:
```
source {
  repository_url: "https://github.com/vv-monsalve/Enriqueta_2019"
  commit: "c1dbf07dd69dc7146e073a549810166587c65de3"
}
```

Note: `config_yaml` field should remain omitted because the override `config.yaml` in google/fonts is auto-detected.

## Status

- **Status**: complete (pending commit hash addition to METADATA.pb)
- **Confidence**: HIGH
- **What's needed**: Add `commit: "c1dbf07dd69dc7146e073a549810166587c65de3"` to the source block in METADATA.pb
- **Override config**: Already in place at `ofl/enriqueta/config.yaml`
