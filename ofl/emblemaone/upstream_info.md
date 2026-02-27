# Investigation Report: Emblema One

- **Date investigated**: 2026-02-27
- **Status**: SFD-only sources (not gftools-builder compatible)
- **Designer**: Riccardo De Franceschi
- **Mastering**: Eben Sorkin (Sorkin Type Co)
- **METADATA.pb path**: `ofl/emblemaone/METADATA.pb`

## Source Data

| Field | Value |
|---|---|
| Repository URL | https://github.com/librefonts/emblemaone |
| Commit hash | `65d5dad63686fcfc0c7e13ba2cb3143803d96bfe` |
| Branch | `master` |
| Config YAML | none (SFD-only sources) |
| Source types | SFD, VFB |

## How URL Was Found

The upstream repository URL `https://github.com/librefonts/emblemaone` was already referenced in the tracking data (`gfonts_library_sources.json`). The URL was verified to return HTTP 200. The `librefonts` GitHub organization is a well-known archive of Google Fonts source files, created by Mikhail Kashkin (hash3g). The repository contains TTX dumps of the binary font along with the original VFB and SFD source files.

The METADATA.pb in google/fonts does not currently contain a `source { }` block -- no `repository_url` is set there.

## How Commit Hash Was Identified

The upstream repository contains only a single commit:

```
65d5dad 2014-10-17 hash3g "update .travis.yml"
```

This is the initial (and only) commit in the repository, which added all files including the TTX dumps, VFB sources, SFD source, FONTLOG.txt, OFL.txt, and the Travis CI configuration. Since there is only one commit, the hash `65d5dad63686fcfc0c7e13ba2cb3143803d96bfe` is the definitive reference.

The font was originally added to Google Fonts on 2012-01-18 (per `date_added` in METADATA.pb). The google/fonts repository itself was created with a bulk "Initial commit" on 2015-03-07 by Dave Crossland, which imported all existing fonts. The font binary (`EmblemaOne-Regular.ttf`) has never been modified since that initial import.

The TTF in google/fonts is Version 1.003 (per the name table), and the TTX dumps in the upstream repo also show Version 1.003, confirming they represent the same font version.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files are:

- `src/EmblemaOne-Regular-TTF.sfd` -- FontForge SFD format (for the TTF output)
- `src/EmblemaOne-Regular-OTF.vfb` -- FontLab VFB format (for the OTF output)
- `src/EmblemaOne-Regular.vfb` -- FontLab VFB format

These are legacy source formats. SFD is a FontForge format, and VFB is a proprietary FontLab format. Neither is compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. Therefore, no override `config.yaml` can be created.

The repository also contains TTX (XML) dumps of the compiled font tables, but these are decomposed table dumps, not a usable source format for gftools-builder.

## Verification

- **Repository URL**: Verified accessible (HTTP 200)
- **Repository status**: Clean, up to date with origin (`git status` shows clean working tree)
- **Single commit**: The repo has exactly one commit (`65d5dad`)
- **Font version match**: Both the google/fonts binary and the upstream TTX name table report Version 1.003
- **FONTLOG consistency**: The FONTLOG.txt files in google/fonts and the upstream repo are identical
- **Source format**: SFD and VFB only -- not compatible with gftools-builder
- **No config.yaml**: Correct, since gftools-builder cannot use these source formats

## Confidence

**HIGH** -- The upstream repository contains a single commit with all files. The font version (1.003) matches between the google/fonts binary and the upstream TTX data. The source formats (SFD, VFB) are definitively not gftools-builder compatible, so the "SFD-only sources" status is accurate.

## Notes

- The font was designed by Riccardo De Franceschi and mastered by Eben Sorkin at Sorkin Type Co.
- The original sources were created in FontLab (VFB) in 2010, and the TTF was mastered in January 2012.
- The `librefonts` archive repo was created in October 2014 by hash3g.
- The DESCRIPTION.en_us.html references the now-defunct Google Code (`code.google.com/p/googlefontdirectory/`) as the source location, indicating this font predates the move to GitHub.
- To make this font rebuildable with gftools-builder, someone would need to convert the SFD or VFB sources to a modern format (`.glyphs` or `.ufo`).
