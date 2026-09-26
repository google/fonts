# Share Tech Mono -- Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

Design sources were found in the **googlefontdirectory-hg** archive (Google Font Directory, Mercurial-era).

- **Repository**: googlefontdirectory-hg
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sharetechmono/src/`

## Source Files

The source directory contains: 2 VFB files (FontLab, proprietary format); 4 compiled binaries (OTF/TTF, not design sources).

The VFB format is proprietary (FontLab) and cannot be built with gftools-builder. These sources are **not directly buildable** with the current open-source pipeline.

### Key source files

- `ShareTechMono-Regular.vfb` (VFB, proprietary)
- `expertset/ShareTechMonoExp-Regular.vfb` (VFB, proprietary)
- `ShareTechMono-Regular.otf` (compiled binary)
- `ShareTechMono-Regularo.ttf` (compiled binary)
- `expertset/ShareTechMonoExp-Regular.otf` (compiled binary)
- `expertset/ShareTechMonoExp-Regular.ttf` (compiled binary)

## Designer

Carrois Apostrophe

## Search Results

- Searched `ShareTechMono in:name` on GitHub: found only `librefonts/sharetechmono` and `google-fonts-bower/sharetechmono-bower`
- `librefonts/sharetechmono` skipped (mirror, not canonical source)
- Note: `m4rc1e/ShareTech` was found for the Share Tech family but does not include Mono sources
- No Carrois-maintained repository with Share Tech Mono source files was found
