**Model**: Claude Opus 4.6

# Suranna — Upstream Source Investigation

## Summary

The canonical upstream repository for Suranna was identified at `https://github.com/appajid/suranna`, maintained by Appaji Ambarisha Darbha. The repository contained a UFO source directory (`Suranna.ufo`).

## Repository Details

- **Repository**: https://github.com/appajid/suranna
- **Owner**: appajid (Appaji Ambarisha Darbha)
- **License**: OFL
- **Source format**: UFO
- **Latest commit**: `ce1c1f150ba50e59fd9d95c114c40545c4e8fe04`
- **Commit message**: "updated copyright & version, no latin characters"
- **Default branch**: master
- **Description**: "updated copyright & version, no latin characters"

## Source Files

The repository root contained:
- `Suranna.ufo/`
- `Suranna.sfd`
- `OFL.txt`

## Confidence

**Medium-High** — The repository was owned by `appajid` (Appaji Ambarisha Darbha), a prolific Telugu font designer with many Telugu font repos on GitHub. The METADATA.pb listed the designer as "Purushoth Kumar Guttula," but the copyright in the font pointed to "Andhrapradesh Society for Knowledge Networks (fonts.siliconandhra.org)," and `appajid` is associated with SiliconAndhra Telugu font work. The repository contained a UFO source file for the Telugu typeface. The SFD file was also present but per policy, the UFO source was used as the canonical format.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/appajid/suranna` at commit `ce1c1f150ba50e59fd9d95c114c40545c4e8fe04`.
