# Investigation Report: Black Han Sans

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Black Han Sans |
| Designer | Zess Type |
| License | OFL |
| Date Added | 2018-02-23 |
| Repository URL | https://github.com/zesstype/Black-Han-Sans |
| Commit | `8809d5944fbf6aa2cd99158cb7ab55629058348a` |
| Branch | None |
| Config YAML | None |
| Status | missing_config |

## How URL Found

The repository URL was added to METADATA.pb by Emma Marichal (commit `9bb786b0e`, 2024-11-28) with the message "adds family.source.repository_url entry". The URL also appears in the copyright string: "Copyright 2015 The Black Han Sans Project Authors (https://github.com/zesstype/Black-Han-Sans)".

## How Commit Determined

The commit hash `8809d5944fbf6aa2cd99158cb7ab55629058348a` was added as part of a batch operation (commit `9a14639f3`, 2026-02-25). This is the HEAD commit of the upstream repository's master branch, representing the latest state of the repo.

### Cross-verification

The commit was verified in the upstream repo at `upstream_repos/fontc_crater_cache/zesstype/Black-Han-Sans/`. It corresponds to "Update README.md" (dated 2020-09-03).

However, this is a **binary-only** repository. At the recorded commit, the repo contains only:
- `BlackHanSans.ttf` - the font binary
- `OFL.txt` - the license
- `README.md` - readme
- A Korean-named OTF file (the same font in OTF format)

There are no source files (no `.glyphs`, `.ufo`, `.designspace`, `.sfd` files) anywhere in the repo's history.

### Relationship to google/fonts binary

The font in google/fonts has been modified multiple times after the initial Korean batch import:
1. **2018-03-13**: Initial add as part of Korean families batch (PR #1459, by Marc Foley)
2. **2024-11-25**: "Black Han Sans: 1.001" - hotfix by Aaron to correct a cmap encoding bug
3. **2024-11-27**: Two additional hotfixes by Aaron (adding BA87 glyph, updating copyright)
4. **2024-11-28**: Final copyright hotfix by Emma Marichal

The font binary currently in google/fonts is NOT from the upstream repo - it was hotfixed directly by Aaron Bell and Emma Marichal. The upstream repo was last updated in 2020 and has not been synced with these hotfixes.

## Config YAML Status

No `config.yaml` exists in the upstream repository at any commit. The repo contains only pre-built binaries with no source files. Therefore, no config.yaml can be created for this family.

There is also no override `config.yaml` in the google/fonts family directory.

## Verification

- **Upstream repo accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/zesstype/Black-Han-Sans/`
- **Commit exists in repo**: Yes - `8809d59 Update README.md` (HEAD of master, dated 2020-09-03)
- **Font file at commit**: Yes - `BlackHanSans.ttf` exists
- **Source files at commit**: No - repository contains only pre-built binaries
- **Config YAML**: Not applicable - no source files to build from

## Confidence Level

**MEDIUM** - The commit hash is the HEAD of the upstream repo, which is the best available reference. However, the font binary in google/fonts has diverged significantly from the upstream version due to multiple hotfixes applied directly in google/fonts. The upstream repo is effectively a binary distribution point, not a true source repository.

## Open Questions

1. Where are the actual source files for Black Han Sans? The upstream repo only contains compiled binaries.
2. Should the commit hash reference the original import state, or is HEAD the correct choice given the binary-only nature of the repo?
3. The hotfixed binary in google/fonts was created by Aaron Bell directly - are there source files in Saja Type Works' private workspace?

## Notes

- Black Han Sans was part of the same Korean fonts batch as Black And White Picture (PR #1459, March 2018).
- The upstream repo (zesstype/Black-Han-Sans) is a very simple repo with only 19 commits total, all simple file uploads and README edits.
- The font was hotfixed in google/fonts in November 2024 to fix cmap encoding issues and copyright strings. These changes are not reflected in the upstream repo.
- The status is correctly `missing_config` because no buildable source files exist in the upstream repo. This cannot be resolved without obtaining source files from the designer (Zess Type).
- The `source {}` block in METADATA.pb currently only contains `repository_url` and `commit` (added by our batch update), with no `config_yaml` field, which is correct.
