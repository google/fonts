# Racing Sans One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `racingsansone/src/`

## Source Files

The `racingsansone/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): RacingSansOne-Regular-OT.vfb, RacingSansOne-Regular-TTF.vfb, RacingSansOne-Regular.vfb
- **OTF** (compiled binaries, not design sources): RacingSansOne-Regular.otf
- **Other**: RacingsSansOne-Preview.jpg

## Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

## Investigation Details

The following searches were performed:

- Searched GitHub for "racing sans one font" and "racingsansone" repositories.
- Checked the `impallari` GitHub account — Pablo Impallari has 26 public repositories, but none for Racing Sans One. The repositories present include other Impallari Type fonts (Cabin, Dosis, Dancing Script, etc.) but not Racing Sans One.
- Checked the `rfuenzalida` GitHub account (co-designer Rodrigo Fuenzalida) — found 5 repositories (`AntonFont`, `Freeman`, `Instrument_Serif`, `MondaFont`, `Outfit-Fonts`), none of which is Racing Sans One.
- Searched for repos with "RacingSansOne" in the name — found only `librefonts/racingsansone` (a librefonts mirror — skipped per policy) and `google-fonts-bower/racingsansone-bower` (a Bower packaging mirror).
- Reviewed the FONTLOG.txt, which referenced `www.impallari.com` and the impallari.com projects page, but no GitHub repository was listed.

No canonical upstream repository with font source files was found.

## Notes

- Designers: Pablo Impallari and Rodrigo Fuenzalida, with spacing/kerning by Igino Marini
- The font was developed in 2012; the FONTLOG references FontLab-era workflow
- Neither designer's GitHub account contains a Racing Sans One source repository
