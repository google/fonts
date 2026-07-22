# Investigation Report: IBM Plex Sans Hebrew

## Summary

IBM Plex Sans Hebrew is the Hebrew script variant of the IBM Plex typeface family, designed by Mike Abbink and Bold Monday. It was added to Google Fonts on 2021-06-18 (its first and only font update). The upstream repository is `googlefonts/plex`. The METADATA.pb source block has the repository URL but is MISSING the commit hash. The commit hash `0f91126e49779170e7b2d18614f9d89a1855659b` was referenced in the gftools-packager commit message but was stripped from METADATA.pb. Source files (.designspace + .ufo) exist at the referenced commit.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | IBM Plex Sans Hebrew |
| Repository URL     | https://github.com/googlefonts/plex |
| Commit Hash (missing) | 0f91126e49779170e7b2d18614f9d89a1855659b |
| Commit Date        | 2021-06-18 |
| Commit Message     | "Hebrew" |
| Config YAML        | None (sources exist, override needed) |
| Source Files       | IBM-Plex-Sans-Hebrew/sources/masters/IBM Plex Sans Hebrew.designspace |
| Build Type         | Pre-compiled static TTFs from Google-Fonts-Fixes |
| Status             | **needs_correction** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/googlefonts/plex`
- **NO `commit` field** (missing!)
- `branch`: `master`
- `primary_script`: `Hebr`
- File mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Hebrew/fonts/complete/ttf/`
- 7 static TTF weights (Thin through Bold, no italics)

### Git History in google/fonts

The font file history shows a single font update:
1. `6d4b5da42` - "IBM Plex Sans Hebrew: Version 1.2 added (#3554)" (2021-07-01, by Yanone)

The commit body contains three squashed commits:
1. "[gftools-packager] IBM Plex Sans Hebrew: Version 1.2 added"
2. "IBM Plex Sans Hebrew Version 1.2 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/0f91126e49779170e7b2d18614f9d89a1855659b."
3. "[gftools-packager] ofl/ibmplexsanshebrew remove METADATA 'source'. google/fonts#2587"

Same pattern as Condensed and Devanagari: the third sub-commit explicitly removed the `source` block from METADATA.pb (per issue #2587). The source block was later re-added by `66f91f10f` ("Merge upstream.yaml into METADATA.pb") but WITHOUT the commit hash.

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/plex/` confirms:
- Commit `0f91126` exists and dates to 2021-06-18, message: "Hebrew"
- At this commit, source files exist:
  - `IBM-Plex-Sans-Hebrew/sources/masters/IBM Plex Sans Hebrew.designspace`
  - `IBM-Plex-Sans-Hebrew/sources/masters/IBM Plex Sans Hebrew-Bold.ufo`
  - `IBM-Plex-Sans-Hebrew/sources/masters/IBM Plex Sans Hebrew-Regular.ufo`
  - `IBM-Plex-Sans-Hebrew/sources/masters/IBM Plex Sans Hebrew-Thin.ufo`

Note: These source files were later removed in January 2024 but exist at the referenced commit.

### Config.yaml Status

No config.yaml exists in google/fonts for IBM Plex Sans Hebrew. Source files (.designspace + .ufo) exist at the referenced commit `0f91126`, so an override config.yaml could be created:
```yaml
sources:
  - IBM-Plex-Sans-Hebrew/sources/masters/IBM Plex Sans Hebrew.designspace
familyName: IBM Plex Sans Hebrew
buildStatic: true
buildOTF: false
```

### Issues Found

1. **Missing commit hash**: The commit hash `0f91126e49779170e7b2d18614f9d89a1855659b` should be added to the METADATA.pb source block
2. **Missing config.yaml**: An override config.yaml should be created pointing to the .designspace source

## Conclusion

The METADATA.pb source block is missing the commit hash, which was originally recorded by gftools-packager but then removed (issue #2587) and not restored when the source block was re-created from upstream.yaml. The correct commit hash is `0f91126e49779170e7b2d18614f9d89a1855659b`. Additionally, an override config.yaml should be created since source files exist at the referenced commit.

**Status: needs_correction** (missing commit hash and config.yaml)
