# Investigation Report: Fjord One

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Fjord One |
| **Designer** | Viktoriya Grabowska |
| **License** | OFL |
| **Date Added** | 2011-11-02 |
| **Category** | Serif |
| **Status** | complete (SFD-only sources) |
| **Confidence** | HIGH |

## Upstream Repository

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/librefonts/fjordone |
| **Commit** | `90b0be2c47a5acd683621f38ce4f046f741abafb` |
| **Branch** | master |
| **Config** | none (SFD-only sources) |

## Source Block (current METADATA.pb)

The current METADATA.pb (in our local clone, pending merge) has:

```
source {
  repository_url: "https://github.com/librefonts/fjordone"
  commit: "90b0be2c47a5acd683621f38ce4f046f741abafb"
}
```

This was added in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25).

## Investigation Details

### Repository Verification

The upstream repository at https://github.com/librefonts/fjordone is valid and accessible. It is cached locally at `upstream_repos/fontc_crater_cache/librefonts/fjordone/`.

The repository is a **librefonts archive** repo, typical of early Google Fonts families that predate modern gftools infrastructure. It contains:

- **Source files**: `src/FjordOne-Regular-TTD.sfd` (FontForge SFD, 467 KB), `src/FjordOne-Regular.vfb` (FontLab VFB, 115 KB)
- **TTX decompositions**: Multiple `.ttx` files for both TTF and OTF binaries in the repo root
- **Metadata**: `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`
- **No config.yaml**: SFD/VFB sources are not compatible with gftools-builder
- **No pre-built binaries in repo**: The TTF/OTF are only present as TTX decompositions

### Commit Hash Verification

The repository has only a **single commit**: `90b0be2c47a5acd683621f38ce4f046f741abafb` (2014-10-17, by hash3g, "update .travis.yml"). This is the HEAD of the master branch and the only commit available.

Since the librefonts repos were created as archives of the original Google Code font directory sources, and there is only one commit, this commit represents the complete state of all archived source files. The referenced commit is the only possible choice.

### Google Fonts History

1. **Initial commit** (`90abd17b4`, 2015-03-07): Fjord One was included in the initial import of the google/fonts repository. The binary `FjordOne-Regular.ttf` (54,156 bytes) was added here.
2. **Deploy update** (`76adaf1d2`, 2021-11-01): A large deploy commit by m4rc1e that restructured the repository. This commit deleted and re-added many files including Fjord One's DESCRIPTION.en_us.html and FONTLOG.txt, but the binary font file itself was not modified -- it remains unchanged since the initial import.

The font binary has been untouched since it was first added to google/fonts. The FONTLOG records:
- Version 1.002 (2011-10-28): "Mastered Font from Fontlab VBF to TTF" by Eben Sorkin
- Version 1.001 (2010-10-27): "Completed first complete version of Fjord in Fontlab (VBF format)" by Viktoriya Grabowska

### Config.yaml Status

No config.yaml is possible for this family. The source files are:
- `FjordOne-Regular-TTD.sfd` -- FontForge SFD format
- `FjordOne-Regular.vfb` -- FontLab VFB format (binary, not directly usable)

Neither format is supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No override config.yaml can be created.

### Copyright and Attribution

The copyright in google/fonts METADATA.pb and the upstream OFL.txt both state:
> "Copyright (c) 2011, Sorkin Type Co (www.sorkintype.com) with Reserved Font Names 'Fjord' and 'Fjord One'"

The font was designed by Viktoriya Grabowska and mastered by Eben Sorkin at Sorkin Type Co.

## Conclusion

Fjord One has a source block with a verified repository URL and the only available commit hash. The upstream repo is a librefonts archive containing only SFD/VFB sources, which are not compatible with gftools-builder. No config.yaml is possible. The status is as complete as it can be for a font with SFD-only sources.
