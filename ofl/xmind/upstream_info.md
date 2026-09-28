# Xmind

Investigated 2026-09-28 by an AI agent (Claude Opus 5.5).

## Initial state

- METADATA.pb had a source block with `repository_url` https://github.com/lamzhonghang/xmind, `commit` b2e4ee3f61453fefe11c694028ccdb472c994e83, `branch` main and three file mappings (OFL.txt, fonts/variable/Xmind[wght].ttf, fonts/variable/Xmind-Italic[wght].ttf), but no `config_yaml`. The family directory had no override config.yaml and no upstream_info.md.
- Version 1.001 was onboarded by PR #10956 (merged 2026-09-23). Its gftools-packager commit 24ad9cf9250a named https://github.com/lamzhonghang/nevermind at commit b2e4ee3; the upstream repository was renamed to xmind during review, and commit 2ff00cfb36 updated `repository_url`. Commits 74c05e0f44, 754463c578 and 79b80491c6 then changed the copyright URL from https://github.com/xmindltd/xmind (which returns 404) to https://github.com/lamzhonghang/xmind in METADATA.pb, OFL.txt and name ID 0 of both fonts.

## Actions taken

- The recorded commit was verified. b2e4ee3 (2026-09-03, "Merge pull request #4 from emmamarichal/main") is the head of `main` in the live repository and in the archived mirrors of lamzhonghang/xmind and lamzhonghang/nevermind; no later upstream commit exists. The onboarded fonts (google/fonts 24ad9cf9250a) are byte-identical to fonts/variable/ at b2e4ee3 (blobs 26ca113 and bea5df7), and so was OFL.txt. Their head.modified is 2026-09-02 15:29:09 UTC, 30 seconds before the upstream commit f43789f that added them. The fonts now in google/fonts differ from them only by the name ID 0 hotfix.
- sources/config.yaml was found at b2e4ee3: a gftools-builder config with `sources: [Xmind.glyphs]` (Glyphs 3 format), `splitItalic: true` and an explicit STAT table.
- The config was build-tested at b2e4ee3:
  - gftools-builder3 (main e851b8b, fontc 1.0.0) stopped with `Invalid tag 'XMIND': Invalid length (5)`. Xmind.glyphs sets a five-character vendorID, XMIND. fontc rejects it, while fontmake truncates it to XMIN, the OS/2 vendor ID of the shipped fonts. A scratch copy with the vendorID patched to XMIN then compiled, but builder3 wrote the same combined wght+ital font under both file names, because it does not implement `splitItalic`.
  - The Python builder (`gftools builder`) with glyphsLib 6.14.0, fontTools 4.61.1, fontmake 3.12.1, ufo2ft 3.9.0 and gftools 0.9.999 rebuilt both variable fonts byte-identical to the onboarded fonts, except for the head checksum and modification date.
  - With the current PyPI toolchain (gftools 0.10.0, fontmake 3.12.1, glyphsLib 6.15.0, ufo2ft 3.9.0, fontTools 4.66.0), both fonts passed the functional gate (cmap, shaping over about 3.0 million runs, rendering, names, line spacing, advances, GDEF). Apart from name ID 0 (see Final state), the glyph set, cmap, outlines, metrics, GPOS, GDEF, STAT and fvar were identical to the shipped fonts. Two chain-context GSUB lookups were packed into one subtable instead of two, and one all-zero gvar tuple of the italic uni0422 was dropped; the same happened with fontTools 4.64.0 and not with 4.61.1, so both follow from the fontTools version. Neither changed shaping or rendering.
  - glyphsLib 6.12.7 built an Italic with 33 changed outlines, backslanted glyphs such as Cyrillic I, parenright and less, and the functional gate failed on rendering. The italic masters use mirrored components with a Glyphs 3 `slant` transform, which glyphsLib supports only since 6.14.0 (released 2026-08-01).
- `config_yaml: "sources/config.yaml"` was added to the source block of METADATA.pb. No other field was changed.

## Final state

The source block records repository_url https://github.com/lamzhonghang/xmind, commit b2e4ee3f61453fefe11c694028ccdb472c994e83, branch main, the three file mappings and `config_yaml: "sources/config.yaml"`. With the Python builder and glyphsLib 6.14.0 or later, the upstream config builds Xmind[wght].ttf and Xmind-Italic[wght].ttf functionally equivalent to the shipped fonts, and byte-identical to the onboarded fonts with fontTools 4.61.1. Until upstream adopts the hotfix, name ID 0 of a rebuilt font carries https://github.com/xmindltd/xmind. The fontc build (gftools-builder3) is still blocked by the five-character vendorID, and builder3 does not support `splitItalic`.

## Related repositories

- https://github.com/lamzhonghang/nevermind: the same repository under its name before the rename (GitHub now redirects it to lamzhonghang/Xmind). The gftools-packager commit message cites this URL. Its archived mirror holds the same refs as lamzhonghang/xmind: 33 commits on `main` (2025-05-09 to 2026-09-03, head b2e4ee3), plus pull/1, pull/2 and pull/4 heads.
- https://github.com/xmindltd/nevermind: Xmind Ltd's earlier NeverMind brand-font repository, OFL-licensed. It has 137 commits on `master` by edman, Edmanchen and Edman Chen (2020-01-03 to 2023-07-21, head 95cf07751b088a82f60d398dec61b2aaf98f9f52). It contains 374 TTF binaries of NeverMind styles, PNG specimens, README and LICENSE, and no editable sources. It shares no git object with lamzhonghang/xmind. Until 2026-09-02 (upstream commits 1c0b7de and f43789f), the copyright string in OFL.txt and in the upstream sources pointed to this repository. It is not an onboarding source and is recorded here for provenance.

## Earlier upstream_info.md

None. ofl/xmind/ had no upstream_info.md before this change.
