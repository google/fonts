# Investigation Report: Harmattan

## Summary

Harmattan is an Arabic sans-serif typeface by SIL International, added to Google Fonts on 2020-07-03. It has been updated multiple times, most recently to version 4.400 (from upstream commit labeled v4.401). The METADATA.pb already contains a complete source block with repository URL, commit hash, archive URL, and file mappings. An override `config.yaml` exists in the google/fonts family directory. The source block is complete as-is.

## Key Findings

| Field              | Value                                                                 |
|--------------------|-----------------------------------------------------------------------|
| Family Name        | Harmattan                                                             |
| Designer           | SIL International                                                     |
| Repository URL     | https://github.com/silnrsi/font-harmattan                            |
| Commit Hash        | b8d089bdb2cf97351cff63beaa9d68a6273dcc42                              |
| Config YAML        | Override config.yaml in google/fonts                                  |
| Status             | complete                                                              |
| Confidence         | HIGH                                                                  |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb already has a fully populated source block:
- `repository_url`: `https://github.com/silnrsi/font-harmattan`
- `commit`: `b8d089bdb2cf97351cff63beaa9d68a6273dcc42`
- `archive_url`: pointing to the v4.400 release zip
- `files`: mapping for OFL.txt and four TTF weights (Regular, Medium, SemiBold, Bold)
- `branch`: `master`
- No `config_yaml` field (override config.yaml is in google/fonts directory)

### Google Fonts Git History

Key commits in `ofl/harmattan/`:

1. **babc03259** - `hotfix-harmattan: v1.002 added (#969)` -- initial addition
2. **7028be6bb** - `Harmattan: v 2.000 added (#2533)` -- major update
3. **9130423d9** - `[gftools-packager] Harmattan: Version 4.000 added` -- v4.000 update
4. **159e763aa** - `Harmattan: Version 4.300 added` -- by Emma Marichal, Oct 30, 2024, referencing upstream commit `00b3f6eeb48170d46b0c56d386374dc79203bd2b`
5. **7697538e4** - `Harmattan: Version 4.400 added` -- by Emma Marichal, Sep 5, 2025, referencing upstream commit `b8d089bdb2cf97351cff63beaa9d68a6273dcc42`
6. **f6c68379a** - `Add override config.yaml for 50 font families` -- added override config.yaml

### Upstream Repository Verification

The upstream repo at `silnrsi/font-harmattan` is cached at `fontc_crater_cache/silnrsi/font-harmattan`.

- The referenced commit `b8d089bd` exists and is dated 2025-08-11. Its message: "Bump to v4.401. Regenerate ftml files."
- This commit is one commit after the `v4.400` tag (which points to `7fafda09`, dated 2025-08-08). The google/fonts commit says "Version 4.400 added" but references the post-tag bump to v4.401. This appears intentional as the commit includes regenerated font binaries.
- There are 8 additional commits after `b8d089bd` in the upstream repo (through 2026-01-12), none of which have been incorporated into google/fonts yet.

### Source Files

The upstream repo contains gftools-builder compatible sources:
- `source/Harmattan.designspace` -- designspace file with weight axis (400-700)
- `source/masters/Harmattan-Regular.ufo` -- Regular master
- `source/masters/Harmattan-Bold.ufo` -- Bold master

No `config.yaml` exists in the upstream repo itself. An override `config.yaml` was added to the google/fonts directory in commit `f6c68379a`:

```yaml
sources:
  - source/Harmattan.designspace
familyName: Harmattan
buildStatic: true
buildOTF: false
```

### Version Note

The METADATA.pb `archive_url` references `Harmattan-4.400.zip` from the v4.400 release, but the `commit` field references `b8d089bd` which is the v4.401 bump (one commit after v4.400). The fonts in google/fonts appear to be built from this post-tag commit, not the tag itself. This is consistent with SIL's workflow where the release tag and final build commit may differ slightly.

## Conclusion

The source block is complete. The repository URL, commit hash, archive URL, and file mappings are all present and verified. The override config.yaml exists in the google/fonts directory, so no `config_yaml` field is needed in METADATA.pb.

### Recommended METADATA.pb Source Block

No changes needed. Current source block is correct:

```
source {
  repository_url: "https://github.com/silnrsi/font-harmattan"
  commit: "b8d089bdb2cf97351cff63beaa9d68a6273dcc42"
  archive_url: "https://github.com/silnrsi/font-harmattan/releases/download/v4.400/Harmattan-4.400.zip"
  files {
    source_file: "Harmattan-4.400/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Harmattan-4.400/Harmattan-Regular.ttf"
    dest_file: "Harmattan-Regular.ttf"
  }
  files {
    source_file: "Harmattan-4.400/Harmattan-Medium.ttf"
    dest_file: "Harmattan-Medium.ttf"
  }
  files {
    source_file: "Harmattan-4.400/Harmattan-SemiBold.ttf"
    dest_file: "Harmattan-SemiBold.ttf"
  }
  files {
    source_file: "Harmattan-4.400/Harmattan-Bold.ttf"
    dest_file: "Harmattan-Bold.ttf"
  }
  branch: "master"
}
```
