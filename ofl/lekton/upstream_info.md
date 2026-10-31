# Investigation: Lekton

**Model**: Claude Opus 4.6
**Confidence**: MEDIUM

## Source Repository

The original design sources for Lekton are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `lekton/src/`.

### Source Files in googlefontdirectory-hg

- `Lekton-Regular-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Lekton-Bold-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Lekton-Italic-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Lekton034.otf` -- compiled OTF binary, not a design source
- `LektonBold034.otf` -- compiled OTF binary, not a design source
- `LektonItalic004.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are SFD (FontForge) format only. No `.glyphs`, `.ufo`, or `.designspace` files are present. SFD files are not compatible with gftools-builder. The `.otf` files are compiled binaries, not design sources.

## METADATA.pb Analysis

The METADATA.pb for Lekton contains no `source { }` block -- no `repository_url`, no commit hash, no config path.

## Google Fonts History

The google/fonts git history for `ofl/lekton/Lekton-Regular.ttf` shows only:
- `90abd17b4` -- "Initial commit" (original onboarding, pre-dating gftools-packager)

## Designer Information

The designer is listed as "ISIA Urbino" (Istituto Superiore per le Industrie Artistiche, Urbino -- an Italian design school). The OFL copyright states: `Copyright (c) 2008, 2009, 2010, Accademia di Belle Arti di Urbino (luciano.perondi@isiaurbino.net)`. The font is attributed to the academic institution rather than an individual designer.

No upstream repository for this font was found in the upstream repo cache.

## Conclusion

The googlefontdirectory-hg monorepo preserves SFD sources for all three styles of Lekton (Regular, Bold, Italic), but SFD is a legacy format not compatible with gftools-builder. No config.yaml can be created without first converting sources to a supported format. Lekton was created by ISIA Urbino (an Italian design institution) and was part of the initial google/fonts batch before source tracking was in place. Finding a modern upstream repository would require contacting the institution.
