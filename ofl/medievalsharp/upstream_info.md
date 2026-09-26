# MedievalSharp — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [wmk69/Medieval-Sharp](https://github.com/wmk69/Medieval-Sharp) |
| Commit | `ee7510b6b13854fd340e7d2e44c218780f672cd1` |
| Date | 2022-03-13 |
| Confidence | High |

## Investigation

The METADATA.pb for MedievalSharp had no source block. The upstream repository was identified as wmk69/Medieval-Sharp, by designer Wojciech Kalinowski (wmk69).

### Source Types Available

- **SFD** (FontForge): `MedievalSharp-Book.sfd`, `MedievalSharp-Bold.sfd`, `MedievalSharp-BookOblique.sfd`, `MedievalSharp-BoldOblique.sfd`
- **Binary TTF**: Matching TTF files for all four styles
- **Documentation**: `FONTLOG.txt`, PDF specimens for each style

### Buildability

SFD-only sources. The gftools-builder toolchain does not support SFD as an input format. Not directly buildable with gftools-builder.

### Notes

- The designer's repo contains an expanded 4-style family (Book, Bold, BookOblique, BoldOblique), while Google Fonts only serves the Book weight
- The repo was created in 2022, well after the font was originally added to Google Fonts (2011), and represents a newer version of the family
- The single commit `ee7510b` (2022-03-13, "Add files via upload") contains all files
- The font was originally published on Open Font Library
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `ee7510b` at wmk69/Medieval-Sharp, which is the designer's own repository with the canonical SFD sources.
