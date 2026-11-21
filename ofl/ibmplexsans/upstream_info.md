# Investigation Report: IBM Plex Sans

## Summary

IBM Plex Sans is the primary sans-serif variant of the IBM Plex typeface family, designed by Mike Abbink and Bold Monday. It was first added to Google Fonts on 2018-03-12 and last updated to Version 3.201 on 2025-01-10 as a variable font (wdth + wght axes). The upstream repository is `googlefonts/plex`. The METADATA.pb has a complete source block with repository URL and commit hash, but the referenced commit (from January 2025) post-dates the removal of source files from the repository. No config.yaml exists for this family.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | IBM Plex Sans |
| Repository URL     | https://github.com/googlefonts/plex |
| Commit Hash        | 3e312890b3b9e47378b30dedfe4196a42151243c |
| Commit Date        | 2025-01-10 |
| Commit Message     | "Discard static Sans entirely, pretend Var Sans is the only Sans moving forward" |
| Config YAML        | None |
| Source Files       | None at referenced commit (sources removed Jan 2024) |
| Build Type         | Pre-compiled variable TTFs from Google-Fonts-Fixes |
| Status             | **missing_config** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/googlefonts/plex`
- `commit`: `3e312890b3b9e47378b30dedfe4196a42151243c`
- `branch`: `master`
- File mappings pull variable TTFs from `Google-Fonts-Fixes/fonts/IBM-Plex-Sans/fonts/complete/ttf/`
- 2 variable font files: `IBMPlexSans[wdth,wght].ttf` and `IBMPlexSans-Italic[wdth,wght].ttf`
- Axes: wdth (75-100), wght (100-700)

This was a major update from static instances (14 TTFs) to variable fonts.

### Git History in google/fonts

The font file history shows:
1. `42ee46942` - Initial addition: "ibmplexsans: v2.001 added (#1483)"
2. `115c6eb01` - "Add updated and new versions of IBM Plex (#1837)"
3. `e0b9f6ca2` - "IBM Plex Sans: Version 3.2 added (#3439)"
4. `8409f033c` - Last font update: "IBM Plex Sans: Version 3.201 added" (2025-01-10, by Yanone)

The commit body says: "Taken from the upstream repo https://github.com/googlefonts/plex at commit 3e312890b3b9e47378b30dedfe4196a42151243c. Resolves #2407."

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/plex/` confirms:
- Commit `3e31289` exists and dates to 2025-01-10, message: "Discard static Sans entirely, pretend Var Sans is the only Sans moving forward"
- At this commit, NO source files exist for IBM Plex Sans (the `IBM-Plex-Sans/sources/` directory was removed in January 2024)
- Only pre-compiled variable TTFs exist at `Google-Fonts-Fixes/fonts/IBM-Plex-Sans/fonts/complete/ttf/`

Sources existed before January 2024:
- `IBM-Plex-Sans/sources/masters/IBM Plex Sans Roman.designspace`
- `IBM-Plex-Sans/sources/masters/IBM Plex Sans Italic.designspace`

But these were deleted in commits `d8d4ace23` (2024-01-23) and `98d717710` (2024-01-26).

### Config.yaml Status

No config.yaml exists in google/fonts for IBM Plex Sans, and no config.yaml exists in the upstream repo. Since the referenced commit has no buildable sources, creating an override config.yaml would require pointing to an older commit or to the original IBM/plex repo where sources may still exist.

### Repository Structure Note

The referenced commit is the HEAD of the googlefonts/plex fork. The original source files were stored under `IBM-Plex-Sans/sources/masters/` with .designspace and .ufo files, but these were removed when the repository was reorganized in January 2024. The fonts served to Google Fonts are pre-compiled variable TTFs placed in the `Google-Fonts-Fixes/` directory.

## Conclusion

The METADATA.pb source block has correct repository URL and commit hash for the pre-compiled font delivery. However, no config.yaml can be created for this commit since source files do not exist at the referenced commit. A config.yaml pointing to sources would require referencing a commit prior to January 2024 when sources still existed, but that would not match the current fonts being served.

**Status: missing_config**
