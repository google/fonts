# Modern Antiqua — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [wmk69/Modern-Antiqua](https://github.com/wmk69/Modern-Antiqua) |
| Commit | `f88d41ebebb9614874068d3142b6af52b707e917` |
| Date | 2022-03-13 |
| Confidence | High |

## Investigation

The METADATA.pb for Modern Antiqua had no source block. The upstream repository was identified as wmk69/Modern-Antiqua, by designer Wojciech Kalinowski (wmk69).

### Source Types Available

- **SFD** (FontForge): `ModernAntiqua-Book.sfd`, `ModernAntiqua-Bold.sfd`, `ModernAntiqua-BookOblique.sfd`, `ModernAntiqua-BoldOblique.sfd`
- **Binary TTF**: Matching TTF files for all four styles
- **Documentation**: `FONTLOG.txt`, PDF specimens for each style

### Buildability

SFD-only sources. The gftools-builder toolchain does not support SFD as an input format. Not directly buildable with gftools-builder.

### Notes

- The designer's repo contains an expanded 4-style family (Book, Bold, BookOblique, BoldOblique), while Google Fonts only serves the Book weight
- The repo was created in 2022, well after the font was originally added to Google Fonts (2011), and represents a newer version of the family
- The single commit `f88d41e` (2022-03-13, "Add files via upload") contains all files
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `f88d41e` at wmk69/Modern-Antiqua, which is the designer's own repository with the canonical SFD sources.
