# Tenali Ramakrishna — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Tenali Ramakrishna was found at https://github.com/appajid/tenaliramakrishna, directly linked in the family's DESCRIPTION.en_us.html. The repository contained a UFO source file (TenaliRamakrishna-Regular.ufo) as well as a legacy SFD file. Tenali Ramakrishna is a Telugu typeface designed by Appaji Ambarisha Darbha, distributed by Silicon Andhra.

## Repository

- **URL**: https://github.com/appajid/tenaliramakrishna
- **Owner**: appajid (Appaji Ambarisha Darbha)
- **Default branch**: master
- **Commit used**: `444587c444ccb531e9b383b787cbdbcb424a476c`
- **Source format**: UFO (and legacy SFD)

## Source Files

The repository root contained:
- `TenaliRamakrishna-Regular.ufo` — UFO source directory
- `TenaliRamakrishna-Regular.sfd` — Legacy FontForge source (SFD)
- `OFL.txt` — License file

## Confidence

High — the repository was directly referenced in the family's description page and owned by the credited designer.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Upstream has both compatible sources (.ufo) and legacy `.sfd`/`.vfb` archives at the pinned commit `444587c` (upstream legacy: .sfd in repo root). Added an override `config.yaml` in `ofl/tenaliramakrishna/` that references the compatible sources only (`TenaliRamakrishna-Regular.ufo`). The legacy archives are retained upstream for historical reference but are not consumed by gftools-builder. `google-fonts-sources` auto-detects the override on the next regeneration of crater's `targets.json`.
