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
