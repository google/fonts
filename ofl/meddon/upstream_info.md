# Meddon — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/vernnobile/MeddonFont |
| Commit | `157a4b58e73139e11e21ac9805282f196b8f4059` |
| Confidence | High |

## Source Types

The repository contains SFD (FontForge) sources:
- `New/Meddon.sfd` — newer version
- `Old/Meddon.sfd` — older version

## Build Compatibility

No `config.yaml` is present. The sources are SFD (FontForge SplineFont Database) format only, which is not directly compatible with gftools-builder. Building from these sources would require FontForge.

## Investigation Notes

Vernon Adams' original repository is the canonical upstream for Meddon. The binary in google/fonts was last touched on 2015-08-05 (fsType fix). The SFD sources represent the original design files.

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Vernon Adams (vernnobile) is the original designer, and this is his canonical repository.
