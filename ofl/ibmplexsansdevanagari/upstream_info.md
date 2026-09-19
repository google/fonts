# Investigation Report: IBM Plex Sans Devanagari

## Summary

IBM Plex Sans Devanagari is the Devanagari script variant of the IBM Plex typeface family, designed by Mike Abbink and Bold Monday. It was added to Google Fonts on 2021-06-18 (its first and only font update). The upstream repository is `googlefonts/plex`. The METADATA.pb source block has the repository URL but is MISSING the commit hash. The commit hash `4ef531544df71be7bcd614c83b8576930ea68dbc` was referenced in the gftools-packager commit message but was stripped from METADATA.pb. Source files (.designspace + .ufo) exist at the referenced commit.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | IBM Plex Sans Devanagari |
| Repository URL     | https://github.com/googlefonts/plex |
| Commit Hash (missing) | 4ef531544df71be7bcd614c83b8576930ea68dbc |
| Commit Date        | 2021-06-18 |
| Commit Message     | "Devanagari" |
| Config YAML        | None (sources exist, override needed) |
| Source Files       | IBM-Plex-Sans-Devanagari/sources/masters/IBM Plex Sans Devanagari.designspace |
| Build Type         | Pre-compiled static TTFs from Google-Fonts-Fixes |
| Status             | **needs_correction** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/googlefonts/plex`
- **NO `commit` field** (missing!)
- `branch`: `master`
- `primary_script`: `Deva`
- File mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Devanagari/fonts/complete/ttf/`
- 7 static TTF weights (Thin through Bold, no italics)

### Git History in google/fonts

The font file history shows a single font update:
1. `a3dd250ef` - "IBM Plex Sans Devanagari: Version 1.1 added (#3555)" (2021-07-01, by Yanone)

The commit body contains three squashed commits:
1. "[gftools-packager] IBM Plex Sans Devanagari: Version 1.1 added"
2. "IBM Plex Sans Devanagari Version 1.1 taken from the upstream repo https://github.com/googlefonts/plex at commit https://github.com/googlefonts/plex/commit/4ef531544df71be7bcd614c83b8576930ea68dbc."
3. "[gftools-packager] ofl/ibmplexsansdevanagari remove METADATA 'source'. google/fonts#2587"

Same pattern as Condensed: the third sub-commit explicitly removed the `source` block from METADATA.pb (per issue #2587). The source block was later re-added by `66f91f10f` ("Merge upstream.yaml into METADATA.pb") but WITHOUT the commit hash.

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/plex/` confirms:
- Commit `4ef5315` exists and dates to 2021-06-18, message: "Devanagari"
- At this commit, source files exist:
  - `IBM-Plex-Sans-Devanagari/sources/masters/IBM Plex Sans Devanagari.designspace`
  - `IBM-Plex-Sans-Devanagari/sources/masters/IBM Plex Sans Devanagari-Bold.ufo`
  - `IBM-Plex-Sans-Devanagari/sources/masters/IBM Plex Sans Devanagari-Regular.ufo`
  - `IBM-Plex-Sans-Devanagari/sources/masters/IBM Plex Sans Devanagari-Thin.ufo`

Note: These source files were later removed in January 2024 but exist at the referenced commit.

### Config.yaml Status

No config.yaml exists in google/fonts for IBM Plex Sans Devanagari. Source files (.designspace + .ufo) exist at the referenced commit `4ef5315`, so an override config.yaml could be created:
```yaml
sources:
  - IBM-Plex-Sans-Devanagari/sources/masters/IBM Plex Sans Devanagari.designspace
familyName: IBM Plex Sans Devanagari
buildStatic: true
buildOTF: false
```

### Issues Found

1. **Missing commit hash**: The commit hash `4ef531544df71be7bcd614c83b8576930ea68dbc` should be added to the METADATA.pb source block
2. **Missing config.yaml**: An override config.yaml should be created pointing to the .designspace source

## Conclusion

The METADATA.pb source block is missing the commit hash, which was originally recorded by gftools-packager but then removed (issue #2587) and not restored when the source block was re-created from upstream.yaml. The correct commit hash is `4ef531544df71be7bcd614c83b8576930ea68dbc`. Additionally, an override config.yaml should be created since source files exist at the referenced commit.

**Status: needs_correction** (missing commit hash and config.yaml)
