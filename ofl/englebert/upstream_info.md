# Englebert

**Model**: Claude Opus 5.5
**Date**: 2026-11-17

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Englebert (google/fonts at commit `2086013c4c53`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/englebert.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Englebert-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/englebert at `078d44fadf93`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts cc39c4c2c304,
under tools/table_gate.py and tools/functional_gate.py: Englebert-Regular: 3 blocking
rows; functionally equivalent Those tools, including this family's plan
`plans/englebert.json`: https://github.com/felipesanches/gf-source-modernization at
`c061ad8`.

`078d44fadf93` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The build's GSUB numbers or packs some lookups differently from the release's (fontc
  places a lookup that only a contextual lookup calls, and packs chained contextual
  rules, its own way: gfonts-ai-usage-report 22-fontc-problems, problems 12 and 13);
  every rule is the same and the text shapes identically (tools/functional_gate.py).
  Decided 2026-10-02: problems that need fontc are disclosed and fixed in fontc later.
- The release's head table states version 1.010 (0x0001028F, its fontRevision) where the
  format allows only 1.0; the build states 1.0. It is the only font Google Fonts ships
  with another value (head_version_scan.py, google/fonts cc39c4c2c).

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/englebert at 0b03ab09eab75a39c93f8fb0432459a7dca74176:
  src/Englebert-Regular-TTF.vfb, a FontLab import of version 1.000. The release is
  version 1.010: the vertical metrics and the copyright were changed on the binary in
  google/fonts (056368350, b7f6aa926; December 2024), so no source of it exists.

## Future work

Not part of what Google Fonts ships; for review in a font-update PR:
- commit `47b5c41` (after the equivalence commit): README: say what the earlier sources
  are, and list them

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/englebert"
      commit: "0b03ab09eab75a39c93f8fb0432459a7dca74176"
    }

## Previous investigation

## Investigation Report: Englebert

### Source Data

| Field              | Value |
|--------------------|-------|
| Family Name        | Englebert |
| Designer           | Astigmatic (Brian J. Bonislawsky) |
| License            | OFL |
| Date Added         | 2012-11-02 |
| Repository URL     | https://github.com/librefonts/englebert |
| Commit Hash        | `0b03ab09eab75a39c93f8fb0432459a7dca74176` |
| Branch             | master |
| Config YAML        | Override `config.yaml` in google/fonts |
| Source Types        | VFB (FontLab Studio) |
| Status             | complete |
| Confidence         | HIGH |

### How Repository URL Was Found

The repository URL `https://github.com/librefonts/englebert` was already present in the METADATA.pb source block. It was added by Simon Cozens in commit `c8a4f855` ("More upstreams (e,f)", 2024-01-14). The URL is also referenced in:

- The copyright notice in METADATA.pb: `Copyright 2012 The Englebert Project Authors (https://github.com/librefonts/englebert)`
- The DESCRIPTION.en_us.html file, which links to the same repository
- The repository is accessible on GitHub under the `librefonts` organization

The repository was created by Mikhail Kashkin (hash3g) on 2014-07-16 with the commit message "Move englebert font files to separate repository", indicating it was migrated from a larger collection into its own repo as part of the librefonts organization.

### How Commit Hash Was Identified

The commit hash `0b03ab09eab75a39c93f8fb0432459a7dca74176` was added to METADATA.pb by a prior investigation (commit `e8c781a6`, "sources info for Englebert v1.010 (PR #8688)", 2025-10-30). This hash is the HEAD of the upstream repository's `master` branch and represents the latest commit (dated 2014-10-17, "update .travis.yml").

**Verification**: The upstream repository has only 12 commits total. All commits after the initial one (`3e3caf6`, 2014-07-16) are CI/Travis configuration changes only. A diff of the `src/` directory between the initial commit and HEAD shows no source file changes (only a file mode permission change on `src/METADATA_comments.txt`). The three VFB source files have been unchanged since the repository was created.

Since the source files never changed, this commit hash is effectively equivalent to any other commit in the repository for the purpose of identifying the sources. Using HEAD (`0b03ab0`) is acceptable and correct.

### How Config YAML Was Resolved

The upstream repository has **no** `config.yaml` file. The source files are exclusively in VFB format (FontLab Studio binary):

- `src/Englebert-Regular.vfb` — Original source with contour overlaps
- `src/Englebert-Regular-TTF.vfb` — TrueType outlines with hinting adjustments
- `src/Englebert-Regular-OTF.vfb` — Merged contours and optimized for OTF

An override `config.yaml` already exists in the google/fonts family directory (`ofl/englebert/config.yaml`), added in commit `e8c781a6` (2025-10-30). It contains:

```yaml
buildVariable: false
sources:
  - src/Englebert-Regular.vfb
  - src/Englebert-Regular-TTF.vfb
  - src/Englebert-Regular-OTF.vfb
```

**Note on VFB sources**: VFB is a proprietary FontLab Studio format. While gftools-builder lists VFB as a potential input, practical support may be limited. The current font binary in google/fonts was NOT built using gftools-builder from these VFB sources. Instead, the font was originally onboarded as a pre-built binary and later hotfixed (binary patched) by Emma Marichal in PR #8688 to fix v-metrics issues (see issue #8679).

Since the `config_yaml` field is omitted from the METADATA.pb source block (as per policy, google-fonts-sources auto-detects local override config files), this is correctly configured.

### Verification

#### Repository Accessibility
- GitHub URL verified accessible: `librefonts/englebert`, default branch `master`
- Last pushed: 2014-10-17 (no activity in over 10 years)

#### Source Block in METADATA.pb
The current source block contains:
```
source {
  repository_url: "https://github.com/librefonts/englebert"
  commit: "0b03ab09eab75a39c93f8fb0432459a7dca74176"
}
```
This is correct and complete. The `config_yaml` field is intentionally omitted because an override config exists locally.

#### Font Binary History
The font binary in google/fonts has been modified three times:
1. **2015-03-07** (`90abd17b`) — Initial commit (the original v1.000 binary)
2. **2024-12-04** (`05636835`) — Hotfixed v-metrics by Emma Marichal (PR #8688)
3. **2024-12-12** (`b7f6aa92`) — Name table updated (copyright) by Emma Marichal (PR #8688)

The current binary (v1.010) was hotfixed directly, not rebuilt from the VFB sources. The original v1.000 binary predates the upstream repository (added to Google Fonts 2012-11-02, upstream repo created 2014-07-16).

#### Upstream Repository Cache
The repository is cloned at `upstream_repos/fontc_crater_cache/librefonts/englebert/` and is clean with no local modifications.

### Confidence

**HIGH** — The repository URL is confirmed through multiple sources (METADATA.pb copyright, DESCRIPTION.en_us.html, GitHub). The commit hash points to the HEAD of the upstream repo, which is appropriate since no source files changed across any commits. An override config.yaml is already in place in google/fonts. The source block is complete and correctly configured.

### Additional Notes

- The font was designed by Brian J. Bonislawsky (Astigmatic) and released in November 2012
- The upstream repository was created as part of the librefonts organization by Mikhail Kashkin, migrating fonts from a larger collection
- PR #8688 was a hotfix to address bad line spacing (v-metrics) reported in issue #8679, merged by Viviana Monsalve on 2024-12-12
- The FONTLOG.txt in the upstream repo documents all three VFB source variants and their purposes
