# Miltonian — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [impallari/Miltonian](https://github.com/impallari/Miltonian) |
| Commit | `95d180e8744380f93a8437226e58032d484882c7` |
| Date | 2016-01-15 |
| Confidence | High |

## Investigation

The METADATA.pb for Miltonian had no source block. The upstream repository was identified as impallari/Miltonian, by designer Pablo Impallari. The repository contains sources for both Miltonian and Miltonian Tattoo.

### Source Types Available

- **VFB** (FontLab): `source/Miltonian-Regular.vfb`, `source/Miltonian-Regular-OTF.vfb`, `source/Miltonian-Regular-TTF.vfb`
- **SFD**: Referenced in earlier investigations but VFB is the canonical format
- **Binary fonts**: `fonts/TTF/Miltonian-Regular-TTF.ttf`, `fonts/OTF/Miltonian-Regular.otf`
- **Documentation**: `FONTLOG.txt`, `README.md`

### Buildability

VFB-only editable sources (FontLab Studio proprietary format). No `.glyphs`, `.ufo`, or `.designspace` files are present. Not directly buildable with gftools-builder.

### Notes

- The repository covers both Miltonian and Miltonian Tattoo families
- Co-designer credit: Igino Marini (ikern.com) for kerning
- The designer Pablo Impallari passed away in 2021; the repo is unlikely to receive further updates
- Commit `95d180e` (2016-01-15, "v1.7") is the latest content commit, matching the google/fonts update (2016-01-25)
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `95d180e` at impallari/Miltonian.
