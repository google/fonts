# Investigation Report: jsMath cmmi10

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `jsmathcmmi10/src/` |
| **Buildable** | No — no original design sources present |

The googlefontdirectory-hg monorepo (a git mirror of the original Google Code Mercurial repository) contains a `jsmathcmmi10/src/` directory with only:

- `METADATA_comments.txt` — metadata only, not a source file

No original design sources are present. The font was generated from MetaFont bitmap sources, not from standard font design files.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | jsMath cmmi10 |
| Designer           | Donald Knuth (Computer Modern) / jsMath project |
| License            | Apache 2.0 |
| Date Added         | 2010-12-20 |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/jsmathcmmi10/`
- **Files**: DESCRIPTION.en_us.html, jsMath-cmmi10.ttf, METADATA.pb
- **No source block** in METADATA.pb
- **No license text file** in directory
- **Copyright**: "Generated from MetaFont bitmap by mftrace 1.0.33, http://www.cs.uu.nl/~hanwen/mftrace/"

### Origin and Build Process

The font is based on the Computer Modern math italic font (`cmmi10`), which provides math italic glyphs for TeX/LaTeX typesetting. It was generated from MetaFont (.mf) bitmap sources using the `mftrace` tool.

The jsMath package (http://www.math.union.edu/locate/jsMath/) was a JavaScript-based mathematics rendering system that used these converted Computer Modern fonts. The font was one of the earliest Google Fonts additions (2010-12-20).

### Git History in google/fonts

The git history shows only metadata-only changes since the initial commit. No font file updates have been made.

### Related Families

This is one of six related jsMath Computer Modern families, all sharing the same MetaFont origin: jsMath cmbx10, cmex10, cmmi10, cmr10, cmsy10, cmti10.

## Conclusion

No upstream git repository exists for this font. The font was generated from MetaFont sources via mftrace, a process that does not use standard gftools-builder compatible sources. The original .mf files reside in the TeX/CTAN distribution, not in any git repository. No config.yaml can be created.

### Status: no_config_possible
### Confidence: HIGH
