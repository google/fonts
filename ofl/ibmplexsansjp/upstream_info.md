# Investigation Report: IBM Plex Sans JP

## Summary

IBM Plex Sans JP is the Japanese variant of the IBM Plex typeface family, designed by Mike Abbink and Bold Monday. It was added to Google Fonts on 2022-09-12 (its first and only font update). The upstream repository is `googlefonts/plex`. The METADATA.pb has a complete source block with repository URL, commit hash, and file mappings. An override config.yaml exists in google/fonts pointing to a .glyphs source file that exists at the referenced commit.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | IBM Plex Sans JP |
| Repository URL     | https://github.com/googlefonts/plex |
| Commit Hash        | 80fcb676509354caa75c6bfc7f9db598545d466f |
| Commit Date        | 2022-09-12 |
| Commit Message     | "Converted all packager files to new format" |
| Config YAML        | Override config.yaml in google/fonts |
| Source Files       | IBM-Plex-Sans-JP/sources/masters/IBM Plex Sans JP.glyphs |
| Build Type         | Pre-compiled static TTFs from Google-Fonts-Fixes (override config available for gftools-builder) |
| Status             | **complete** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/googlefonts/plex`
- `commit`: `80fcb676509354caa75c6bfc7f9db598545d466f`
- `branch`: `master`
- `primary_script`: `Jpan`
- File mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-JP/fonts/complete/ttf/`
- 7 static TTF weights (Thin through Bold, no italics)

### Git History in google/fonts

The font file history shows:
1. `f6d4d2bf9` - Initial and only font update: "[gftools-packager] IBM Plex Sans JP: Version 1.001 added (#5226)" (2022-09-22, by Yanone)
2. `6a2dc64d2` - "Update METADATA.pb (#5295)" (metadata changes only)
3. `591845e2c` - "IBM Plex JP: trying another lang ID (#5439)" (metadata changes only)

The commit body says: "IBM Plex Sans JP Version 1.001 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/80fcb676509354caa75c6bfc7f9db598545d466f."

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/plex/` confirms:
- Commit `80fcb67` exists and dates to 2022-09-12, message: "Converted all packager files to new format"
- At this commit, source files exist:
  - `IBM-Plex-Sans-JP/sources/masters/IBM Plex Sans JP.glyphs`
  - `IBM-Plex-Sans-JP/sources/instances/postscript/IBM Plex Sans JP-*.glyphs` (per-instance .glyphs files)
  - `IBM-Plex-Sans-JP/sources/instances/truetype/IBM Plex Sans JP-*.glyphs` (per-instance .glyphs files)

Note: Source files were later removed from the repo in January 2024, but they exist at the referenced commit.

### Override config.yaml

An override config.yaml exists at `ofl/ibmplexsansjp/config.yaml` in google/fonts:
```yaml
sources:
  - IBM-Plex-Sans-JP/sources/masters/IBM Plex Sans JP.glyphs
familyName: IBM Plex Sans JP
buildStatic: true
buildOTF: false
```

This was added in commit `f6c68379a` ("Add override config.yaml for 50 font families").

### Repository Structure Note

The `googlefonts/plex` repo is a Google-maintained fork of IBM/plex. At the referenced commit, the original IBM/plex monorepo structure was still intact with source files under `IBM-Plex-{Family}/sources/`. These sources were removed in January 2024 when the repo was reorganized.

## Conclusion

IBM Plex Sans JP has a complete source block in METADATA.pb with a verified commit hash. The override config.yaml correctly points to the .glyphs source file that exists at the referenced commit. No corrections needed.

**Status: complete**
