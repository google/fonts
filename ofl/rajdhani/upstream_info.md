# Rajdhani — Source Metadata Investigation

**Model**: Claude Sonnet 4.6
**Date**: 2026-03-12

## Source Repository

A canonical upstream source repository was found and a source block was added to METADATA.pb.

- **Repository**: https://github.com/itfoundry/rajdhani
- **Commit**: `86cae0e9a63279efa076915a470049dd76c044f0`
- **Source files**: UFO sources found at `masters/Rajdhani_0.ufo` and `masters/Rajdhani_1.ufo`

## What Was Done

- Searched GitHub for "rajdhani font" via the search API.
- Found `itfoundry/rajdhani` — the Indian Type Foundry's official repository for Rajdhani.
- Verified the repository description: "Rajdhani, a Devanagari + Latin family for Google Fonts."
- Confirmed presence of UFO source files in the `masters/` directory (`Rajdhani_0.ufo`, `Rajdhani_1.ufo`).
- Retrieved the latest commit SHA via the GitHub API.
- Added a `source` block to `METADATA.pb` with the repository URL and commit hash.

## Notes

- Designer: Indian Type Foundry
- The repository contains both UFO and VFB (FontLab) files for the masters
- The `itfoundry` GitHub account is the official Indian Type Foundry organization account
