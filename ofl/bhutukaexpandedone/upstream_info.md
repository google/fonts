# Investigation Report: BhuTuka Expanded One

- **Family Name**: BhuTuka Expanded One
- **Slug**: bhutukaexpandedone
- **Designer**: Erin McLaughlin
- **Category**: SERIF / SLAB_SERIF / DISPLAY
- **Date Added**: 2022-01-21
- **Primary Script**: Gurmukhi
- **Model**: Claude Opus 4.6

## Source Metadata

| Field            | Value |
|------------------|-------|
| Repository URL   | https://github.com/erinmclaughlin/BhuTuka-Extended-One |
| Commit           | `ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6` |
| Config YAML      | `sources/builder.yaml` |
| Branch           | `master` |
| Status           | **complete** |
| Confidence       | **HIGH** |

## Investigation Details

### METADATA.pb Review

The METADATA.pb file contained a fully populated `source { }` block with `repository_url`, `commit`, `config_yaml`, `branch`, and `files` entries. The source block referenced `sources/builder.yaml` as the config file and mapped three files: `OFL.txt`, `DESCRIPTION.en_us.html`, and `fonts/ttf/BhuTukaExpandedOne-Regular.ttf`.

### Repository Verification

The upstream repository at https://github.com/erinmclaughlin/BhuTuka-Extended-One returned HTTP 200 and was confirmed accessible. The cached clone at `upstream_repos/fontc_crater_cache/erinmclaughlin/BhuTuka-Extended-One` was clean (no local modifications) and up to date with `origin/master`.

### Commit Verification

The referenced commit `ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6` was verified to exist in the upstream repository. It is a merge commit ("Merge pull request #4 from yanone/master") dated 2021-12-23, authored by Erin McLaughlin. This is the **only commit** in the repository, meaning it is the initial commit that set up the entire project.

The google/fonts onboarding commit `b52c85605` (PR #4222, merged 2022-01-28) explicitly referenced this commit in its message:

> "BhuTuka Expanded One Version 1.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/erinmclaughlin/BhuTuka-Extended-One at commit https://github.com/erinmclaughlin/BhuTuka-Extended-One/commit/ac2ad17bcd23da70b2c63a4ed794cbb7a7ebaac6."

### Binary Verification

The font binary `BhuTukaExpandedOne-Regular.ttf` in google/fonts matched the upstream binary at the referenced commit exactly:
- MD5: `69396f6ff67ed96e537b2f2138d2521c` (both files)

This confirmed the commit hash was correct and the binary was taken directly from the upstream repository without modification.

### Config YAML Verification

The file `sources/builder.yaml` existed at the referenced commit and contained valid gftools-builder configuration:

```yaml
sources:
  - BhuTukaExpandedOne-Regular.glyphs
outputDir: "../fonts"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

The config referenced the Glyphs source file `BhuTukaExpandedOne-Regular.glyphs`, which was present in the `sources/` directory. No local override config.yaml existed in the google/fonts family directory.

### google/fonts History

The font was onboarded via PR #4222, committed on 2022-01-28 by Yanone (Rosalie Wagner co-authored). The commit was created by `gftools-packager`. Subsequent commits to this family directory were metadata-only changes (upstream.yaml merge, source fields population, HTML formatting, stroke/classification data, primary script identification).

## Conclusion

All source metadata fields in METADATA.pb were verified as correct. The repository URL was accessible, the commit hash matched the onboarding commit (confirmed by both the gftools-packager message and binary MD5 comparison), and the config.yaml path pointed to a valid gftools-builder configuration in the upstream repo. No corrections were needed.
