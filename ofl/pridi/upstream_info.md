# Pridi — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at https://github.com/cadsondemak/pridi, owned by Cadson Demak, the designer listed in METADATA.pb. The repository is not a mirror and contains UFO source files. The METADATA.pb source block was updated accordingly.

## Designer

Cadson Demak (info@cadsondemak.com) — a Thai type foundry. The DESCRIPTION.en_us.html explicitly links to `https://github.com/cadsondemak/pridi` as the contribution URL.

## Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry for cadsondemak/pridi.
- **GitHub search**: The repository `https://github.com/cadsondemak/pridi` was found and verified (HTTP 200).
- **Ownership**: The repository owner is `cadsondemak`, matching the designer credit. It is not a fork.
- **Description**: "Pridi is a informal serif Latin + looped Thai font" (15 stars).
- **Latest commit**: `fe54fb681271c79ffd55ea9045145c9d1da8ade1` — "source and font files updated. fix problem nikahit and tone marks."

## Source Files

The repository contains UFO source files along with TTF/OTF outputs.

## Verdict

**Canonical upstream repo found.** `https://github.com/cadsondemak/pridi` is the designer-owned repository. METADATA.pb was updated with `repository_url` and `commit` fields.
