**Model**: Claude Opus 4.6

## Trirong

**Designer**: Cadson Demak

### Upstream Repository

The canonical upstream repository was found at **https://github.com/cadsondemak/trirong**, maintained by Cadson Demak (GitHub: cadsondemak), a type foundry based in Thailand. The DESCRIPTION.en_us.html in the Google Fonts repo explicitly linked to this repository.

The repository contained the following structure at the investigated commit:
- `source/` — 18 Glyphs source files, one per weight per style (e.g., `Trirong-100_Thin.glyphs`, `Trirong-400_Regular.glyphs`, etc.)
- `fonts/` — compiled TTF files
- `README.md`, `BRIEF.md`, `OFL.txt`

The presence of Glyphs source files confirmed this as an eligible upstream with modern, editable sources.

### Investigated Commit

- **Repo**: https://github.com/cadsondemak/trirong
- **Branch**: master
- **Commit**: `0c1ce550d14a0a719ea49fcd6992cf5e1027dc6f`
- **Date**: 2015-11-30
- **Message**: "source and font files updated. fix nikahit and tone marks problem."

The commit hash was verified via the GitHub API (`gh api repos/cadsondemak/trirong/commits/master`).

### Status

Source block was added to `METADATA.pb` pointing to the above repository and commit.

### Notes

Cadson Demak also maintains repositories for other Thai typefaces in Google Fonts (Anuphan, Bai Jamjuree, Chakra Petch, Charm, K2D, Kanit, Kodchasan, etc.) all under the `cadsondemak` GitHub organization.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/trirong/` referencing the upstream gftools-builder-compatible source at the pinned commit `0c1ce55` (`source/Trirong-100_Thin.glyphs`, `source/Trirong-100_Thin_Ita.glyphs`, `source/Trirong-200_ExtraLight.glyphs`, `source/Trirong-200_ExtraLight_Ita.glyphs`, `source/Trirong-300_Light.glyphs`, `source/Trirong-300_Light_Ita.glyphs`, `source/Trirong-400_Regular.glyphs`, `source/Trirong-400_Regular_Ita.glyphs`, `source/Trirong-500_Medium.glyphs`, `source/Trirong-500_Medium_Ita.glyphs`, `source/Trirong-600_DemiBold.glyphs`, `source/Trirong-600_DemiBold_Ita.glyphs`, `source/Trirong-700_Bold.glyphs`, `source/Trirong-700_Bold_Ita.glyphs`, `source/Trirong-800_ExtraBold.glyphs`, `source/Trirong-800_ExtraBold_Ita.glyphs`, `source/Trirong-900_Black.glyphs`, `source/Trirong-900_Black_Ita.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
