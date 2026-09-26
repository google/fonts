# Investigation: Gowun Dodum

## Summary

Gowun Dodum is a Korean humanist sans-serif typeface by Yanghee Ryu. It was onboarded to Google Fonts as Version 2.000 via PR #3523 (merged 2021-06-11) by Aaron Bell using gftools-packager. The upstream repository is at `yangheeryu/Gowun-Dodum`, and the commit hash `6d9ef10` is explicitly referenced in the PR commit message. The METADATA.pb source block already has the correct repository URL, commit hash, file mappings, and branch. An override `config.yaml` already exists in the google/fonts family directory.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gowun Dodum                                                        |
| Designer           | Yanghee Ryu                                                        |
| Repository URL     | https://github.com/yangheeryu/Gowun-Dodum                         |
| Commit Hash        | 6d9ef10fc745cf3b0a4aba02dad1c740f94d029b                           |
| Config YAML        | Override config.yaml in google/fonts                               |
| Source Format       | .glyphs (sources/GowunDodum.glyphs)                               |
| Status             | complete                                                           |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Current State

The current METADATA.pb has a comprehensive source block:

```
source {
  repository_url: "https://github.com/yangheeryu/Gowun-Dodum"
  commit: "6d9ef10fc745cf3b0a4aba02dad1c740f94d029b"
  files {
    source_file: "fonts/ttf/GowunDodum-Regular.ttf"
    dest_file: "GowunDodum-Regular.ttf"
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

- **Repository**: https://github.com/yangheeryu/Gowun-Dodum
- **Cached at**: upstream_repos/fontc_crater_cache/yangheeryu/Gowun-Dodum
- **Branches**: master only
- **Latest commit**: `6d9ef10` ("Updating for GF", 2021-06-10) by Aaron Bell

The repository contains:
- `sources/GowunDodum.glyphs` - Glyphs source file (52 MB)
- `build.py` - Custom build script using glyphsLib, ufo2ft, fontTools
- `fonts/ttf/GowunDodum-Regular.ttf` - Pre-built TTF
- No `config.yaml` in upstream

### Onboarding History

The font was onboarded via PR #3523, merged 2021-06-11:
- **Commit**: `16a2143d6` in google/fonts
- **Author**: Aaron Bell (aaronbell)
- **Message**: "Gowun Dodum: Version 2.000 added (#3523)"
- **gftools-packager reference**: "Gowun Dodum Version 2.000 taken from the upstream repo https://github.com/yangheeryu/Gowun-Dodum.git at commit https://github.com/yangheeryu/Gowun-Dodum/commit/6d9ef10fc745cf3b0a4aba02dad1c740f94d029b"

The commit hash `6d9ef10` is the latest (HEAD) commit in the upstream repo and matches the gftools-packager reference exactly. This is also the commit authored by Aaron Bell himself ("Updating for GF") on 2021-06-10, one day before the google/fonts merge on 2021-06-11. In that commit, Aaron prepared the font for Google Fonts submission: created a build script, set GASP to smoothing, added DESCRIPTION.en_us.html, and made a slight modification to the ogonek character.

### Config YAML Assessment

An override `config.yaml` already exists at `ofl/gowundodum/config.yaml` in google/fonts:

```yaml
buildVariable: false
sources:
  - sources/GowunDodum.glyphs
```

This was added in commit `144713201` ("sources info for Gowun Dodum: Version 2.000 (PR #3523)", 2025-11-11).

The upstream repo uses a custom `build.py` script (not gftools-builder), so the override config.yaml in google/fonts is the correct approach. The source is a `.glyphs` file directly in the sources directory (not zipped, unlike Gowun Batang).

### Commit Hash Verification

The commit `6d9ef10` is verified as correct:
- It is the HEAD commit on the master branch of the upstream repo
- It is explicitly referenced in the gftools-packager message in the google/fonts onboarding commit
- It was authored on 2021-06-10, one day before the google/fonts PR merge on 2021-06-11
- It was authored by Aaron Bell, who also submitted the google/fonts PR

## Conclusion

This family is fully complete. The METADATA.pb source block has the correct repository URL, commit hash, file mappings, and branch. An override `config.yaml` already exists in the google/fonts family directory.

### Current METADATA.pb Source Block (correct, no changes needed)

```
source {
  repository_url: "https://github.com/yangheeryu/Gowun-Dodum"
  commit: "6d9ef10fc745cf3b0a4aba02dad1c740f94d029b"
  files {
    source_file: "fonts/ttf/GowunDodum-Regular.ttf"
    dest_file: "GowunDodum-Regular.ttf"
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
