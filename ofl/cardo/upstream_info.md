# Cardo - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Cardo |
| **Designer** | David Perry |
| **Repository URL** | https://github.com/googlefonts/CardoFont |
| **Commit** | `b2bf876b4e251ac44b343605464dad86b336b38d` |
| **Branch** | (not set) |
| **Config YAML** | (none) |
| **Date Added** | 2011-09-07 |
| **License** | OFL |
| **Status** | missing_config |

## How URL Was Found

The repository URL `https://github.com/googlefonts/CardoFont` is recorded in METADATA.pb. It was added in commit `c8f729cbd` ("Add more upstreams (c,d)") in the google/fonts repository.

## How Commit Was Determined

The commit `b2bf876b4e251ac44b343605464dad86b336b38d` is the initial commit in the CardoFont repository, made by Marc Foley on 2017-06-09. It is titled "Converted project from old google fonts repository".

This is a special case: Cardo was originally added to Google Fonts in the initial commit of the google/fonts repository (2015-03-07), years before this upstream repo was created. The CardoFont repository was created after the fact by Marc Foley as part of a project to organize upstream sources for fonts that were already in Google Fonts.

The METADATA.pb source block only contains `repository_url` with no commit hash, branch, or config_yaml fields. The commit `b2bf876b` is the one recorded in the tracking JSON but NOT in METADATA.pb itself.

## Repository Structure

The upstream repository has 4 commits total:
1. `b2bf876` - "Converted project from old google fonts repository" - Contains SFD sources in `old/version-1.000/`
2. `8446a1f` - "converd .sfd to .glyphs" - Added Glyphs sources in `sources/`
3. `db3be82` - "updated metadata to match gf spec"
4. `fc675d7` - "fonts now compile" (HEAD) - Updated Glyphs sources

At the recorded commit (`b2bf876`), only FontForge SFD sources exist in `old/version-1.000/`. The `sources/` directory with Glyphs files was added in later commits. No compiled TTF files exist in the upstream repo at any commit.

## Config YAML Status

**No config.yaml or config.yml exists anywhere in the upstream repository** at any commit. There is also no override config.yaml in the google/fonts family directory (`google/fonts/ofl/cardo/`).

The source types are SFD (FontForge format) at the original commit, and Glyphs format at later commits. Neither is set up with a gftools-builder config.

## Verification

- **Commit exists in upstream repo**: Yes, verified (initial commit)
- **Binary match**: Cannot verify - the upstream repo does not contain compiled TTF files. The fonts in google/fonts were added from the original google/fonts initial commit (2015) or from the previous font hosting infrastructure, predating this upstream repo.
- **config.yaml present at commit**: No - no config file exists at any commit
- **Font file history in google/fonts**:
  - Initial addition: `90abd17b4` (2015-03-07, "Initial commit")
  - Last binary modification: `d70318ab8` (2015-04-27, "Updating ofl/cardo/*ttf with nbspace and fsType fixes" by Dave Crossland)

## Confidence Level

**MEDIUM** - The repository URL is verified and the commit exists. However, this is a legacy font where:
- The upstream repo was created after the font was already in Google Fonts
- The repo has no compiled fonts and no build configuration
- The fonts in google/fonts were not built from this upstream repo
- The source format (SFD, later converted to Glyphs) is not directly compatible with gftools-builder

## Open Questions

1. **Missing config.yaml**: A config.yaml would need to be created (either in the upstream repo or as an override in google/fonts) to enable gftools-builder compilation. The Glyphs sources at HEAD (`fc675d7`) might be usable but would need a config file.

2. **Correct commit**: The recorded commit `b2bf876b` is the initial import. The more useful commit for rebuilding would be the HEAD `fc675d7a` ("fonts now compile"), which has Glyphs sources. However, fonts have never actually been rebuilt from this repo.

3. **Font binary provenance**: The TTF files in google/fonts were not produced from this upstream repository. They predate the repo and come from the original font release by David Perry. The upstream repo is a preservation archive, not the actual build source.
