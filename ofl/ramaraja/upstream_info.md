# Ramaraja — Source Metadata Investigation

**Model**: Claude Sonnet 4.6
**Date**: 2026-03-12

## Source Repository

A canonical upstream source repository was found and a source block was added to METADATA.pb.

- **Repository**: https://github.com/appajid/ramaraja
- **Commit**: `fc98f3e28ac1857afaeb80e1befa842f083f40f1`
- **Source files**: UFO source (`Ramaraja-Regular.ufo`) and SFD file (`Ramaraja-Regular.sfd`) found at the repository root

## What Was Done

- Searched GitHub for repos with "Ramaraja" in the name.
- Found `appajid/ramaraja` — maintained by Appaji Ambarisha Darbha (GitHub user `appajid`), who is the listed designer in METADATA.pb.
- Confirmed that the GitHub user `appajid` is indeed Appaji Ambarisha Darbha, as stated in their GitHub profile bio.
- Verified the repository contains `Ramaraja-Regular.ufo` (a UFO source file) and `Ramaraja-Regular.sfd` (FontForge source).
- Retrieved the latest commit SHA via the GitHub API.
- Added a `source` block to `METADATA.pb` with the repository URL and commit hash.

## Notes

- Designer: Appaji Ambarisha Darbha — confirmed match between METADATA.pb designer field and GitHub user `appajid`
- The repository description states "updating copyright and latin characters", indicating active maintenance
- The copyright in METADATA.pb references Silicon Andhra (fonts.siliconandhra.org) and Sebastian Kosch (Crimson font), as Ramaraja was based on the Crimson design extended to support Telugu
- The appajid account maintains many Telugu font repositories under the Silicon Andhra umbrella

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Upstream has both compatible sources (.ufo) and legacy `.sfd`/`.vfb` archives at the pinned commit `fc98f3e` (upstream legacy: .sfd in repo root). Added an override `config.yaml` in `ofl/ramaraja/` that references the compatible sources only (`Ramaraja-Regular.ufo`). The legacy archives are retained upstream for historical reference but are not consumed by gftools-builder. `google-fonts-sources` auto-detects the override on the next regeneration of crater's `targets.json`.
