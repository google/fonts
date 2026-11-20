# Gowun Batang

**Model**: Claude Opus 5.5
**Date**: 2026-11-17

Sources modernized 2026-11: the sources the designer published do not rebuild the fonts
Google Fonts ships (listed under "Earlier sources"), so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Gowun Batang (google/fonts at commit `2086013c4c53`). The
designer's published sources ("Earlier sources") do not rebuild those fonts, so the
family could not be built from them with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/gowunbatang.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from GowunBatang-{Bold,Regular}.ttf, the fonts
  Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/gowunbatang at `bf6ce63b0e06`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts cc39c4c2c304 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF, hinting), 2 styles. Those
tools, including this family's plan `plans/gowunbatang.json`:
https://github.com/felipesanches/gf-source-modernization at `c061ad8`.

`bf6ce63b0e06` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/yangheeryu/Gowun-Batang at
  4e73f5a9a004927220354f4b68a4c720da538147, the designer's repository:
  sources/GowunBatang.zip holds GowunBatang.glyphs (113 MB). Built today it does not
  give the release (shaping differs in 21554 of 11663056 runs for the Regular;
  logs/crater-skipped-2026-11-16), so the fonts as shipped are the source of record
  here.

## Future work

Not part of what Google Fonts ships; for review in a font-update PR:
- commit `753ee3a` (after the equivalence commit): README: say what the earlier sources
  are, and list them

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/yangheeryu/Gowun-Batang"
      commit: "4e73f5a9a004927220354f4b68a4c720da538147"
      files {
        source_file: "fonts/ttf/GowunBatang-Regular.ttf"
        dest_file: "GowunBatang-Regular.ttf"
      }
      files {
        source_file: "fonts/ttf/GowunBatang-Bold.ttf"
        dest_file: "GowunBatang-Bold.ttf"
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

## Investigation: Gowun Batang

### Summary

Gowun Batang is a Korean serif typeface by Yanghee Ryu. It was onboarded to Google Fonts as Version 2.000 via PR #3524 (merged 2021-06-11) by Aaron Bell using gftools-packager. The upstream repository is at `yangheeryu/Gowun-Batang`, and the commit hash `4e73f5a` is explicitly referenced in the PR commit message. The METADATA.pb source block already has the correct repository URL, commit hash, file mappings, and branch. An override `config.yaml` already exists in the google/fonts family directory.

### Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gowun Batang                                                       |
| Designer           | Yanghee Ryu                                                        |
| Repository URL     | https://github.com/yangheeryu/Gowun-Batang                        |
| Commit Hash        | 4e73f5a9a004927220354f4b68a4c720da538147                           |
| Config YAML        | Override config.yaml in google/fonts                               |
| Source Format       | .glyphs (inside sources/GowunBatang.zip)                          |
| Status             | complete                                                           |
| Confidence         | HIGH                                                               |

### Investigation Details

#### METADATA.pb Current State

The current METADATA.pb has a comprehensive source block:

```
source {
  repository_url: "https://github.com/yangheeryu/Gowun-Batang"
  commit: "4e73f5a9a004927220354f4b68a4c720da538147"
  files {
    source_file: "fonts/ttf/GowunBatang-Regular.ttf"
    dest_file: "GowunBatang-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/GowunBatang-Bold.ttf"
    dest_file: "GowunBatang-Bold.ttf"
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
```

#### Upstream Repository Analysis

- **Repository**: https://github.com/yangheeryu/Gowun-Batang
- **Cached at**: upstream_repos/fontc_crater_cache/yangheeryu/Gowun-Batang
- **Branches**: master only
- **Latest commit**: `4e73f5a` ("Batang ready to go!", 2021-06-10) by Aaron Bell

The repository contains:
- `sources/GowunBatang.zip` - Contains `GowunBatang.glyphs` (114 MB, merged Regular+Bold)
- `build.py` - Custom build script using glyphsLib, ufo2ft, fontTools
- `fonts/ttf/GowunBatang-Regular.ttf` and `fonts/ttf/GowunBatang-Bold.ttf` - Pre-built TTFs
- No `config.yaml` in upstream

#### Onboarding History

The font was onboarded via PR #3524, merged 2021-06-11:
- **Commit**: `539f6c4bb` in google/fonts
- **Author**: Aaron Bell (aaronbell)
- **Message**: "Gowun Batang: Version 2.000 added (#3524)"
- **gftools-packager reference**: "Gowun Batang Version 2.000 taken from the upstream repo https://github.com/yangheeryu/Gowun-Batang.git at commit https://github.com/yangheeryu/Gowun-Batang/commit/4e73f5a9a004927220354f4b68a4c720da538147"

The commit hash `4e73f5a` is the latest (HEAD) commit in the upstream repo and matches the gftools-packager reference exactly. This is also the commit authored by Aaron Bell himself ("Batang ready to go!") on 2021-06-10, one day before the google/fonts merge on 2021-06-11.

#### Config YAML Assessment

An override `config.yaml` already exists at `ofl/gowunbatang/config.yaml` in google/fonts:

```yaml
buildVariable: false
sources:
  - sources/GowunBatang.zip
```

This was added in commit `fa89220ae` ("sources info for Gowun Batang: Version 2.000 (PR #3524)", 2025-11-11).

The upstream repo uses a custom `build.py` script (not gftools-builder), so the override config.yaml in google/fonts is the correct approach. The source is a `.glyphs` file inside `GowunBatang.zip`.

#### Commit Hash Verification

The commit `4e73f5a` is verified as correct:
- It is the HEAD commit on the master branch of the upstream repo
- It is explicitly referenced in the gftools-packager message in the google/fonts onboarding commit
- It was authored on 2021-06-10, one day before the google/fonts PR merge on 2021-06-11
- It was authored by Aaron Bell, who also submitted the google/fonts PR

### Conclusion

This family is fully complete. The METADATA.pb source block has the correct repository URL, commit hash, file mappings, and branch. An override `config.yaml` already exists in the google/fonts family directory.

#### Current METADATA.pb Source Block (correct, no changes needed)

```
source {
  repository_url: "https://github.com/yangheeryu/Gowun-Batang"
  commit: "4e73f5a9a004927220354f4b68a4c720da538147"
  files {
    source_file: "fonts/ttf/GowunBatang-Regular.ttf"
    dest_file: "GowunBatang-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/GowunBatang-Bold.ttf"
    dest_file: "GowunBatang-Bold.ttf"
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
```

**Status**: complete
**Confidence**: HIGH -- commit hash directly referenced by gftools-packager in the onboarding commit message, and it is the HEAD of the upstream repo.
