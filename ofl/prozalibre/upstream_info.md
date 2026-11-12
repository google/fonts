# Proza Libre — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

A canonical upstream repository was found at https://github.com/jasperdewaard/Proza-Libre, owned by the designer Jasper de Waard (Bureau Roffa). The repository is not a mirror. The METADATA.pb source block was updated accordingly.

## Designer

Jasper de Waard (Bureau Roffa). The DESCRIPTION.en_us.html explicitly links to `https://github.com/jasperdewaard/Proza-Libre` as the contribution URL. The copyright notices in METADATA.pb list "Jasper de Waard."

## Repository Investigation

- **Checked cache**: `/mnt/shared/upstream_repos/fontc_crater_cache/` — no cached entry for jasperdewaard/Proza-Libre.
- **GitHub search**: The repository `https://github.com/jasperdewaard/Proza-Libre` was found and verified (HTTP 200).
- **Ownership**: The repository owner is `jasperdewaard`, matching the designer. It is not a fork.
- **Description**: "Proza Libre is a web font by Bureau Roffa" (73 stars).
- **Latest commit**: `45ea7bb14c2301988fbda75fc27374f63e33c19c` — "Light and LightItalic vfb files"

## Source Files

The repository contains VFB source files along with TTF outputs for the full 10-style family.

## Verdict

**Canonical upstream repo found.** `https://github.com/jasperdewaard/Proza-Libre` is the designer-owned repository. METADATA.pb was updated with `repository_url` and `commit` fields.
