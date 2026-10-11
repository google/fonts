# Share -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `share/src/`

## Source Files

The source directory contains: 12 VFB files (FontLab, proprietary format); 4 SFD files (FontForge format); 20 compiled binaries (OTF/TTF, not design sources).

Neither VFB (FontLab, proprietary) nor SFD (FontForge) formats are supported by gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `Share-Bold-OTF.vfb` (VFB, proprietary)
- `Share-BoldItalic-OTF.vfb` (VFB, proprietary)
- `Share-Italic-OTF.vfb` (VFB, proprietary)
- `Share-Regular-OTF.vfb` (VFB, proprietary)
- `Share-BoldExp.vfb` (VFB, proprietary)
- `Share-BoldItalicExp.vfb` (VFB, proprietary)
- `Share-ItalicExp.vfb` (VFB, proprietary)
- `Share-RegularExp.vfb` (VFB, proprietary)
- `Share-BoldItalicOSF.vfb` (VFB, proprietary)
- `Share-BoldOSF.vfb` (VFB, proprietary)
- `Share-ItalicOSF.vfb` (VFB, proprietary)
- `Share-RegularOSF.vfb` (VFB, proprietary)
- `Share-Bold-TTF.sfd` (SFD, FontForge)
- `Share-BoldItalic-TTF.sfd` (SFD, FontForge)
- `Share-Italic-TTF.sfd` (SFD, FontForge)
- `Share-Regular-TTF.sfd` (SFD, FontForge)
- `Share-Bold.otf` (compiled binary)
- `Share-BoldItalic.otf` (compiled binary)
- `Share-Italic.otf` (compiled binary)
- `Share-Regular.otf` (compiled binary)
- `Share-BoldExp.otf` (compiled binary)
- `Share-BoldExp.ttf` (compiled binary)
- `Share-BoldItalicExp.otf` (compiled binary)
- `Share-BoldItalicExp.ttf` (compiled binary)
- `Share-ItalicExp.otf` (compiled binary)
- `Share-ItalicExp.ttf` (compiled binary)
- `Share-RegularExp.otf` (compiled binary)
- `Share-RegularExp.ttf` (compiled binary)
- `Share-BoldItalicOSF.otf` (compiled binary)
- `Share-BoldItalicOSF.ttf` (compiled binary)
- `Share-BoldOSF.otf` (compiled binary)
- `Share-BoldOSF.ttf` (compiled binary)
- `Share-ItalicOSF.otf` (compiled binary)
- `Share-ItalicOSF.ttf` (compiled binary)
- `Share-RegularOSF.otf` (compiled binary)
- `Share-RegularOSF.ttf` (compiled binary)

## Designer

Carrois Apostrophe

## Search Results

- Searched `share font carrois` on GitHub: 0 relevant results
- Searched `share font user:carrois`: found only `carrois/ShareHand`
- Checked `carrois/ShareHand` contents: only OTF, PDF, and web font binaries (no sources)
- Note: `m4rc1e/ShareTech` was found for Share Tech (a separate family)
- No repository for the full Share family (4 styles) with sources was found
