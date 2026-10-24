**Model**: Claude Opus 4.6

# Suravaram — Upstream Source Investigation

## Summary

The canonical upstream repository for Suravaram was identified at `https://github.com/appajid/suravaram`, maintained by Appaji Ambarisha Darbha. The repository contained a UFO source directory (`Suravaram.ufo`).

## Repository Details

- **Repository**: https://github.com/appajid/suravaram
- **Owner**: appajid (Appaji Ambarisha Darbha)
- **License**: OFL
- **Source format**: UFO
- **Latest commit**: `c8d4e86f6a287199182d1ce6c97450307388dc23`
- **Commit message**: "updated copyright & version, no latin characters"
- **Default branch**: master
- **Description**: "updated copyright & version, no latin characters"

## Source Files

The repository root contained:
- `Suravaram.ufo/`
- `Suravaram.sfd`
- `OFL.txt`

## Confidence

**Medium-High** — The repository was owned by `appajid` (Appaji Ambarisha Darbha), a prolific Telugu font designer with many Telugu font repos on GitHub. The METADATA.pb listed the designer as "Purushoth Kumar Guttula," but the copyright in the font pointed to "Silicon Andhra (fonts.siliconandhra.org)," and `appajid` is associated with SiliconAndhra Telugu font work. The repository contained a UFO source file for the Telugu typeface. The SFD file was also present but per policy, the UFO source was used as the canonical format.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/appajid/suravaram` at commit `c8d4e86f6a287199182d1ce6c97450307388dc23`.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Upstream has both compatible sources (.ufo) and legacy `.sfd`/`.vfb` archives at the pinned commit `c8d4e86` (upstream legacy: .sfd in repo root). Added an override `config.yaml` in `ofl/suravaram/` that references the compatible sources only (`Suravaram.ufo`). The legacy archives are retained upstream for historical reference but are not consumed by gftools-builder. `google-fonts-sources` auto-detects the override on the next regeneration of crater's `targets.json`.
