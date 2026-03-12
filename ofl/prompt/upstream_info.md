# Prompt — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at https://github.com/cadsondemak/prompt, owned by Cadson Demak, the designer listed in METADATA.pb. The repository is not a mirror and contains source files. The METADATA.pb source block was updated accordingly.

## Designer

Cadson Demak (info@cadsondemak.com) — a Thai type foundry. The DESCRIPTION.en_us.html explicitly links to `https://github.com/cadsondemak/prompt` as the contribution URL.

## Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry for cadsondemak/prompt.
- **GitHub search**: The repository `https://github.com/cadsondemak/prompt` was found and verified (HTTP 200).
- **Ownership**: The repository owner is `cadsondemak`, matching the designer credit. It is not a fork.
- **Description**: "Prompt is a Thai + Latin formal sans serif font family with 18 styles" (51 stars).
- **Latest commit**: `18f813a4dea16a7ecc6f944053d3ce2cd4d7e824` — "The mark has been fixed. The mark of the letters Ỗ and ỗ has been fixed."

## Source Files

The repository contains the full 18-style family (9 weights × 2 axes: upright and italic).

## Verdict

**Canonical upstream repo found.** `https://github.com/cadsondemak/prompt` is the designer-owned repository. METADATA.pb was updated with `repository_url` and `commit` fields.
