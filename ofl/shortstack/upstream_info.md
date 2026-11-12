# Short Stack -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `shortstack/src/`

## Source Files

The source directory contains: 1 VFB file (FontLab, proprietary format); 1 SFD file (FontForge format); 1 compiled binary (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `ShortStack-Regular.vfb` (VFB, proprietary)
- `ShortStack-Regular-TTF.sfd` (SFD, FontForge)
- `ShortStack-Regular.otf` (compiled binary)

## Designer

James Grieshaber

## Search Results

- Searched `short stack font sorkin` on GitHub: 0 results
- Searched `shortstack font` on GitHub: 0 results
- Searched `short stack font grieshaber` on GitHub: 0 results
- No Sorkin Type Co or James Grieshaber GitHub presence found with Short Stack sources
