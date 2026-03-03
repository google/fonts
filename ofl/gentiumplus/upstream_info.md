# Investigation: Gentium Plus

## Summary

Gentium Plus is a serif typeface designed by SIL International, part of the Gentium family. It was onboarded to Google Fonts on 2022-05-13 via PR #4662 by Emma Marichal. The fonts were taken from the pre-built v6.101 release archive of the upstream repo `silnrsi/font-gentium`. Both Gentium Plus and Gentium Book Plus are instances generated from the same designspace files in this shared upstream repository.

The upstream build system is SIL's `smith` toolchain (not gftools-builder), which uses `.feax` extended feature files, `psfchangettfglyphnames`, `ttfautohint`, and TypeTuner -- none of which are supported by gftools-builder. Creating an override `config.yaml` is not feasible because the source files require smith-specific preprocessing that cannot be replicated with fontmake/gftools-builder.

The METADATA.pb source block already has the correct `repository_url` and `archive_url`, but is missing a `commit` hash. The correct commit is the v6.101 tag: `7ac5e5ca61b776c5b8df4522c04b9707573ffd42`.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Gentium Plus |
| Repository URL     | https://github.com/silnrsi/font-gentium |
| Onboarding Commit  | `7ac5e5ca61b776c5b8df4522c04b9707573ffd42` (tag v6.101, 2022-02-09) |
| Config YAML        | None (smith build system, not gftools-builder compatible) |
| Status             | no_config_possible |
| Confidence         | HIGH |
| Onboarding PR      | google/fonts#4662 |
| Onboarding Author  | Emma Marichal |
| Onboarding Date    | 2022-05-13 |

## Investigation Details

### METADATA.pb Current State

The existing source block contains:
- `repository_url`: `https://github.com/silnrsi/font-gentium` (correct)
- `archive_url`: `https://github.com/silnrsi/font-gentium/releases/download/v6.101/GentiumPlus-6.101.zip` (correct)
- `branch`: `master` (correct)
- File mappings for 4 TTF files + OFL.txt from the release archive
- **Missing**: `commit` hash
- **Missing**: `config_yaml` (but not applicable -- see below)

### Onboarding History

PR #4662 (merged 2022-05-13) by Emma Marichal added Gentium Plus. The commit message states:

> "Gentium Plus Version 6.101 taken from the upstream repo https://github.com/silnrsi/font-gentium at commit https://github.com/silnrsi/font-gentium/commit/."

The commit URL is empty -- the packager tool failed to capture the actual commit hash. The original `upstream.yaml` specified the release archive URL, confirming fonts were taken from pre-built binaries.

### Commit Hash Determination

The tracking JSON had commit `202d6d3bf1c92db9dd8f9635697ec302a6441725` (2022-05-06, "Add placeholders and glyph_data for new glyphs"), which is 21 commits after v6.101. This was likely the HEAD of master when `gftools-packager` ran, but it is NOT the correct reference commit because:

1. The fonts were taken from the **release archive** (v6.101 ZIP), not compiled from source
2. The release archive corresponds to the **v6.101 tag**, which points to commit `7ac5e5ca61b776c5b8df4522c04b9707573ffd42` (2022-02-09)
3. The 21 subsequent commits between v6.101 and 202d6d3 added new glyphs, feature changes, and design revisions that are NOT reflected in the v6.101 binaries

The correct commit hash is: **`7ac5e5ca61b776c5b8df4522c04b9707573ffd42`** (v6.101 tag).

### Upstream Repository Analysis

- **Repo**: https://github.com/silnrsi/font-gentium
- **Shared with**: Gentium Book Plus (same repo, same designspace files)
- **Build system**: `smith` (SIL's build tool), configured via `wscript`
- **Source files at v6.101**:
  - `source/GentiumPlusRoman.designspace` (instances: Gentium Plus Regular/Bold, Gentium Book Plus Regular/Bold)
  - `source/GentiumPlusItalic.designspace` (instances: Gentium Plus Italic/BoldItalic, Gentium Book Plus Italic/BoldItalic)
  - `source/masters/GentiumPlusMaster-Regular.ufo`
  - `source/masters/GentiumPlusMaster-ExtraBold.ufo`
  - `source/masters/GentiumPlusMaster-Italic.ufo`
  - `source/masters/GentiumPlusMaster-ExtraBoldItalic.ufo`
- **Feature files**: `.feax` format (SIL extended, not standard `.fea`)
- **Custom build steps**: `psfchangettfglyphnames`, `ttfautohint`, TypeTuner, `.feax` -> `.fea` conversion
- **Graphite**: Sources present but commented out in v6.101 wscript
- **Latest version**: v6.200 (2023-02-01), with active development continuing

### Why config.yaml Is Not Possible

The smith build system uses several SIL-specific tools and formats that have no gftools-builder equivalent:
1. **`.feax` files**: Extended OpenType feature format requiring pysilfont preprocessing
2. **`psfchangettfglyphnames`**: Post-processing step for TTF glyph naming
3. **`ttfautohint`**: Custom auto-hinting with reference fonts
4. **TypeTuner**: SIL's font customization technology
5. **`classes.xml`**: Custom class definitions separate from the designspace

Without these, gftools-builder/fontmake would produce significantly different output from the official release binaries.

## Conclusion

The METADATA.pb source block needs a `commit` hash added. No `config_yaml` is possible due to the smith build system.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/silnrsi/font-gentium"
  commit: "7ac5e5ca61b776c5b8df4522c04b9707573ffd42"
  archive_url: "https://github.com/silnrsi/font-gentium/releases/download/v6.101/GentiumPlus-6.101.zip"
  files {
    source_file: "GentiumPlus-6.101/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "GentiumPlus-6.101/GentiumPlus-Regular.ttf"
    dest_file: "GentiumPlus-Regular.ttf"
  }
  files {
    source_file: "GentiumPlus-6.101/GentiumPlus-Italic.ttf"
    dest_file: "GentiumPlus-Italic.ttf"
  }
  files {
    source_file: "GentiumPlus-6.101/GentiumPlus-Bold.ttf"
    dest_file: "GentiumPlus-Bold.ttf"
  }
  files {
    source_file: "GentiumPlus-6.101/GentiumPlus-BoldItalic.ttf"
    dest_file: "GentiumPlus-BoldItalic.ttf"
  }
  branch: "master"
}
```

### Status: `no_config_possible`
### Confidence: HIGH
