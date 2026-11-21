# Gamja Flower

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Gamja Flower as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/gamjaflower.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  GamjaFlower-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/gamjaflower at `c98981a4f463`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/gamjaflower.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`c98981a4f463` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/yoondesign/yoonfont-Gamjaflower at
  c31c8953af3fc0dca946e82e5196c9dacfe7a3b3: the fonts as built (2 font files); no
  source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/yoondesign/yoonfont-Gamjaflower"
      commit: "c31c8953af3fc0dca946e82e5196c9dacfe7a3b3"
    }

## Previous investigation

## Investigation Report: Gamja Flower

### Summary

Gamja Flower is a Korean handwriting/display typeface created by YoonDesign Inc. It was onboarded to Google Fonts on March 13, 2018, as part of a batch of Korean font families in PR #1459, authored by Marc Foley. The font binaries were mastered by Aaron Bell (Saja Type Works). The upstream repository at `yoondesign/yoonfont-Gamjaflower` contains only binary font files (TTF and OTF) with no compilable source files and no config.yaml. METADATA.pb currently has no source block at all. A source block can be added referencing the upstream binary-only repo, but no config.yaml is possible since there are no compilable sources.

### Key Findings

| Field             | Value                                                           |
|-------------------|-----------------------------------------------------------------|
| Family Name       | Gamja Flower                                                    |
| Repository URL    | https://github.com/yoondesign/yoonfont-Gamjaflower              |
| Commit Hash       | c31c8953af3fc0dca946e82e5196c9dacfe7a3b3                        |
| Config Path       | N/A (no compilable sources in upstream)                         |
| Source Files      | None (only binary TTF and OTF in upstream repo)                 |
| Status            | **no_config_possible**                                          |
| Confidence        | **HIGH**                                                        |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb has **no source block**. It contains only basic metadata:
- Name: Gamja Flower
- Designer: YoonDesign Inc
- License: OFL
- Date added: 2018-02-23
- Category: HANDWRITING
- Primary script: Kore
- Subsets: korean, latin, menu

#### Onboarding Commit (google/fonts)

- **Commit**: `16680f8688ffcd467d2eb2146a9ce0343404581d`
- **Date**: 2018-03-13
- **Author**: Marc Foley (m4rc1e)
- **Message**: "korean families r01: added (#1459)"
- This was a batch commit adding approximately 20 Korean font families simultaneously
- PR #1459 body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com"

#### File History in google/fonts

The font binary has been through the following changes:
1. **`16680f868`** (2018-03-13): Original onboarding as `Gamjaflower-Regular.ttf` (lowercase 'f')
2. **`4bfc18e3a`**: File removed during case-insensitive file cleanup
3. **`1ef157d39`** (2018-03-13): Re-added as `GamjaFlower-Regular.ttf` (uppercase 'F') - case correction
4. **`76adaf1d2`** (2021-11-01): Deploy commit that temporarily removed the file (deploy/redeploy cycle)

The binary file (12,615,444 bytes) has remained unchanged since the original onboarding.

#### Upstream Repository Verification

The upstream repo `yoondesign/yoonfont-Gamjaflower` was cloned and inspected from the cache at `upstream_repos/fontc_crater_cache/yoondesign/yoonfont-Gamjaflower/`.

**Repository contents** (only files, no subdirectories besides .git):
- `Gamjaflower.otf` (3,799,416 bytes)
- `Gamjaflower.ttf` (7,422,056 bytes)
- `OFL_Yoondesign Gamjaflower.txt`
- `README.md`
- `Readme_Yoondesign_GamjaFlower.txt`

**Commit history** (9 total commits, all from Dec 2017):
1. `d6320fcf` (2017-12-13): Initial commit
2. `e686b945` (2017-12-13): Added TTF, OTF, and OFL docx files
3. `2c37ce5e` - `c31c8953` (2017-12-19): Various readme and file cleanup commits

**Latest commit**: `c31c8953af3fc0dca946e82e5196c9dacfe7a3b3` (2017-12-19) - "Update Readme_Yoondesign_GamjaFlower.txt"

The repository has had no activity since December 2017, well before the March 2018 onboarding.

#### Binary File Comparison

- **Upstream TTF**: 7,422,056 bytes (`Gamjaflower.ttf`)
- **google/fonts TTF**: 12,615,444 bytes (`GamjaFlower-Regular.ttf`)

The file sizes are significantly different (7.4 MB vs 12.6 MB), confirming that Aaron Bell remastered/processed the font binaries before they were added to Google Fonts. The google/fonts version is much larger, likely due to subsetting or hinting additions during the mastering process.

#### Font Metadata (from binary strings)

The google/fonts binary contains:
- Copyright: "Copyright (c) YoonDesign Inc. All Rights Reserved."
- Version: 3.00, build 20171102
- Vendor URL: http://www.yoonfont.co.kr

#### Source Files Assessment

The upstream repo contains **no compilable source files**:
- No .glyphs files
- No .ufo directories
- No .designspace files
- No .sfd files
- No config.yaml

The repository only contains pre-compiled binary fonts (TTF and OTF). The original design sources are not publicly available. This is consistent with YoonDesign's practice of releasing only compiled binaries for their open-source Korean fonts.

### Conclusion

A source block can be added to METADATA.pb referencing the upstream repository, but no config.yaml is possible because the repository contains only binary font files with no compilable sources. The commit hash `c31c8953` represents the HEAD of the repository at the time of onboarding (and still is HEAD, as the repo has had no activity since December 2017).

Note: The font in google/fonts was remastered by Aaron Bell from the binary TTF in the upstream repo, not compiled from design sources.

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/yoondesign/yoonfont-Gamjaflower"
  commit: "c31c8953af3fc0dca946e82e5196c9dacfe7a3b3"
  files {
    source_file: "OFL_Yoondesign Gamjaflower.txt"
    dest_file: "OFL.txt"
  }
}
```

**Status**: no_config_possible
**Confidence**: HIGH
- The upstream repo contains only binary font files; no compilable sources exist
- The google/fonts binary was remastered by Aaron Bell, not built from source
