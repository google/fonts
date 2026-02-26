# Belgrano - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Belgrano |
| Repository URL | https://github.com/librefonts/belgrano |
| Commit Hash | 9637660aa35d5ad59241a400f78d31413475bb77 |
| Config YAML | null |
| Status | missing_config |
| Category | SERIF |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/belgrano` was previously identified and added to the tracking data. The librefonts organization on GitHub hosts many font projects that were originally migrated for the Google Fonts ecosystem. The METADATA.pb file does not currently contain a `source {}` block (has_source_block: false), and the URL was added to the tracking file as part of a batch update (commit `9a14639f3`).

## How the Commit Hash Was Determined

The commit hash `9637660aa35d5ad59241a400f78d31413475bb77` is the only commit in the upstream repository, dated 2014-10-17. The commit message is "update .travis.yml". Since the repository has a single commit, this is trivially the correct (and only possible) commit to reference.

The font was originally added to google/fonts in the initial commit (`90abd17b4`) and later updated in PR #851 ("hotfix-belgrano: v1.003 added", by Marc Foley, 2017-08-07). The most recent TTF modification was in commit `162b8ed63`. The upstream repo contains the source files (SFD format) that were used to produce the binary.

## Config YAML Status

**No config.yaml exists** in the upstream repository, at any commit. The repo structure at the recorded commit is:

```
.travis.yml
Belgrano-Regular.ttf.*.ttx (multiple TTX files)
DESCRIPTION.en_us.html
METADATA.json
OFL.txt
src/
  Belgrano-Regular-OTF.vfb
  Belgrano-Regular-TTF.sfd
  Belgrano-Regular.otf.*.ttx (multiple TTX files)
  METADATA_comments.txt
  VERSIONS.txt
```

The source files are in SFD (FontForge) and VFB (FontLab) formats, which are not compatible with gftools-builder. A config.yaml cannot be meaningfully created for this project without converting the sources to a modern format (.glyphs, .ufo, or .designspace).

## Verification

- Commit hash `9637660` exists in the upstream repo (the only commit)
- The repo contains SFD-only sources, confirming the `missing_config` status and `source_types: ["sfd"]` annotation
- No override config.yaml exists in the google/fonts family directory
- The METADATA.pb does not have a `source {}` block

## Confidence Level

**High** - The commit hash is trivially correct as the only commit in the repository. The `missing_config` status is correct because the sources are in legacy formats (SFD/VFB) that cannot be used with gftools-builder.

## Open Questions

- The METADATA.pb currently has no `source {}` block. A source block with `repository_url` and `commit` should be added, even without `config_yaml`, to document the upstream origin.
- The font was added to Google Fonts in 2011 and last updated in 2017 (PR #851). The upstream repo appears abandoned with only one commit from 2014.
