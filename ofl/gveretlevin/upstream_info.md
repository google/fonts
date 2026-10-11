# Investigation Report: Gveret Levin

## Summary

Gveret Levin is a Hebrew handwriting font by AlefAlefAlef. It was added to Google Fonts on 2025-11-14 by Emma Marichal. The upstream repository at `https://github.com/AlefAlefAlef/gveret-levin` has a single commit which is correctly referenced in METADATA.pb. The repo includes a `sources/config.yaml` which is also correctly documented. The source block is fully complete.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gveret Levin                                                       |
| Designer           | AlefAlefAlef                                                       |
| Date Added         | 2025-11-14                                                         |
| Repository URL     | https://github.com/AlefAlefAlef/gveret-levin                      |
| Commit Hash        | b383a9c00863837b1b88b4d0365f43a304007dae                           |
| Config YAML        | sources/config.yaml (in upstream repo)                             |
| Source Files       | sources/GveretLevin.glyphs                                        |
| Status             | **complete**                                                       |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a comprehensive source block with:
- `repository_url`: `https://github.com/AlefAlefAlef/gveret-levin`
- `commit`: `b383a9c00863837b1b88b4d0365f43a304007dae`
- `config_yaml`: `sources/config.yaml`
- `branch`: `master`
- File mappings for `OFL.txt` and `fonts/ttf/GveretLevin-Regular.ttf`

### Git History in google/fonts

Key commits affecting `ofl/gveretlevin/`:

1. **abb852d9** (2025-11-14) - Emma Marichal: "Gveret Levin: Version 2.000; ttfautohint (v1.8.4.7-5d5b) added". The commit body explicitly states: "Taken from the upstream repo https://github.com/AlefAlefAlef/gveret-levin at commit b383a9c00863837b1b88b4d0365f43a304007dae."
2. **9a88e1c2** (2025-11-14) - Added article.
3. **6d1febd9** (2025-12-04) - Updated METADATA.pb.
4. **b6cb57e6** (2026-01-29) - Updated METADATA.pb.
5. **34926685** (2026-02-16) - Added `config_yaml` field to METADATA.pb.

### Upstream Repository Inspection

The upstream repo at `AlefAlefAlef/gveret-levin` contains a single commit:
- **b383a9c** (2025-11-14) by Avraham Cornfeld: "Merge pull request #8 from emmamarichal/master" with message "Gveret Levin on Google Fonts!"

This is the only commit in the local clone, confirming the hash is correct.

Repository contents:
- `sources/GveretLevin.glyphs` - Glyphs source file
- `sources/config.yaml` - gftools-builder config
- `fonts/ttf/GveretLevin-Regular.ttf` - Compiled TTF
- `fonts/otf/GveretLevin-Regular.otf` - Compiled OTF
- `fonts/webfonts/GveretLevin-Regular.woff2` - WOFF2
- `OFL.txt` - License

The `sources/config.yaml` contains:
```yaml
sources:
  - GveretLevin.glyphs
familyName: Gveret Levin
cleanUp: true
```

### Commit Hash Verification

The commit hash `b383a9c` is explicitly referenced in the google/fonts onboarding commit message by Emma Marichal. The upstream repo has only one commit, making this unambiguously correct.

## Conclusion

The source block for Gveret Levin is **complete**. All fields are correct: repository URL, commit hash, config_yaml path, branch, and file mappings.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/AlefAlefAlef/gveret-levin"
  commit: "b383a9c00863837b1b88b4d0365f43a304007dae"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/GveretLevin-Regular.ttf"
    dest_file: "GveretLevin-Regular.ttf"
  }
  branch: "master"
}
```

**Status**: complete
**Confidence**: HIGH
