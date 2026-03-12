# Pattaya — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Pattaya was identified as **https://github.com/cadsondemak/pattaya**, maintained by the designer Cadson Demak (a type foundry in Thailand). This was confirmed by the DESCRIPTION.en_us.html in the google/fonts repository, which explicitly links to this repository. The repository is designer-owned and not a librefonts mirror.

## Investigation

The METADATA.pb listed the designer as Cadson Demak with copyright noting contributions from Cadson Demak, Pablo Impallari (Lobster), and Alexei Vanyashin (Cyreal).

The DESCRIPTION.en_us.html explicitly linked to `https://github.com/cadsondemak/pattaya` as the contribution URL. Web search confirmed this is the canonical Cadson Demak organization's own GitHub repository, consistent with their other font repositories (cadsondemak/kanit, cadsondemak/Krub, cadsondemak/Kodchasan, etc.).

The latest commit in the upstream repository was retrieved:

- **Commit**: `fec6c7a0c8b84949dcb2a1c6dbe1ec4ba12ca0d9`
- **Message**: "Rename project to Pattaya (Fixes #3)"
- **Date**: 2016-05-31

## Upstream Repository

- **URL**: https://github.com/cadsondemak/pattaya
- **Owner**: Cadson Demak
- **Type**: Designer-owned canonical upstream
- **License**: OFL 1.1
- **Latest commit**: `fec6c7a0c8b84949dcb2a1c6dbe1ec4ba12ca0d9`

## METADATA.pb Changes

A `source` block was added to METADATA.pb with the repository URL and latest commit hash.
