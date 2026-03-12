# Palanquin Dark — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Palanquin Dark was identified as **https://github.com/VanillaandCream/Palanquin**, the same repository as the Palanquin family. This was confirmed by inspecting the repository structure, which contains a `PalanquinDark/` subdirectory alongside the `Palanquin/` directory. Both families are maintained by designer Pria Ravichandran under the VanillaandCream GitHub organization.

## Investigation

The METADATA.pb file listed the designer as Pria Ravichandran with copyright dated 2014. The Palanquin Dark description confirmed it is the "heavier display family" extending the Palanquin superfamily. A search of the VanillaandCream GitHub organization revealed only three repositories: Bandipur, Catamaran-Tamil, and Palanquin — confirming no separate PalanquinDark repository exists, and that all Palanquin Dark sources are contained within the main Palanquin repository.

The latest commit in the upstream repository was retrieved:

- **Commit**: `f912925eccf9b020425a6f0ddc2ce32fc1640695`
- **Message**: "Test docs added"
- **Date**: 2015-07-03

## Upstream Repository

- **URL**: https://github.com/VanillaandCream/Palanquin
- **Owner**: Pria Ravichandran (VanillaandCream)
- **Type**: Designer-owned canonical upstream (shared with Palanquin)
- **License**: OFL 1.1
- **Latest commit**: `f912925eccf9b020425a6f0ddc2ce32fc1640695`

## METADATA.pb Changes

A `source` block was added to METADATA.pb with the repository URL and latest commit hash.
