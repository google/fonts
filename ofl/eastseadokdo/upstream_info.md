# East Sea Dokdo

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped East Sea Dokdo as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/eastseadokdo.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  EastSeaDokdo-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/eastseadokdo at `7826832c41f5`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/eastseadokdo.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`7826832c41f5` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release has no glyph instructions: its font program defines functions that no
  glyph calls, and its control value program sets up the rasterizer without hinting any
  glyph. These sources carry no TrueType instructions, and the build is hinted by
  ttfautohint, as for every release that has a font program: the outlines, spacing and
  layout are the release's, its rendering at small sizes under a TrueType interpreter is
  not. Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/yoondesign/Yoonfont-KoreaDokdo at
  1bc4d9ec41e5159a839e58a349fa2e88799e93bc: the fonts as built (2 font files); no
  source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/yoondesign/Yoonfont-KoreaDokdo"
      commit: "1bc4d9ec41e5159a839e58a349fa2e88799e93bc"
    }

## Previous investigation

## East Sea Dokdo

### Summary

East Sea Dokdo is a Korean and Latin handwriting/display font designed by YoonDesign Inc. The upstream repository (`yoondesign/Yoonfont-KoreaDokdo`) contains only binary font files (.ttf, .otf) -- no editable source files. The font was originally named "KoreaDokdo" and was renamed to "East Sea Dokdo" during the Google Fonts onboarding process. A config.yaml cannot be created because there are no buildable source files.

### Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | East Sea Dokdo |
| **Designer** | YoonDesign Inc |
| **License** | OFL |
| **Date Added** | 2018-03-12 |
| **Repository URL** | https://github.com/yoondesign/Yoonfont-KoreaDokdo |
| **Commit Hash** | `41594a5` (latest commit before google/fonts merge) |
| **Config YAML** | N/A (binary-only repo, no buildable sources) |
| **Status** | no_config_possible |

### Investigation Details

#### Onboarding History

East Sea Dokdo was added to Google Fonts in PR [#1459](https://github.com/google/fonts/pull/1459) ("korean families r01: added") by Marc Foley (@m4rc1e) on 2018-03-13 (commit `16680f868`). The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com". This was a batch addition of approximately 20 Korean font families.

The font was originally named "KoreaDokdo" in the upstream repo. During the onboarding process, it was renamed to "East Sea Dokdo" (the name table in the google/fonts binary still contains traces of both names: `EastSeaDokdo-Regular` and `KoreaDokdo-Regular` / `DaehanMingukDokdo-Regular`).

The font binary has not been updated since onboarding.

#### Upstream Repository

The upstream repository is [yoondesign/Yoonfont-KoreaDokdo](https://github.com/yoondesign/Yoonfont-KoreaDokdo), created on 2017-12-13. YoonDesign Inc is a Korean professional design group.

**Repository contents** (binary-only, no source files):
- `KoreaDokdo.ttf` (3,834,712 bytes) -- added in commit `50394d2` (2017-12-13), never modified
- `OFL_Yoondesign KoreaDokdo.txt` -- license file
- `README.md` -- brief description
- `Readme_Yoondesign_KoreaDokdo.txt` -- brief description
- `KoreaDokdo.otf` was present but deleted in commit `4daa805` (2018-03-18, after google/fonts merge)

**Commit timeline:**
| Hash | Date | Description |
|------|------|-------------|
| `05b13e8` | 2017-12-13 | Create README.md |
| `50394d2` | 2017-12-13 | Add files via upload (TTF, OTF, OFL.docx) |
| `71a3f66` | 2017-12-19 | Delete KoreaDokdo OFL.docx |
| `c51db01` | 2017-12-19 | Delete README.md |
| `db6fa92` | 2017-12-19 | Add files via upload (OFL.txt, Readme) |
| `8392394` | 2017-12-19 | Create README.md |
| `bd0e074` | 2017-12-19 | Delete README.md |
| **`41594a5`** | **2017-12-19** | **Create README.md** (latest before google/fonts merge) |
| `1bc4d9e` | 2017-12-19 | Update Readme_Yoondesign_KoreaDokdo.txt |
| `4daa805` | 2018-03-18 | Delete KoreaDokdo.otf (AFTER google/fonts merge) |

**Note on commit ordering**: Commits `41594a5` and `1bc4d9e` both have the date 2017-12-19 but `1bc4d9e` is a child of `41594a5`. Both predate the google/fonts merge on 2018-03-13. The most accurate reference commit is `1bc4d9e` as the last commit before the google/fonts merge.

**Corrected reference commit**: `1bc4d9e` (2017-12-19, "Update Readme_Yoondesign_KoreaDokdo.txt") -- this was the latest commit in the upstream repo before the google/fonts PR #1459 was merged.

#### Binary Comparison

The upstream TTF (`KoreaDokdo.ttf`, 3,834,712 bytes) differs from the google/fonts binary (`EastSeaDokdo-Regular.ttf`, 3,178,684 bytes). This is expected because Aaron Bell re-mastered the font for Google Fonts, which included:
- Renaming from "KoreaDokdo" to "East Sea Dokdo"
- Modifying the name table (vendor code `UKWN`)
- Likely subsetting or optimizing the font (file is ~656KB smaller)

#### Other YoonDesign Repos

YoonDesign has several font repos on GitHub, all following the same binary-only pattern:
- `yoondesign/yoonfont-Gamjaflower` -- binary only
- `yoondesign/Yoonfont-HiMelody` -- binary only
- `yoondesign/Yoonfont-Poorstory` -- binary only
- `yoondesign/Yoonfont` -- empty repo

None contain editable source files.

#### Source Availability

No source files (`.glyphs`, `.ufo`, `.designspace`, `.sfd`) exist in the upstream repository or anywhere publicly accessible. The repository only contains compiled binary fonts (.ttf, .otf). A config.yaml cannot be created because there are no buildable source files for gftools-builder.

#### Copyright and License

- Upstream OFL: "Copyright [1989-2017] Yoondesign Inc., with Reserved Font Name 'KoreaDokdo'"
- google/fonts OFL: "Copyright (c) YoonDesign Inc. All Rights Reserved."
- Designer website: http://www.yoonfont.co.kr

### Conclusion

East Sea Dokdo has an identified upstream repository (`yoondesign/Yoonfont-KoreaDokdo`), but it is a binary-only repo with no editable source files. The source block can reference the repository URL and commit hash, but no config.yaml can be provided since there are no buildable sources. The font was re-mastered by Aaron Bell during onboarding, so the google/fonts binary is a derivative of the upstream binary rather than a direct copy.

**Recommended METADATA.pb source block:**
```
source {
  repository_url: "https://github.com/yoondesign/Yoonfont-KoreaDokdo"
  commit: "1bc4d9ec41e5159a839e58a349fa2e88799e93bc"
}
```

**Status**: `missing_config` -- upstream repo exists but contains only binaries, no buildable source files, so no config.yaml is possible.
