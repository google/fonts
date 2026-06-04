# Bentham - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bentham |
| Repository URL | https://github.com/librefonts/bentham |
| Commit Hash | a89643ad524f785a73f5326e6ee901fb042fa765 |
| Config YAML | (none) |
| Status | missing_config |
| Category | SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/bentham` comes from the librefonts organization on GitHub, a collection of decompiled font repos maintained by Marc Foley. The URL was recorded in the tracking data and added to METADATA.pb in commit `9a14639f3` (on branch `sources_info_2026-02-25`, not yet merged to main).

## How the Commit Hash Was Determined

The commit hash `a89643ad524f785a73f5326e6ee901fb042fa765` is the latest (HEAD) commit in the librefonts/bentham repo, dated 2014-10-17. This was set because it is the most recent commit in the repository and corresponds to a Travis CI config update ("update .travis.yml").

**Font history in google/fonts**:
- Initial commit `90abd17b4`: Font first added to google/fonts
- `d1b545148`: "Updating ofl/bentham/*ttf with nbspace and fsType fixes"
- `4e933f27b`: "hotfix-bentham: v2.002 added" (PR #854, by Marc Foley, 2017-08-07)

The hotfix PR #854 by Marc Foley had an empty body, providing no context about the source of the updated TTFs. The librefonts repo's last commit predates the hotfix by about 3 years (2014 vs 2017).

## Config YAML Status

- **No `config.yaml`** exists in the upstream librefonts repo (not at any commit)
- **No override `config.yaml`** in `google/fonts/ofl/bentham/`
- The repo contains only **SFD sources** (`src/Bentham-TTF.sfd`) and TTX-decomposed font files
- SFD (FontForge format) is not compatible with gftools-builder
- No UFO, Glyphs, or DesignSpace sources are available

## Verification

- Commit hash `a89643a` exists in the repo (message: "update .travis.yml", dated 2014-10-17)
- It is the HEAD commit of the master branch (11 total commits in the repo)
- Repository URL is valid and accessible
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/bentham`
- PR #854 body was empty

## Confidence Level

**Medium** - The commit hash is simply HEAD of the librefonts mirror repo. The librefonts repo is not the original design source -- it was created by extracting TTX data from the compiled fonts. The original designer is Ben Weiner (ben@readingtype.org.uk). The repo only has SFD and TTX sources, making gftools-builder integration impossible without conversion work.

## Open Questions

- The font's original source files from Ben Weiner are not known to be publicly available outside this librefonts mirror
- SFD-only sources cannot be used with gftools-builder; this family would need a UFO/Glyphs conversion or an alternative build approach
- The hotfix from 2017 may have used a process not reflected in the librefonts repo (which was last updated in 2014)
- This font was added to Google Fonts in 2010, making it one of the original catalog fonts with limited source documentation
