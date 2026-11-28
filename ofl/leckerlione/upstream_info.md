# Investigation: Leckerli One

**Model**: Claude Opus 4.6
**Confidence**: HIGH

## Source Repository

The original design sources for Leckerli One are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `leckerlione/src/`.

### Source Files in googlefontdirectory-hg

The `src/` directory contains buildable UFO sources alongside legacy formats:

- `LeckerliOne-Regular.ufo/` -- complete UFO source with glyphs, features, kerning, and font info (buildable with gftools-builder)
- `LeckerliOne-Regular-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `LeckerliOne-Regular.vfb` -- FontLab binary source (proprietary, not buildable with gftools-builder)
- `LeckerliOne-Regular.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The UFO source includes `features.fea` (OpenType feature code), `fontinfo.plist`, `groups.plist`, `kerning.plist`, `lib.plist`, `metainfo.plist`, and a full set of glyph files (`.glif`) covering Latin letters, accented characters, numerals, punctuation, and symbols.

**The UFO source is gftools-builder compatible** and could be used to create an override config.yaml for reproducible builds.

## METADATA.pb Analysis

The METADATA.pb for Leckerli One contains no `source { }` block -- no `repository_url`, no commit hash, no config path.

## Google Fonts History

The google/fonts git history for `ofl/leckerlione/LeckerliOne-Regular.ttf` shows only:
- `90abd17b4` -- "Initial commit" (original onboarding, pre-dating gftools-packager)

## Designer Information

The designer is listed as "Gesine Todt" and the copyright references `www.gesine-todt.de`. The OFL copyright string mentions "hallo@gesine-todt.de" and a reserved font name "Leckerli". No GitHub repository URL is referenced in the font files.

The FONTLOG.txt contains basic font information but no upstream repository reference.

No upstream repository for this font was found in the upstream repo cache beyond the librefonts archive.

## Conclusion

The googlefontdirectory-hg monorepo preserves UFO sources for Leckerli One, which are gftools-builder compatible. An override config.yaml referencing `LeckerliOne-Regular.ufo` could enable reproducible builds. The font was onboarded in the initial google/fonts commit before gftools-packager was in use. The designer Gesine Todt does not appear to have a public GitHub repository for this font.
