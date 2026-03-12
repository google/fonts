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
