# Investigation Report: IBM Plex Mono

## Summary

IBM Plex Mono is the monospace variant of the IBM Plex typeface family, designed by Mike Abbink and Bold Monday. It was first added to Google Fonts on 2018-03-12 and last updated to Version 2.3 on 2022-11-09. The upstream repository is `googlefonts/plex` (a fork of IBM/plex). The METADATA.pb has a complete source block with repository URL, commit hash, and file mappings. An override config.yaml exists in google/fonts pointing to .designspace sources that exist at the referenced commit.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | IBM Plex Mono |
| Repository URL     | https://github.com/googlefonts/plex |
| Commit Hash        | 9ab3b5b3b96325fb20f365ee0804adca92024cbf |
| Commit Date        | 2022-11-09 |
| Commit Message     | "Latest Mono fonts" |
| Config YAML        | Override config.yaml in google/fonts |
| Source Files       | IBM-Plex-Mono/sources/masters/IBM Plex Mono Roman.designspace, IBM-Plex-Mono/sources/masters/IBM Plex Mono Italic.designspace |
| Build Type         | Pre-compiled TTFs from Google-Fonts-Fixes (override config available for gftools-builder) |
| Status             | **complete** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb contains a complete source block:
- `repository_url`: `https://github.com/googlefonts/plex`
- `commit`: `9ab3b5b3b96325fb20f365ee0804adca92024cbf`
- `branch`: `master`
- File mappings pull pre-compiled TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Mono/fonts/complete/ttf/`
- 14 static TTF weights (Thin through Bold, Roman and Italic)

### Git History in google/fonts

The font file history shows multiple updates:
1. `b271bab46` - Initial addition: "ibmplexmono: v2.000 added (#1481)"
2. `115c6eb01` - "Add updated and new versions of IBM Plex (#1837)"
3. `465b90c97` - "IBM Plex Mono: Version 2.1 added (#3527)"
4. `633f32005` - Last font update: "[gftools-packager] IBM Plex Mono: Version 2.3 added (#5524)" (2022-11-09, by Yanone)

The commit `633f32005` explicitly references the upstream commit `9ab3b5b` in its body: "IBM Plex Mono Version 2.3 taken from the upstream repo https://github.com/googlefonts/plex at commit 9ab3b5b3b96325fb20f365ee0804adca92024cbf."

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/plex/` confirms:
- Remote: `https://github.com/googlefonts/plex` (fork of IBM/plex)
- Commit `9ab3b5b` exists and dates to 2022-11-09, message: "Latest Mono fonts"
- At this commit, source files exist:
  - `IBM-Plex-Mono/sources/masters/IBM Plex Mono Roman.designspace`
  - `IBM-Plex-Mono/sources/masters/IBM Plex Mono Italic.designspace`
  - 6 UFO master directories (Bold, Bold Italic, Italic, Regular, Thin, Thin Italic)

Note: Source files were later removed from the repo in January 2024 (`98d717710`), but they exist at the referenced commit.

### Override config.yaml

An override config.yaml exists at `ofl/ibmplexmono/config.yaml` in google/fonts:
```yaml
sources:
  - IBM-Plex-Mono/sources/masters/IBM Plex Mono Roman.designspace
  - IBM-Plex-Mono/sources/masters/IBM Plex Mono Italic.designspace
familyName: IBM Plex Mono
buildStatic: true
buildOTF: false
```

This was added in commit `f6c68379a` ("Add override config.yaml for 50 font families").

### Repository Structure Note

The `googlefonts/plex` repo is a Google-maintained fork of the original `IBM/plex` repository. It contains a `Google-Fonts-Fixes` directory with pre-compiled fonts specifically prepared for Google Fonts. The original IBM/plex monorepo structure had source files under `IBM-Plex-{Family}/sources/masters/`, but these were removed in January 2024 when the repo was reorganized into a `packages/` structure with only distribution files.

## Conclusion

IBM Plex Mono has a complete source block in METADATA.pb with a verified commit hash. The override config.yaml correctly points to .designspace source files that exist at the referenced commit. No corrections needed.

**Status: complete**
