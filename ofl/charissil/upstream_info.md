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

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`258e5326`](https://github.com/silnrsi/font-charis/commit/258e5326) to [`f99e7514`](https://github.com/silnrsi/font-charis/commit/f99e7514), the [v6.101 tag](https://github.com/silnrsi/font-charis/tree/v6.101). This settles the open question above. Google Fonts ships the v6.101 release zip: [google/fonts#4659](https://github.com/google/fonts/pull/4659) ([google/fonts `dfad63d0`](https://github.com/google/fonts/commit/dfad63d0)) recorded the `archive_url` but an empty commit, and the 2025 back-fill ([google/fonts `58502310`](https://github.com/google/fonts/commit/58502310)) then recorded `258e5326`, a development commit 19 commits after the tag.

All four shipped TTFs are md5-identical to the files in `CharisSIL-6.101.zip`: Regular `614843207b892092d21fd22c7d5c090c`, Italic `d4e4d168cab27dfd920680e9b66bcad8`, Bold `05f8f051aa88782c7bff8c1cfa408bee`, BoldItalic `49c9cd820367ede68bf8f79a15ba8482`. SIL keeps the same four files in `references/v6101/`. The release was published from tag v6.101, which is `f99e7514` ("Set version to 6.101", on `master`). The binaries come from SIL's smith pipeline, so no file committed at the tag is byte-comparable; the tag is the release's source.

The override `config.yaml` resolves at `f99e7514`; `branch` and `archive_url` are unchanged.
