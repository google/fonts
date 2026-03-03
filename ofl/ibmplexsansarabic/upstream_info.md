# Investigation Report: IBM Plex Sans Arabic

## Summary

IBM Plex Sans Arabic is the Arabic script variant of the IBM Plex typeface family, designed by Mike Abbink, Bold Monday, Khajag Apelian, and Wael Morcos. It was added to Google Fonts on 2021-06-17 and last updated to Version 1.101 on 2024-11-08. The upstream repository is `googlefonts/plex`. The METADATA.pb has a complete source block with repository URL and commit hash, but the referenced commit (from November 2024) post-dates the removal of source files from the repository. No config.yaml exists for this family.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | IBM Plex Sans Arabic |
| Repository URL     | https://github.com/googlefonts/plex |
| Commit Hash        | e80bf9282a630e70d6c1459f4125c9ec0e75316b |
| Commit Date        | 2024-11-08 |
| Commit Message     | "Delete old temp folder" |
| Config YAML        | None |
| Source Files       | None at referenced commit (sources removed Jan 2024) |
| Build Type         | Pre-compiled static TTFs from Google-Fonts-Fixes |
| Status             | **missing_config** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/googlefonts/plex`
- `commit`: `e80bf9282a630e70d6c1459f4125c9ec0e75316b`
- `branch`: `master`
- `primary_script`: `Arab`
- File mappings pull static TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Arabic/fonts/complete/ttf/`
- 7 static TTF weights (Thin through Bold, no italics)

### Git History in google/fonts

The font file history shows:
1. `121e596e0` - Initial addition: "IBM Plex Sans Arabic: Version 1.1 added (#3545)"
2. `2cf301086` - Last font update: "IBM Plex Sans Arabic: Version 1.101 added" (2024-11-08, by Yanone)

The commit body says: "Taken from the upstream repo https://github.com/googlefonts/plex at commit e80bf9282a630e70d6c1459f4125c9ec0e75316b. Resolves #7611."

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/plex/` confirms:
- Commit `e80bf92` exists and dates to 2024-11-08, message: "Delete old temp folder"
- At this commit, NO source files exist for IBM Plex Sans Arabic (the `IBM-Plex-Sans-Arabic/sources/` directory was removed in January 2024)
- Only pre-compiled TTFs exist at `Google-Fonts-Fixes/fonts/IBM-Plex-Sans-Arabic/fonts/complete/ttf/`

Sources existed before January 2024:
- `IBM-Plex-Sans-Arabic/sources/masters/IBM Plex Sans Arabic.designspace`
- Plus .ufo master directories

These were deleted in commits `d8d4ace23` (2024-01-23) and `98d717710` (2024-01-26).

### Config.yaml Status

No config.yaml exists in google/fonts for IBM Plex Sans Arabic, and no config.yaml exists in the upstream repo. Since the referenced commit has no buildable sources, creating an override config.yaml is not possible for this commit.

### Repository Structure Note

The `googlefonts/plex` repo is a Google-maintained fork of IBM/plex. The font files in Google-Fonts-Fixes were prepared specifically for Google Fonts consumption. The original sources under `IBM-Plex-Sans-Arabic/sources/masters/` were removed in January 2024 when the repo was reorganized.

## Conclusion

The METADATA.pb source block has correct repository URL and commit hash for the pre-compiled font delivery. However, no config.yaml can be created for this commit since source files do not exist at the referenced commit. A config pointing to sources would require referencing a commit prior to January 2024.

**Status: missing_config**
