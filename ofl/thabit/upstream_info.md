# Thabit — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `thabit/src/`.

### Source Files

- **SFD (FontForge)**: Thabit-Bold.sfd, Thabit.sfd
- **OpenType features**: Thabit.fea
- **Other**: build.py, cour/LICENSE.txt, cour/README.txt, cour/cour.pfa, cour/courb.pfa, cour/courbi.pfa, cour/couri.pfa

Sources are in SFD format (FontForge), which is not buildable with gftools-builder.

## Investigation Details

- github.com/khaledhosny — full repo list checked (28+ repos), no Thabit
- GitHub search: "thabit arabic font" — no relevant results
- GitHub search: "arabeyes khotot" — no results
- GitHub search: "thabit arabic fixed-width font" — no results
- github.com/arabeyes-org/khotot — not found
- github.com/googlefonts/thabit — not found

The Thabit font appears to originate from the Arabeyes.org Khotot project which predates GitHub and its sources are not available in a GitHub repository with UFO or Glyphs format. No source block was added to METADATA.pb.
