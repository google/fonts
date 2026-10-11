# Meera Inimai — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [smc/Meera](https://github.com/smc/Meera) |
| Commit | `c689e9c5a4ea7b23a8a1a7ab2af535d3cd609bdf` |
| Date | 2016-12-31 |
| Confidence | Medium |

## Investigation

The METADATA.pb for Meera Inimai had no source block. The upstream repository was identified as smc/Meera, maintained by the Swathanthra Malayalam Computing (SMC) project. Meera Inimai is a Tamil derivative of the Meera font family.

### Source Types Available

- **SFD** (FontForge): `Meera.sfd`
- **Feature files**: `features/features.fea`, `features/kerning.fea`, `features/lookups.fea`, `features/tables.fea`
- **Build system**: Custom `Makefile` with Python build scripts (`tools/build.py`)
- **Binary TTF**: `ttf/Meera.ttf`

### Buildability

SFD-only sources. The gftools-builder toolchain does not support SFD as an input format. No `config.yaml` can be created without first converting the SFD to a modern format (.ufo, .glyphs, or .designspace). Not directly buildable with gftools-builder.

### Notes

- The font name differs between Google Fonts ("Meera Inimai") and the upstream repository ("Meera")
- Confidence is medium because the copyright strings match but naming differs
- The commit `c689e9c` (2016-12-31, "Enable CI") is the latest commit in the repository

### Actions Taken

A source block was added to METADATA.pb pointing to commit `c689e9c` at smc/Meera.
