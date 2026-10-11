# Investigation Report: Hubballi

## Summary

Hubballi is a Kannada and Latin sans-serif font designed by Erin McLaughlin. It was onboarded to Google Fonts on 2021-12-16 via gftools-packager by Yanone (Jan Gerner). The upstream repository is at `github.com/erinmclaughlin/Hubballi`. The METADATA.pb source block is complete with repository URL, commit hash, config_yaml path, and file mappings. The commit hash `e5c909be` in METADATA.pb matches the commit referenced in the google/fonts onboarding commit message and is the latest (HEAD) commit in the upstream repo. The builder.yaml file exists at the referenced commit. All data is consistent and verified.

## Key Findings

| Field | Value |
|---|---|
| Family Name | Hubballi |
| Repository URL | https://github.com/erinmclaughlin/Hubballi |
| Commit Hash | e5c909bedfc4a2395ea300f94acec0d245ff7635 |
| Config YAML | source/builder.yaml |
| Config Exists at Commit | Yes |
| Source Files | source/Hubballi-Regular.glyphs |
| Date Added | 2021-12-16 |
| Status | complete |
| Confidence | HIGH |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb file contains a complete source block:
- `repository_url`: `https://github.com/erinmclaughlin/Hubballi`
- `commit`: `e5c909bedfc4a2395ea300f94acec0d245ff7635`
- `config_yaml`: `source/builder.yaml`
- `branch`: `master`
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and fonts/ttf/Hubballi-Regular.ttf

### Google Fonts Commit History

The onboarding commit `29cde031b` (2021-12-16) by Yanone states:
> "[gftools-packager] Hubballi: Version 1.000; ttfautohint (v1.8.3) added"
> "Hubballi Version 1.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/erinmclaughlin/Hubballi at commit https://github.com/erinmclaughlin/Hubballi/commit/e5c909bedfc4a2395ea300f94acec0d245ff7635."

The commit hash in the onboarding message matches the METADATA.pb exactly.

A later commit `a6e5eec8e` (2025-09-18) added the source info to METADATA.pb, referencing the original onboarding commit.

### Upstream Repository

The repo at `github.com/erinmclaughlin/Hubballi` has commit `e5c909be` as its HEAD (latest commit, dated 2021-12-08):
- "Merge pull request #10 from yanone/master" — merging Yanone's preparation work

The merge brought in: builder.yaml, DESCRIPTION.en_us.html, updated source files, and compiled font binary. This is the commit used for onboarding.

The repo has extensive history going back to 2015 showing the complete development of the Kannada font.

### Config YAML (builder.yaml)

The file `source/builder.yaml` exists at commit `e5c909be` and contains:
```yaml
sources:
  - ../source/Hubballi-Regular.glyphs
outputDir: "../fonts"
buildTTF: true
buildOTF: false
buildWebfont: false
buildVariable: false
```

This is a static-only build (no variable font), building only TTF output from a single Glyphs source file.

### Binary Font Verification

The font file `fonts/ttf/Hubballi-Regular.ttf` exists at the referenced commit, and the file was introduced in commit `173f9119` (2021-11-04, "Latest binary"), which is part of the merge at `e5c909be`.

### Timeline

- 2015-07 to 2016-05: Initial development by Erin McLaughlin
- 2021-11-04: Yanone prepared the repo for Google Fonts (builder.yaml, binary, etc.)
- 2021-12-08: Merge PR #10 from yanone/master (commit `e5c909be`)
- 2021-12-16: Onboarded to google/fonts by Yanone via gftools-packager

## Conclusion

**Status: complete**

All source metadata is present and verified. The repository URL is correct, the commit hash matches both the onboarding message and the HEAD of the upstream repo, the config_yaml path points to a valid builder.yaml file, and file mappings are correct. No corrections needed. Confidence is HIGH because the gftools-packager onboarding message explicitly references this exact commit, the commit exists in the repo, and the font binary is present at that commit.
