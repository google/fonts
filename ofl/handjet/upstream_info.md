# Investigation Report: Handjet

## Summary

Handjet is a variable display font designed by David Brezina at Rosetta Type, first added to Google Fonts on 2020-09-11. It was updated to version 2.003 via gftools-packager in PR #5376 on 2022-10-13. The METADATA.pb already contains a complete source block with repository URL and commit hash. The upstream repo has Glyphs sources but no config.yaml; however, an override config.yaml already exists in the google/fonts family directory. The existing source metadata is correct and complete.

## Key Findings

| Field | Value |
|---|---|
| **Family Name** | Handjet |
| **Designer** | Rosetta, David Brezina |
| **Date Added** | 2020-09-11 |
| **Repository URL** | https://github.com/rosettatype/handjet |
| **Commit Hash** | 3918b7798e06c81da6bc558e88dfddd5a6b49807 |
| **Config YAML** | Override config.yaml in google/fonts (sources/Handjet.glyphs) |
| **Status** | complete |
| **Confidence** | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb already has a source block:
```
source {
  repository_url: "https://github.com/rosettatype/handjet"
  commit: "3918b7798e06c81da6bc558e88dfddd5a6b49807"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Handjet[ELGR,ELSH,wght].ttf"
    dest_file: "Handjet[ELGR,ELSH,wght].ttf"
  }
  branch: "master"
}
```

### Git History in google/fonts

Key commits:
1. `16a38d82a` - "Handjet: version 2.000 added (#2679)" - Initial onboarding
2. `2ec566467` (2022-10-13) - "[gftools-packager] Handjet: Version 2.003 added (#5376)" - Update to v2.003, referencing commit `3918b77` from upstream
3. `e11ccfef5` - "sources info for Handjet: Version 2.003 (PR #5376)" - Added config.yaml override and merged upstream.yaml into METADATA.pb

### Commit Hash Verification

The referenced commit `3918b7798e06c81da6bc558e88dfddd5a6b49807` exists in the upstream repo:
- Date: 2022-10-04 (9 days before the google/fonts merge on 2022-10-13)
- Message: "Added Acaron glyphs, stylistic set names"
- The font file at that commit (`fonts/Handjet[ELGR,ELSH,wght].ttf`) is exactly 283,912 bytes
- The font file in google/fonts is also exactly 283,912 bytes
- **Binary sizes match perfectly**, confirming this is the correct commit

### Upstream Repository

The upstream repository at `https://github.com/rosettatype/handjet` (cached at `rosettatype/handjet`) contains:
- **Sources**: `sources/Handjet.glyphs` (Glyphs format, gftools-builder compatible)
- **Production**: `production/Handjet.designspace`, `production/build.sh`, workflow files
- **Compiled fonts**: `fonts/Handjet[ELGR,ELSH,wght].ttf` and `.woff2`
- **No config.yaml** in the upstream repo (neither at root nor at the referenced commit)

### Config YAML

An override `config.yaml` already exists in the google/fonts family directory at `ofl/handjet/config.yaml`:
```yaml
buildVariable: true
sources:
  - sources/Handjet.glyphs
```

This was added in commit `e11ccfef5` ("sources info for Handjet: Version 2.003 (PR #5376)"). Since the override config.yaml exists locally, no `config_yaml` field is needed in METADATA.pb, and google-fonts-sources will auto-detect it.

### Post-Onboarding Upstream Activity

There have been approximately 30 additional commits in the upstream repo after the referenced commit (3918b77), including version 2.004 updates and Korean (Hangeul) support. These changes have not been incorporated into google/fonts and would require separate review.

## Conclusion

The Handjet source metadata is already complete and correct. The repository URL, commit hash, and file mappings are all verified. The override config.yaml is in place. No changes are needed.

### Current METADATA.pb Source Block (Already Correct)

```
source {
  repository_url: "https://github.com/rosettatype/handjet"
  commit: "3918b7798e06c81da6bc558e88dfddd5a6b49807"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Handjet[ELGR,ELSH,wght].ttf"
    dest_file: "Handjet[ELGR,ELSH,wght].ttf"
  }
  branch: "master"
}
```

**Status**: complete (source block present and verified, override config.yaml in place)
