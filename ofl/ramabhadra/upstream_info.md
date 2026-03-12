# Ramabhadra — Source Metadata Investigation

**Model**: Claude Sonnet 4.6
**Date**: 2026-03-12

## Source Repository

A source repository was found and a source block was added to METADATA.pb.

- **Repository**: https://github.com/appajid/ramabhadra
- **Commit**: `09579428d71598b6d3148aebe5505df573cc1b30`
- **Source files**: UFO source (`Ramabhadra.ufo`) and SFD file (`Ramabhadra.sfd`) found at the repository root

## What Was Done

- Searched GitHub for repos with "Ramabhadra" in the name.
- Found `appajid/ramabhadra` — maintained by Appaji Ambarisha Darbha (GitHub user `appajid`), who is a Telugu font designer associated with the Silicon Andhra project.
- Verified the repository contains `Ramabhadra.ufo` (a UFO source file) and `Ramabhadra.sfd` (FontForge source).
- Retrieved the latest commit SHA via the GitHub API.
- Added a `source` block to `METADATA.pb` with the repository URL and commit hash.

## Notes

- The METADATA.pb lists the designer as "Purushoth Kumar Guttula", while the copyright mentions "Andhra Pradesh Society for Knowledge Networks (fonts.siliconandhra.org)"
- The GitHub repository is maintained by `appajid` (Appaji Ambarisha Darbha), who maintains many Telugu fonts under the Silicon Andhra umbrella — this is consistent with the organization copyright
- The repository description states "Updating TTF SFD Copyright and version", indicating active maintenance
- The repo contains a UFO source file, making it suitable as an upstream source
