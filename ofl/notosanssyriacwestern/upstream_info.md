# Noto Sans Syriac Western - Upstream Source Info

**Model**: Claude Opus 5.5

## Initial state

- METADATA.pb recorded repository_url `https://github.com/notofonts/syriac`, commit `a24ba4586441a6b76df20215464898852e702078`, branch `main` and archive_url `https://github.com/notofonts/syriac/releases/download/NotoSansSyriacWestern-v3.001/NotoSansSyriacWestern-v3.001.zip`. It had no `config_yaml`, and the family directory had no override config.yaml.
- The shipped `NotoSansSyriacWestern[wght].ttf` (Version 3.001, 618 glyphs, 446 codepoints, sha256 `29d375b8...`) came from google/fonts commit 5d425ebbb ("Fix again", 2025-10-03), merged with PR #9416 on 2025-10-03.

## Actions taken

- Verified the recorded commit:
  - `a24ba45` ("Another needing alternates", 2025-10-02 16:12 +0100) was the last upstream commit before the PR #9416 merge. The next commit on any branch, `3318b31`, is dated 2026-08-10.
  - `a24ba45` rebuilt `uni0715.fina.qr` as a component of `uni0715.fina`, whose base glyph `uni0716.fina` has had alternate (bracket) layers since `4b57be2`, and it moved the dot contour of `uni0716.fina`. The shipped binary shows both changes. It has one glyph more than the v3.001 release binary, `uni0715.fina.qr.BRACKET.varAlt01`, and `uni0716.fina`, `uni0715.fina`, `uni0715.fina.qr`, `uni072A.fina` and `uni072F.fina` carry the dot change `a24ba45` made. The shipped binary's head.modified (2025-10-02 17:09:59 UTC) is later than `a24ba45` (15:12:48 UTC).
- Found the gftools-builder config `sources/config-sans-syriac-western.yaml` at `a24ba45` (sources: `NotoSansSyriacWestern.glyphs`, recipeProvider `noto`, includeSubsets GF_Latin_Core from Noto Sans). The sibling families Noto Sans Syriac and Noto Sans Syriac Eastern already reference their configs in this repo.
- Added `config_yaml: "sources/config-sans-syriac-western.yaml"` to the source block. No override config.yaml was needed.
- Built the config at `a24ba45`:
  - Python gftools builder (gftools from a local development checkout with unpublished builder fixes, fontmake 3.11.1): the `googlefonts/variable-ttf/NotoSansSyriacWestern[wght].ttf` output had the same glyph order, outlines and gvar as the shipped binary. Only the head, name, fvar and STAT tables differed: the build numbers its instance names from name ID 257, the shipped binary from 265. functional_gate passed all 7 checks: 446 codepoints exact, 2838032 shaping runs with 0 differences, 0 rendering differences. The full run stopped at the unrelated `slim-variable-ttf` step because the local `hb-subset` failed with an undefined symbol, so the googlefonts target was built directly with ninja.
  - gftools-builder3 (`e851b8b`, fontc 1.0.0): the build succeeded, and functional_gate failed. The differences were in glyphs and features merged from the Noto Sans donor, plus one mark attachment:
    - 8 donor glyphs were missing: `uni02C9` (U+02C9), `caroncommaaccent` and `commaaccentrotate`, which the shipped macron, caron and g-comma-accent letters use as components, and 5 glyphs that no text reaches.
    - `periodcentered` had a different outline, and the `aalt` and `ordn` substitutions differed.
    - On the dotted circle, U+030A and U+0741 were not attached (2 runs).
    - All 64611 Syriac word-list runs and 23260 rule runs shaped identically.
    - builder3 named the file `[wdth,wght]`, although its fvar holds only `wght`.

## Final state

- The source block records repository_url, commit `a24ba4586441a6b76df20215464898852e702078`, archive_url (unchanged), branch `main` and `config_yaml: "sources/config-sans-syriac-western.yaml"`.
- Open point: archive_url still names the v3.001 release zip (tag `NotoSansSyriacWestern-v3.001` -> `4b57be2`). Its googlefonts binary is byte-identical to the superseded binary from google/fonts commit 4416b69 (617 glyphs), not to the shipped one. It was left unchanged pending a decision.

## Earlier upstream_info.md (preserved)

Correction (2026-09-27): commit 1b6a4d32d replaced the v3.000 archive_url with the v3.001 one; it did not remove it. The family directory first appeared in google/fonts in d75fe2bbf (2025-05-06); 2023-01-06 is the `date_added` value in METADATA.pb.

### Noto Sans Syriac Western - Upstream Source Info

**Model**: Claude Opus 4.6

#### Repository

- **URL**: https://github.com/notofonts/syriac
- **Commit**: `a24ba4586441a6b76df20215464898852e702078`
- **Branch**: main
- **Config**: not specified in METADATA.pb
- **Archive**: https://github.com/notofonts/syriac/releases/download/NotoSansSyriacWestern-v3.001/NotoSansSyriacWestern-v3.001.zip

#### Summary

Noto Sans Syriac Western was sourced from the notofonts/syriac repository (shared with Noto Sans Syriac and Noto Sans Syriac Eastern). The family was published as a variable font with a `wght` axis (100-900), covering the Western Syriac script variant (Syrc) and supporting Assyrian Neo-Aramaic, Classical Syriac, Syriac, Turoyo, and Arabic written in Syriac. No `config_yaml` field was present in the METADATA.pb source block. Files were distributed via the NotoSansSyriacWestern-v3.001 release archive. The font was added to Google Fonts on 2023-01-06 and released at version 3.001.

#### Recent upstream/main activity (post-investigation)

A four-commit revision sequence by Simon Cozens on 2025-10-02/03 advanced this family to v3.001:

- **2025-10-02** - Simon Cozens, commit [`4416b69d2`](https://github.com/google/fonts/commit/4416b69d2) ("Add 3.001"): added the v3.001 binary update.
- **2025-10-02** - Simon Cozens, commit [`1b6a4d32d`](https://github.com/google/fonts/commit/1b6a4d32d) ("Update metadata"): advanced `commit` (`0be4b71c...` -> `4b57be25d...`) and removed the v3.000 `archive_url`.
- **2025-10-03** - Simon Cozens, commit [`5d425ebbb`](https://github.com/google/fonts/commit/5d425ebbb) ("Fix again"): another binary update.
- **2025-10-03** - Simon Cozens, commit [`aa728a5ea`](https://github.com/google/fonts/commit/aa728a5ea) ("Update SHA"): advanced `commit` again (`4b57be25d...` -> `a24ba4586...`), the final state of the source block at HEAD.

The final recorded commit `a24ba4586441a6b76df20215464898852e702078` is what HEAD reflects today.
