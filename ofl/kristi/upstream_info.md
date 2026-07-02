# Investigation: Kristi

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `kristi/src/` |
| **Buildable** | No — legacy format only (.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

### Source files (2)

| File | Format | Notes |
|------|--------|-------|
| `Kristi.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains a single FontForge SFD file, which is an original design source but is not compatible with the gftools-builder pipeline.

## Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) and subsequently updated in `1ac6f76ab` ("hotfix-kristi: v1.004 added (#902)", May 8, 2017).

The copyright notice reads: "Copyright (c) 2010, Birgit Pulk (birgitpulk@gmail.com). All rights reserved. Licenced under SIL OFL v1.1"

The DESCRIPTION.en_us.html describes it as "a calligraphy font inspired by old chancery typefaces" designed by Birgit Pulk, a graphic designer from Estonia.

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/kristi` containing only TTX dumps of the binary font. The googlefontdirectory-hg monorepo preserves the more useful SFD design source that the librefonts mirror did not retain.

No upstream GitHub repository for Birgit Pulk was found.

## Conclusion

The googlefontdirectory-hg monorepo contains the original design source in FontForge SFD format, but this is not buildable with gftools-builder. The librefonts mirror only preserved TTX dumps. No upstream GitHub repository is known for this family.
