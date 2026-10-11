# Sofia -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sofia/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 1 compiled binary (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Sofia-Regular-OTF.vfb` (VFB, proprietary)
- `Sofia-Regular.otf` (compiled binary)

## Research

Sofia was designed by Paula Nazal and Daniel Hernández for LatinoType Limitada
(info@latinotype.com). The font was released in 2011. Searches on GitHub and
the web did not reveal any repository maintained by LatinoType or the
individual designers that contained open source files in UFO, Glyphs, or
other editable formats.

A separate unrelated typeface called "Sofia Sans" exists on GitHub at
`lettersoup/Sofia-Sans`, but this is a different typeface and not related to
the LatinoType Sofia font on Google Fonts.


## Notes

The designer listed in METADATA.pb is LatinoType. The font is described as
an upright script font with unconventional ligatures. LatinoType is a Chilean
type foundry founded by Paula Nazal Selaive and Daniel Hernández Zamora.
