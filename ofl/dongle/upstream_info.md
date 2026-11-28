# Dongle

**Model**: Claude Opus 5.5
**Date**: 2026-11-17

Sources modernized 2026-11: the sources the designer published do not rebuild the fonts
Google Fonts ships (listed under "Earlier sources"), so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Dongle (google/fonts at commit `2eb0b48d5f76`). The designer's
published sources ("Earlier sources") do not rebuild those fonts, so the family could
not be built from them with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/dongle.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from Dongle-{Bold,Light,Regular}.ttf, the fonts
  Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/dongle at `d424e1283eec`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts cc39c4c2c304 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF, hinting), 3 styles. Those
tools, including this family's plan `plans/dongle.json`:
https://github.com/felipesanches/gf-source-modernization at `c061ad8`.

`d424e1283eec` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/yangheeryu/Dongle at f7127c4d2450e1cad20254ec692591347e2fc260, the
  designer's repository: sources/Dongle.zip holds Dongle.glyphs (113 MB). It maps U+2225
  to two glyphs, which fontmake rejects, and built with gftools-builder it is far from
  the release (logs/crater-skipped-2026-11-16), so the fonts as shipped are the source
  of record here.

## Future work

Not part of what Google Fonts ships; for review in a font-update PR:
- commit `cbd9f5b` (after the equivalence commit): README: say what the earlier sources
  are, and list them

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/yangheeryu/Dongle"
      commit: "f7127c4d2450e1cad20254ec692591347e2fc260"
      files {
        source_file: "fonts/ttf/Dongle-Light.ttf"
        dest_file: "Dongle-Light.ttf"
      }
      files {
        source_file: "fonts/ttf/Dongle-Regular.ttf"
        dest_file: "Dongle-Regular.ttf"
      }
      files {
        source_file: "fonts/ttf/Dongle-Bold.ttf"
        dest_file: "Dongle-Bold.ttf"
      }
      files {
        source_file: "OFL.txt"
        dest_file: "OFL.txt"
      }
      files {
        source_file: "DESCRIPTION.en_us.html"
        dest_file: "DESCRIPTION.en_us.html"
      }
      branch: "master"
    }

## Previous investigation

## Dongle

### Summary

Dongle is a Korean sans-serif font by Yanghee Ryu available in Light, Regular, and Bold weights. It has complete source documentation with a repository URL, commit hash, and an override config.yaml in the google/fonts directory.

### Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | Dongle |
| **Designer** | Yanghee Ryu |
| **License** | OFL |
| **Date Added** | 2021-06-14 |
| **Repository URL** | https://github.com/yangheeryu/Dongle |
| **Commit Hash** | `f7127c4d2450e1cad20254ec692591347e2fc260` |
| **Config YAML** | Override in google/fonts (`ofl/dongle/config.yaml`) |
| **Status** | complete |

### Investigation Details

#### Onboarding History

Dongle v2.000 was added to Google Fonts via PR #3530 (commit `388be86af`) by Aaron Bell on 2021-06-22. The PR commit message states: "Dongle Version 2.000 taken from the upstream repo https://github.com/yangheeryu/Dongle.git at commit https://github.com/yangheeryu/Dongle/commit/71cc5162a79d65b3b9b5ad70398473152ce59ab9."

The source block and override config.yaml were later added in commit `5f31230ff` ("sources info for Dongle: Version 2.000 (PR #3530)").

#### Upstream Repository

The upstream repo at https://github.com/yangheeryu/Dongle contains:
- `sources/Dongle.zip` - source files in a zip archive
- `fonts/ttf/` - compiled TTF files (Dongle-Light.ttf, Dongle-Regular.ttf, Dongle-Bold.ttf)
- No config.yaml in the upstream repo

The HEAD commit is `f7127c4` ("Update README.md"), which matches the METADATA.pb. The original onboarding was at commit `71cc516`, but the 3 commits between then and HEAD are only README/DESCRIPTION updates - no source or font changes.

#### Commit Hash Analysis

The source files (`sources/Dongle.zip`) were last modified at commit `dbd7f34` ("Updated font metrics to match original"), which is earlier than both the onboarding commit (`71cc516`) and the recorded commit (`f7127c4`). Using HEAD is acceptable since no source changes occurred after onboarding.

#### Config YAML

The METADATA.pb uses a `files` block to copy pre-compiled TTFs directly from the upstream repo (not rebuilding from sources). An override config.yaml exists in `ofl/dongle/config.yaml`:
```yaml
buildVariable: false
sources:
  - sources/Dongle.zip
```

Since the override config.yaml exists in the google/fonts directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

### Conclusion

Dongle is fully documented. The source block has the correct repository URL and commit hash. The override config.yaml in the google/fonts directory provides the build configuration. No further action needed.
