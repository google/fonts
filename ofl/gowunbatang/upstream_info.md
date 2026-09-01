# Investigation: Gowun Batang

## Summary

Gowun Batang is a Korean serif typeface by Yanghee Ryu. It was onboarded to Google Fonts as Version 2.000 via PR #3524 (merged 2021-06-11) by Aaron Bell using gftools-packager. The upstream repository is at `yangheeryu/Gowun-Batang`, and the commit hash `4e73f5a` is explicitly referenced in the PR commit message. The METADATA.pb source block already has the correct repository URL, commit hash, file mappings, and branch. An override `config.yaml` already exists in the google/fonts family directory.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gowun Batang                                                       |
| Designer           | Yanghee Ryu                                                        |
| Repository URL     | https://github.com/yangheeryu/Gowun-Batang                        |
| Commit Hash        | 4e73f5a9a004927220354f4b68a4c720da538147                           |
| Config YAML        | Override config.yaml in google/fonts                               |
| Source Format       | .glyphs (inside sources/GowunBatang.zip)                          |
| Status             | complete                                                           |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Current State

The current METADATA.pb has a comprehensive source block:

```
source {
  repository_url: "https://github.com/yangheeryu/Gowun-Batang"
  commit: "4e73f5a9a004927220354f4b68a4c720da538147"
  files {
    source_file: "fonts/ttf/GowunBatang-Regular.ttf"
    dest_file: "GowunBatang-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/GowunBatang-Bold.ttf"
    dest_file: "GowunBatang-Bold.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

### Upstream Repository Analysis

- **Repository**: https://github.com/yangheeryu/Gowun-Batang
- **Cached at**: upstream_repos/fontc_crater_cache/yangheeryu/Gowun-Batang
- **Branches**: master only
- **Latest commit**: `4e73f5a` ("Batang ready to go!", 2021-06-10) by Aaron Bell

The repository contains:
- `sources/GowunBatang.zip` - Contains `GowunBatang.glyphs` (114 MB, merged Regular+Bold)
- `build.py` - Custom build script using glyphsLib, ufo2ft, fontTools
- `fonts/ttf/GowunBatang-Regular.ttf` and `fonts/ttf/GowunBatang-Bold.ttf` - Pre-built TTFs
- No `config.yaml` in upstream

### Onboarding History

The font was onboarded via PR #3524, merged 2021-06-11:
- **Commit**: `539f6c4bb` in google/fonts
- **Author**: Aaron Bell (aaronbell)
- **Message**: "Gowun Batang: Version 2.000 added (#3524)"
- **gftools-packager reference**: "Gowun Batang Version 2.000 taken from the upstream repo https://github.com/yangheeryu/Gowun-Batang.git at commit https://github.com/yangheeryu/Gowun-Batang/commit/4e73f5a9a004927220354f4b68a4c720da538147"

The commit hash `4e73f5a` is the latest (HEAD) commit in the upstream repo and matches the gftools-packager reference exactly. This is also the commit authored by Aaron Bell himself ("Batang ready to go!") on 2021-06-10, one day before the google/fonts merge on 2021-06-11.

### Config YAML Assessment

An override `config.yaml` already exists at `ofl/gowunbatang/config.yaml` in google/fonts:

```yaml
buildVariable: false
sources:
  - sources/GowunBatang.zip
```

This was added in commit `fa89220ae` ("sources info for Gowun Batang: Version 2.000 (PR #3524)", 2025-11-11).

The upstream repo uses a custom `build.py` script (not gftools-builder), so the override config.yaml in google/fonts is the correct approach. The source is a `.glyphs` file inside `GowunBatang.zip`.

### Commit Hash Verification

The commit `4e73f5a` is verified as correct:
- It is the HEAD commit on the master branch of the upstream repo
- It is explicitly referenced in the gftools-packager message in the google/fonts onboarding commit
- It was authored on 2021-06-10, one day before the google/fonts PR merge on 2021-06-11
- It was authored by Aaron Bell, who also submitted the google/fonts PR

## Conclusion

This family is fully complete. The METADATA.pb source block has the correct repository URL, commit hash, file mappings, and branch. An override `config.yaml` already exists in the google/fonts family directory.

### Current METADATA.pb Source Block (correct, no changes needed)

```
source {
  repository_url: "https://github.com/yangheeryu/Gowun-Batang"
  commit: "4e73f5a9a004927220354f4b68a4c720da538147"
  files {
    source_file: "fonts/ttf/GowunBatang-Regular.ttf"
    dest_file: "GowunBatang-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/GowunBatang-Bold.ttf"
    dest_file: "GowunBatang-Bold.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

**Status**: complete
**Confidence**: HIGH -- commit hash directly referenced by gftools-packager in the onboarding commit message, and it is the HEAD of the upstream repo.
