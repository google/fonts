# Investigation: Charis SIL

## Source Data

| Field | Value |
|---|---|
| Family Name | Charis SIL |
| Designer | SIL International |
| License | OFL |
| Date Added | 2022-05-12 |
| Repository URL | https://github.com/silnrsi/font-charis |
| Commit | `258e532625d5e6c5fca8448782e710db78a6ca8a` |
| Branch | master |
| Config YAML | Override in google/fonts |
| Status | complete |

## How URL Found

The repository URL `https://github.com/silnrsi/font-charis` was already present in the METADATA.pb `source` block. The onboarding PR #4659 explicitly references this URL: "Charis SIL Version 6.101 taken from the upstream repo https://github.com/silnrsi/font-charis". The URL is verified as the official SIL International font repository.

## How Commit Determined

The commit `258e532625d5e6c5fca8448782e710db78a6ca8a` is recorded in METADATA.pb. However, there is a notable discrepancy: the fonts were taken from the **v6.101 release archive** (as indicated by the `archive_url` field in METADATA.pb pointing to `CharisSIL-6.101.zip`), but the recorded commit is **19 commits after** the v6.101 tag (`f99e75143ab2295806f547f4b5bc7dfc4d7dde94`).

The v6.101 tag commit message is "Set version to 6.101", while the recorded commit `258e53` message is "Add placeholders and glyph_data for new glyphs" -- clearly post-release development work.

The PR #4659 body actually has an empty commit reference: "at commit https://github.com/silnrsi/font-charis/commit/." (note the trailing dot with no hash). This suggests gftools-packager failed to capture the correct commit, and the commit was filled in later, possibly incorrectly.

Since the fonts were taken from the v6.101 release archive (pre-built binaries, not compiled from source), the correct reference commit should arguably be the v6.101 tag (`f99e75143ab2295806f547f4b5bc7dfc4d7dde94`). However, the current value has been accepted in the METADATA.pb, and the fonts themselves match the v6.101 release regardless.

## Config YAML Status

An override `config.yaml` exists in the google/fonts family directory at `ofl/charissil/config.yaml`. It specifies:
- `buildVariable: false`
- Sources: `source/CharisSILRoman.designspace` and `source/CharisSILItalic.designspace`

The upstream repo at the recorded commit contains UFO sources and designspace files, confirming the override config is valid for building from source.

## Verification

- **Repository URL**: Verified -- the upstream repo at `upstream_repos/fontc_crater_cache/silnrsi/font-charis` exists and is accessible.
- **Commit**: Verified as existing in the upstream repo on the master branch. However, this commit is 19 commits ahead of v6.101, while fonts were taken from the v6.101 release archive.
- **Fonts**: The METADATA.pb uses `archive_url` to pull pre-built binaries from the v6.101 release ZIP, not compiled from source at the recorded commit.
- **Override config**: Confirmed present and valid.

## Confidence Level

**High** -- The repository URL and override config are definitively correct. The commit hash has a minor discrepancy (post-release commit vs. release tag), but since the fonts were distributed via release archive and the commit is on the same branch, this does not affect the actual font files served.

## Open Questions

1. Should the commit hash be corrected to the v6.101 tag commit (`f99e75143ab2295806f547f4b5bc7dfc4d7dde94`) since the fonts were taken from that release? The current commit (`258e53`) points to post-release development work that was not used for the fonts.
