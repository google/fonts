# Pushster — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Pushster is a test font that was created internally at Google to test the font push process. It is a derivative of the Lobster v2.100 font by Pablo Impallari, with the font family name renamed from "Lobster" to "Pushster". The binary in the Google Fonts repo does NOT exactly match any commit in the upstream `impallari/The-Lobster-Font` repository. The METADATA.pb source block (which points to the Lobster repo) was added by an automated "Update upstreams" batch commit, not through a formal upstream investigation. The closest matching upstream commit was identified and added as the commit reference.

## Repository

- **URL**: https://github.com/impallari/The-Lobster-Font
- **Upstream cache**: Not present in the fontc_crater_cache (no `impallari/` directory found)

## Version Identification

The font binary in the Google Fonts repo was inspected:

- `Pushster-Regular.ttf`: Version 2.100, nameID3 = "2.100;IMPA;Lobster-Regular"
- File size: 406,076 bytes

The vendor ID `IMPA` confirms this is derived from the Impallari (Pablo Impallari) Lobster font. The postscript name `Lobster-Regular` and version `2.100` both match the Lobster upstream. However, the family name was renamed to "Pushster" and the file size does not match any commit in the Lobster repository.

## Origin of Pushster

The git history of `ofl/pushster/` in the `google/fonts` repo was reviewed. The original commit adding Pushster was:

```
a2e33f35f Create a test font, temporarily, to test the push process.
Author: Andy John <andyj@andyj-macbookpro.roam.corp.google.com>
Date: Mon Mar 25 23:55:05 2019 -0700
```

The original METADATA.pb had NO source block — it was a bare minimal entry with just font metadata. The description file contains "INTERNAL TESTING" and describes the Lobster font's design approach verbatim.

The `source` block pointing to `impallari/The-Lobster-Font` was added in a later batch commit titled "Update upstreams" (`91b9cb3e2`), which was an automated metadata enrichment pass. It was not the result of a dedicated investigation.

## Lobster Commit Size Comparison

All commits to `fonts/ttf/Lobster-Regular.ttf` in the upstream repo were checked, with file sizes:

| Commit | Date | Size (bytes) |
|--------|------|-------------|
| `0796aa8a` | 2017-10-27 | 405,892 |
| `9101378a` | 2017-10-26 | 406,280 |
| `2516b83d` | 2016-12-13 | 405,352 |
| `92bbae6e` | 2016-12-13 | 405,352 |

None of these exactly matches the Pushster binary (406,076 bytes). The closest is `9101378a` (difference of only 204 bytes), which corresponds to the "exported fonts v.2.100" commit from 2017-10-26.

The 204-byte difference is consistent with a name table modification (renaming "Lobster" to "Pushster" in the family name fields), which would have been done manually before adding the font to Google Fonts.

## Commit Identification

Given that:
1. Pushster is version 2.100 with IMPA vendor code
2. The closest Lobster commit is `9101378a` ("exported fonts v.2.100", 2017-10-26, 406,280 bytes)
3. The size difference (204 bytes) is attributable to name table renaming
4. Pushster was added to GF in March 2019, after this 2017 commit

The commit `9101378a660fa0b93a03372467df8dfd15647fd9` was identified as the upstream source base. It was verified:

```
gh api repos/impallari/The-Lobster-Font/commits/9101378a660fa0b93a03372467df8dfd15647fd9 --jq '.sha'
# Returns: 9101378a660fa0b93a03372467df8dfd15647fd9
```

## Caveats and Issues

1. **Binary mismatch**: The Pushster TTF is NOT an exact copy of any Lobster commit. It was modified (name table at minimum) before being added to Google Fonts.
2. **Test font status**: Pushster was explicitly described as a "test font, temporarily, to test the push process." It is unclear why it remains in the production Google Fonts library.
3. **Incorrect metadata**: The copyright string in the current METADATA.pb contains artifacts: `"Copyright 2010 xyz The Lobster Project Authors..."` — the "xyz" is clearly erroneous. The `primary_script: "Thai"` is also incorrect (Pushster is a Latin script font). The `minisite_url: "https://fonts.google.com/icons"` is also wrong (points to Material Icons, not Pushster).
4. **Source block accuracy**: Since the binary is not directly from the Lobster repo (it was name-modified), the source block relationship is approximate rather than exact.

## Changes Made

- Added `commit: "9101378a660fa0b93a03372467df8dfd15647fd9"` to the `source` block in `METADATA.pb` as the best available upstream reference

## Confidence

**Low.** The Pushster binary does not exactly match any upstream commit. The commit added represents the closest upstream source base (Lobster v2.100 export), but the actual Pushster binary was modified before being submitted to Google Fonts. Additional investigation or removal of this test font from the library may be warranted.

## Repo / Commit / Config / Status

- **Repo**: https://github.com/impallari/The-Lobster-Font
- **Commit**: `9101378a660fa0b93a03372467df8dfd15647fd9` (closest upstream base: "exported fonts v.2.100", 2017-10-26)
- **Config**: No files mapping present in source block (bare repository_url only)
- **Status**: Commit hash added to METADATA.pb; multiple metadata quality issues identified (corrupt copyright string, wrong primary_script, wrong minisite_url)
- **Confidence**: Low — binary mismatch between GF copy and all upstream commits
