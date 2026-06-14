# Investigation Report: Graduate

## Summary

Graduate is a Latin slab-serif/display font by Eduardo Tunni, available in a single Regular weight. It was originally added to Google Fonts in its initial commit (2012-03-14) and later updated via PR #7623 by Emma Marichal on 2024-05-01, which added the source block pointing to https://github.com/etunni/graduate at commit d6031c4. The upstream repo contains a .glyphs source file and a config.yaml for gftools-builder. The METADATA.pb source block is already complete.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Graduate |
| Designer          | Eduardo Tunni |
| Repository URL    | https://github.com/etunni/graduate |
| Commit Hash       | d6031c4ce60208e8e68f5e4dee771420d22c3815 |
| Branch            | master |
| Config YAML       | sources/config.yaml |
| Date Added        | 2012-03-14 |
| Status            | **complete** |
| Confidence        | HIGH |

## Investigation Details

### Onboarding and Update History

Graduate was part of the initial commit of the google/fonts repository (`90abd17b4` dated 2012). It was subsequently updated via PR #7623 ("Graduate: Version 1.100; ttfautohint (v1.8.4.7-5d5b) added") authored by Emma Marichal and merged on 2024-05-01. The PR body states:

> "Taken from the upstream repo https://github.com/etunni/graduate at commit https://github.com/etunni/graduate/commit/d6031c4ce60208e8e68f5e4dee771420d22c3815."

This update (commit `d0b20c8a1` in google/fonts) added the source block to METADATA.pb, updated the font binary from 22,732 bytes to 59,296 bytes, and updated the OFL and description files.

The `config_yaml` field was later added by commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list") on 2025-03-31.

### Upstream Repository Analysis

The upstream repository `etunni/graduate` contains:

- `sources/Graduate.glyphs` - Glyphs source file (296,812 bytes)
- `sources/config.yaml` - gftools-builder configuration
- `fonts/ttf/Graduate-Regular.ttf` - Pre-built TTF font
- `old/Graduate-Regular.otf.ufo` - Legacy UFO source
- `documentation/` - Documentation files
- `OFL.txt`, `AUTHORS.txt`, `CONTRIBUTORS.txt`, `README.md`, `requirements.txt`

The `config.yaml` content:
```yaml
    sources:
        - graduate.glyphs
    familyName: Graduate
    buildVariable: false
```

**Note on case sensitivity**: The config.yaml references `graduate.glyphs` (lowercase) but the actual file is `Graduate.glyphs` (uppercase G). This works on case-insensitive filesystems (macOS) but could be an issue on case-sensitive systems (Linux). Since this was already successfully used in the google/fonts update pipeline, it appears to work in the Google Fonts build environment.

### Commit History

The upstream repo has a relatively short history, restructured by Emma Marichal in April 2024:

- `d6031c4` (2024-04-28) - "Merge pull request #2 from emmamarichal/master" (Update OFL) -- **referenced commit**
- `77d89ff` (2024-04-26) - "Update OFL"
- `44c6955` (2024-04-25) - "Merge pull request #1 from emmamarichal/master"
- `03a6fd2` through `481e988` (2024-04-25) - Series of commits adding .glyphs source, config.yaml, font info updates, caret anchors, cleaning old files
- `e952c4a` (2013-12-30) - "Adobe Latin 3 encoding" -- original commit

The referenced commit `d6031c4` is the latest commit (HEAD) on the master branch, which is a merge commit updating the OFL license.

### Source Block Verification

The current METADATA.pb source block on main includes:
- `repository_url`: https://github.com/etunni/graduate -- **correct**
- `commit`: d6031c4ce60208e8e68f5e4dee771420d22c3815 -- **correct** (HEAD of master)
- `files` mapping: fonts/ttf/Graduate-Regular.ttf and OFL.txt -- **correct**
- `branch`: master -- **correct**
- `config_yaml`: sources/config.yaml -- **correct** (exists in upstream repo)

All fields are verified and accurate.

## Conclusion

Graduate's METADATA.pb source block is already complete and correct. The upstream repo at `etunni/graduate` contains a .glyphs source and config.yaml at the referenced commit `d6031c4`. No changes are needed.

### Current METADATA.pb Source Block (already correct)

```
source {
  repository_url: "https://github.com/etunni/graduate"
  commit: "d6031c4ce60208e8e68f5e4dee771420d22c3815"
  files {
    source_file: "fonts/ttf/Graduate-Regular.ttf"
    dest_file: "Graduate-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```
