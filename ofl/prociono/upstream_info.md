# Prociono — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at https://github.com/theleagueof/prociono, maintained by The League of Moveable Type and containing Barry Schwartz's original UFO sources. The repository is not a fork. The METADATA.pb source block was updated accordingly.

## Designer

Barry Schwartz (chemoelectric@chemoelectric.org). The DESCRIPTION.en_us.html references both `https://bitbucket.org/sortsmill/sortsmill-fonts` and `https://www.theleagueofmoveabletype.com/prociono`. The League of Moveable Type confirmed a GitHub repository at https://github.com/theleagueof/prociono.

## Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry for theleagueof/prociono.
- **GitHub search**: The repository `https://github.com/theleagueof/prociono` was found and verified (HTTP 200).
- **Ownership**: Owned by `theleagueof`, the organization that hosts and distributes Barry Schwartz's Prociono. The readme credits "Barry Schwartz" as the designer.
- **Description**: "A roman serif with blackletter elements." (98 stars, not a fork).
- **Latest commit**: `f9d9680de6d6f0c13939f23c9dd14cd7853cf844` — "Initial commit with readme and licenses"
- **Source files**: The repository contains `source/Prociono.ufo` with full UFO source, OTF and TTF binaries.

## Notes

The Bitbucket URL referenced in DESCRIPTION.en_us.html (`https://bitbucket.org/sortsmill/sortsmill-fonts`) is a broader Sorts Mill fonts repository. The League of Moveable Type GitHub repository is the primary distribution point for Prociono and is the most widely referenced canonical source.

## Verdict

**Canonical upstream repo found.** `https://github.com/theleagueof/prociono` is the authoritative repository. METADATA.pb was updated with `repository_url` and `commit` fields.
