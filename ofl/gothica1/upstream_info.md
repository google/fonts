# Investigation Report: Gothic A1

## Summary

Gothic A1 is a Korean and Latin sans-serif font family by HanYang I&C Co., available in 9 weights (Thin through Black). It was onboarded to Google Fonts on 2018-02-24 via PR #1459 ("korean families r01: added") by Marc Foley. The upstream repository at https://github.com/hanyangfont/Gothic contains only pre-compiled binary font files (TTF and OTF) with no editable source files. The repository has exactly 2 commits, with the latest (599d7e3) dated 2017-12-07, predating the Google Fonts onboarding.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Gothic A1 |
| Designer          | HanYang I&C Co |
| Repository URL    | https://github.com/hanyangfont/Gothic |
| Commit Hash       | 599d7e34fff27a50f3e9266b753ad661d3167b91 |
| Branch            | master |
| Config YAML       | N/A (no buildable sources) |
| Date Added        | 2018-02-24 |
| Status            | **no_config_possible** |
| Confidence        | HIGH |

## Investigation Details

### Onboarding History

The font was onboarded to Google Fonts via PR #1459 ("korean families r01: added"), authored by Marc Foley and merged on 2018-03-13. This PR was a batch addition of multiple Korean font families. The PR body states: "Korean Font binaries have been mastered by Aaron Bell." The PR was part of a larger Korean fonts initiative.

Commit in google/fonts: `16680f8688ffcd467d2eb2146a9ce0343404581d`

The TTF files have not been modified since the original onboarding commit.

### Upstream Repository Analysis

The upstream repository `hanyangfont/Gothic` is hosted under the `hanyangfont` GitHub user account. It contains:

- `fonts/ttf/` - 9 TTF files (Gothic_A1_100.ttf through Gothic_A1_900.ttf)
- `fonts/otf/` - 9 OTF files (for Mac)
- `OFL.txt` - License file
- `README.md`
- Korean font specification document

The repository has exactly **2 commits**:
1. `8ac4dd8` (2017-11-29) - "hanyang fonts" - Initial upload
2. `599d7e3` (2017-12-07) - "Add files via upload" - Latest commit

**No source files exist** in the repository -- no .glyphs, .ufo, .designspace, .sfd, .vfb, or any other editable font source format. The repository contains only pre-compiled binaries and metadata.

Note that the TTF files in the upstream repo have different filenames from those in google/fonts (e.g., `Gothic_A1_400.ttf` vs `GothicA1-Regular.ttf`). The fonts in google/fonts were processed/renamed by Aaron Bell during mastering.

The file sizes also differ between upstream and google/fonts (e.g., upstream Regular is ~1.43 MB while google/fonts Regular is ~2.30 MB), indicating the fonts were reprocessed during onboarding.

### Source Block Status

The METADATA.pb on the main branch of google/fonts does not currently have a source block. A source block was added in commit `9a14639f3` on the feature branch `sources_info_2026-02-25` but has not been merged to main.

### Config YAML Assessment

Since the upstream repository contains only binary font files and no editable sources (.glyphs, .ufo, .designspace, etc.), a config.yaml for gftools-builder is not applicable. The fonts cannot be rebuilt from source using this repository.

## Conclusion

Gothic A1's upstream repository is confirmed as `hanyangfont/Gothic` at commit `599d7e3`. However, the repository contains only pre-compiled binaries, making it impossible to create a gftools-builder config.yaml. The status is **no_config_possible**.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/hanyangfont/Gothic"
  commit: "599d7e34fff27a50f3e9266b753ad661d3167b91"
  files {
    source_file: "fonts/ttf/Gothic_A1_100.ttf"
    dest_file: "GothicA1-Thin.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_200.ttf"
    dest_file: "GothicA1-ExtraLight.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_300.ttf"
    dest_file: "GothicA1-Light.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_400.ttf"
    dest_file: "GothicA1-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_500.ttf"
    dest_file: "GothicA1-Medium.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_600.ttf"
    dest_file: "GothicA1-SemiBold.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_700.ttf"
    dest_file: "GothicA1-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_800.ttf"
    dest_file: "GothicA1-ExtraBold.ttf"
  }
  files {
    source_file: "fonts/ttf/Gothic_A1_900.ttf"
    dest_file: "GothicA1-Black.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
```

**Note**: The files mapping above is approximate. The actual fonts in google/fonts were reprocessed/mastered by Aaron Bell, so they are not byte-identical to the upstream TTFs. A simpler source block with just repository_url and commit (no files mapping) may be more appropriate given that the fonts were reprocessed during onboarding.

Simpler alternative:
```
source {
  repository_url: "https://github.com/hanyangfont/Gothic"
  commit: "599d7e34fff27a50f3e9266b753ad661d3167b91"
}
```
