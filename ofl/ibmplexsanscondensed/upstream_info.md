# Investigation Report: IBM Plex Sans Condensed

## Summary

IBM Plex Sans Condensed is the condensed variant of the IBM Plex Sans typeface family, designed by Mike Abbink and Bold Monday. It was first added to Google Fonts on 2018-03-12 and last updated to Version 1.3 on 2021-07-15. The upstream repository is `googlefonts/plex`. The METADATA.pb source block has the repository URL but is MISSING the commit hash. The commit hash `71d012bccb31a2e282cc46de63b387ff7f676287` was referenced in the gftools-packager commit message but was stripped from METADATA.pb when the source block was later cleared and re-added. Source files (.designspace + .ufo) exist at the referenced commit.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | IBM Plex Sans Condensed |
| Repository URL     | https://github.com/googlefonts/plex |
| Commit Hash (missing) | 71d012bccb31a2e282cc46de63b387ff7f676287 |
| Commit Date        | 2021-06-11 |
| Commit Message     | "Clarified URL" |
| Config YAML        | None (sources exist, override needed) |
| Source Files       | IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Roman.designspace, IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Italic.designspace |
| Build Type         | Pre-compiled static TTFs from Google-Fonts-Fixes |
| Status             | **needs_correction** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/googlefonts/plex`
- **NO `commit` field** (missing!)
- `branch`: `master`
- File mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Condensed/fonts/complete/ttf/`
- 14 static TTF weights (Thin through Bold, Roman and Italic)

### Git History in google/fonts

The font file history shows:
1. `ae12d6189` - Initial addition: "ibmplexsanscondensed: v1.001 added (#1484)"
2. `115c6eb01` - "Add updated and new versions of IBM Plex (#1837)"
3. `137470e1c` - Last font update: "IBM Plex Sans Condensed: Version 1.3 added (#3440)" (2021-07-15, by Yanone)

The commit `137470e1c` body contains three squashed commits:
1. "[gftools-packager] IBM Plex Sans Condensed: Version 1.3 added"
2. "IBM Plex Sans Condensed Version 1.3 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/71d012bccb31a2e282cc46de63b387ff7f676287."
3. "[gftools-packager] ofl/ibmplexsanscondensed remove METADATA 'source'. google/fonts#2587"

The third sub-commit explicitly removed the `source` block from METADATA.pb (per issue #2587, which was about cleaning up incomplete/broken source blocks). The source block was later re-added by commit `66f91f10f` ("Merge upstream.yaml into METADATA.pb") but WITHOUT the commit hash.

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/plex/` confirms:
- Commit `71d012b` exists and dates to 2021-06-11, message: "Clarified URL"
- At this commit, source files exist:
  - `IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Roman.designspace`
  - `IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Italic.designspace`
  - 6 UFO master directories (Bold, Bold Italic, Italic, Regular, Thin, Thin Italic)

Note: These source files were later removed in January 2024 but exist at the referenced commit.

### Config.yaml Status

No config.yaml exists in google/fonts for IBM Plex Sans Condensed. Source files (.designspace + .ufo) exist at the referenced commit `71d012b`, so an override config.yaml could be created:
```yaml
sources:
  - IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Roman.designspace
  - IBM-Plex-Sans-Condensed/sources/masters/IBM Plex Sans Condensed Italic.designspace
familyName: IBM Plex Sans Condensed
buildStatic: true
buildOTF: false
```

### Issues Found

1. **Missing commit hash**: The commit hash `71d012bccb31a2e282cc46de63b387ff7f676287` should be added to the METADATA.pb source block
2. **Missing config.yaml**: An override config.yaml should be created pointing to the .designspace sources

## Conclusion

The METADATA.pb source block is missing the commit hash, which was originally recorded by gftools-packager but then removed (issue #2587) and not restored when the source block was re-created from upstream.yaml. The correct commit hash is `71d012bccb31a2e282cc46de63b387ff7f676287`. Additionally, an override config.yaml should be created since source files exist at the referenced commit.

**Status: needs_correction** (missing commit hash and config.yaml)
