# Investigation Report: Glory

## Summary

Glory is a sans-serif variable font family designed by Robert Leuschke, added to Google Fonts on 2021-06-17. The upstream repository is `googlefonts/glory` on GitHub. The METADATA.pb source block is already complete with the correct repository URL, commit hash, branch, config path, and file mappings. No changes are needed.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Glory                                                              |
| Designer          | Robert Leuschke                                                    |
| Date Added        | 2021-06-17                                                         |
| Repository URL    | https://github.com/googlefonts/glory                               |
| Commit Hash       | 76ea446c0499989af653f75c1cbd80447ef955d6                           |
| Branch            | master                                                             |
| Config Path       | sources/config.yml                                                 |
| Source Files      | Glory.glyphs, Glory-Italic.glyphs (in sources/)                    |
| Status            | **complete**                                                       |
| Confidence        | **HIGH**                                                           |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a fully populated `source { }` block with:
- `repository_url`: `https://github.com/googlefonts/glory`
- `commit`: `76ea446c0499989af653f75c1cbd80447ef955d6`
- `branch`: `master`
- `config_yaml`: `sources/config.yml`
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and both variable font files

### Onboarding History in google/fonts

The font was onboarded via commit `e311a15b7` (PR #3553) on 2021-06-22 by Viviana Monsalve:
- Commit message: "Glory: Version 1.011 added"
- Explicitly references upstream repo `https://github.com/googlefonts/glory` at commit `76ea446c0499989af653f75c1cbd80447ef955d6`
- Used gftools-packager for onboarding

Subsequent commits in google/fonts for this family:
- `cd0053a20` — OFL.txt update (2021-06-22)
- `659cb68b2` — DESCRIPTION.en_us.html update (PR #3738)
- Various metadata batch updates (language support, stroke/classification)
- `19cdcec59` — fontc_crater targets batch
- `85b768b39` — DESCRIPTION update

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/googlefonts/glory/` confirms:
- Remote URL: `https://github.com/googlefonts/glory`
- Commit `76ea446` exists and is the HEAD of `master` branch (the latest commit)
- Commit message: "copyright fix on italics" dated 2021-06-17
- The commit is 5 days before the google/fonts merge (2021-06-22), which is consistent

### Config and Source Files

At commit `76ea446`:
- `sources/config.yml` exists with valid gftools-builder configuration
- Sources: `Glory.glyphs` and `Glory-Italic.glyphs`
- Config specifies `axisOrder: [wght, ital]` and `familyName: "Glory"`
- Variable font outputs: `Glory[wght].ttf` and `Glory-Italic[wght].ttf`

### Commit Hash Cross-Verification

The commit hash `76ea446` in METADATA.pb matches exactly what the gftools-packager commit message references. The commit is HEAD of master, meaning the entire repo history was used at onboarding. The upstream commit date (2021-06-17) predates the google/fonts merge date (2021-06-22) by 5 days, which is a normal timeline.

## Conclusion

The Glory source block in METADATA.pb is complete and accurate. All fields (repository_url, commit, branch, config_yaml, file mappings) are correctly set. No changes are needed.

### Current METADATA.pb Source Block (no changes needed)

```
source {
  repository_url: "https://github.com/googlefonts/glory"
  commit: "76ea446c0499989af653f75c1cbd80447ef955d6"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Glory-Italic[wght].ttf"
    dest_file: "Glory-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Glory[wght].ttf"
    dest_file: "Glory[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

**Status: complete**
