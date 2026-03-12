# Sarpanch — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Sarpanch was identified at `itfoundry/sarpanch` on GitHub (Indian Type Foundry). The repository contained UFO master sources. A source block was added to METADATA.pb.

## Upstream Repository

- **URL**: https://github.com/itfoundry/sarpanch
- **Owner**: itfoundry (Indian Type Foundry)
- **Branch**: master
- **Commit**: `265ec8e95cad31046b4e01a553ebfbfcbeee1188`
- **Commit message**: "Compile 2.000 — Change \"FontRevision\" from \"2.201\" to \"2.000\" to align with the otf"

## Source Files Found

| File | Type | Notes |
|------|------|-------|
| `masters/Sarpanch_0.ufo` | UFO source | Light master |
| `masters/Sarpanch_1.ufo` | UFO source | Heavy master |
| `masters/Sarpanch_0.vfb` | VFB source | Legacy format |
| `masters/Sarpanch_1.vfb` | VFB source | Legacy format |

## Designer

Sarpanch was designed by the Indian Type Foundry (info@indiantypefoundry.com). The repository is hosted under the `itfoundry` GitHub organization.

## Investigation Notes

The repository was found by searching GitHub for `Sarpanch devanagari font`, which returned `itfoundry/sarpanch` as the top result, with description "Sarpanch, a Devanagari + Latin family for Google Fonts." The repository structure used a custom Python build system (`build.py`) with UFO sources as masters. Both UFO and legacy VFB files were present, but the UFO sources are the canonical format. The repository also contained a `davelab6/sarpanch` fork.

## Result

A source block was added to METADATA.pb referencing the repository URL, the latest commit hash, and the primary UFO master source.
