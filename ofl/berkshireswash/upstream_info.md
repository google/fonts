# Berkshire Swash - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Berkshire Swash |
| Repository URL | https://github.com/librefonts/berkshireswash |
| Commit Hash | 1a4fb49d514e01ada8934472cae85cc4590efa58 |
| Config YAML | (none) |
| Status | missing_config |
| Category | HANDWRITING / DISPLAY |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/berkshireswash` comes from the librefonts organization on GitHub, a collection of decompiled font repos maintained by Marc Foley. The URL was recorded in the tracking data and added to METADATA.pb in commit `9a14639f3` (on branch `sources_info_2026-02-25`, not yet merged to main).

## How the Commit Hash Was Determined

The commit hash `1a4fb49d514e01ada8934472cae85cc4590efa58` is the latest (HEAD) commit in the librefonts/berkshireswash repo, dated 2014-10-17. This was set because it is the most recent commit in the repository, corresponding to a Travis CI config update ("update .travis.yml").

**Font history in google/fonts**:
- Initial commit `90abd17b4`: Font first added to google/fonts
- `5e3cf0753`: "hotfix-berkshireswash: v1.001 added" (PR #855, by Marc Foley, 2017-08-07)

The hotfix PR #855 by Marc Foley had an empty body. The librefonts repo's last commit predates the hotfix by about 3 years (2014 vs 2017).

## Config YAML Status

- **No `config.yaml`** exists in the upstream librefonts repo (not at any commit)
- **No override `config.yaml`** in `google/fonts/ofl/berkshireswash/`
- The repo contains only **VFB sources** (`src/BerkshireSwash-Regular-OTF.vfb`, `src/BerkshireSwash-Regular-TTF.vfb`, `src/BerkshireSwash-Regular.vfb`) and TTX-decomposed font files
- VFB (FontLab Studio format) is a proprietary binary format not compatible with gftools-builder
- No UFO, Glyphs, or DesignSpace sources are available

## Verification

- Commit hash `1a4fb49` exists in the repo (message: "update .travis.yml", dated 2014-10-17)
- It is the HEAD commit of the master branch (10 total commits in the repo)
- Repository URL is valid and accessible
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/berkshireswash`
- PR #855 body was empty

## Confidence Level

**Medium** - The commit hash is simply HEAD of the librefonts mirror repo. The librefonts repo is not the original design source. The original designer is Brian J. Bonislawsky (Astigmatic/AOETI). The repo only has VFB (proprietary FontLab) and TTX sources, making gftools-builder integration impossible without source conversion.

## Open Questions

- The original VFB source files from Astigmatic are proprietary format (FontLab Studio); conversion to UFO would be needed for gftools-builder compatibility
- The hotfix from 2017 may have used a process not reflected in the librefonts repo (which was last updated in 2014)
- Astigmatic (Brian Bonislawsky) designed many fonts for Google Fonts; it's unknown if more modern source formats are available from the designer
- The tracking notes say "No buildable source files at recorded commit" which is correct -- VFB files require proprietary software to open
- This font was added to Google Fonts in 2012 and has classification DISPLAY with SERIF stroke
