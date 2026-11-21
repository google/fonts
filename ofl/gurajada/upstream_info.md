# Investigation Report: Gurajada

## Summary

Gurajada is a Telugu sans-serif font designed by Purushoth Kumar Guttula. It was added to Google Fonts on 2015-01-08 as part of the initial commit of the google/fonts repository. The upstream repository at `https://github.com/appajid/gurajada` contains a single commit with SFD and UFO sources. The source block in METADATA.pb is already complete, with the correct repository URL, commit hash, and an override config.yaml in google/fonts.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gurajada                                                           |
| Designer           | Purushoth Kumar Guttula                                            |
| Date Added         | 2015-01-08                                                         |
| Repository URL     | https://github.com/appajid/gurajada                                |
| Commit Hash        | 47d49279bffcb4cebab2dca10f8d7b20ff5230a2                           |
| Config YAML        | Override config.yaml in google/fonts (not in upstream repo)        |
| Source Files       | Gurajada.ufo, Gurajada.sfd                                        |
| Status             | **complete**                                                       |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a source block with:
- `repository_url`: `https://github.com/appajid/gurajada`
- `commit`: `47d49279bffcb4cebab2dca10f8d7b20ff5230a2`

No `config_yaml` field is set in METADATA.pb, which is correct because an override config.yaml exists in the google/fonts family directory.

### Git History in google/fonts

Key commits affecting `ofl/gurajada/`:

1. **90abd17b** (2015-03-07) - Initial commit of the google/fonts repository, which included Gurajada among many other families.
2. **474a446c** (2024-01-14) - Simon Cozens added the `source { repository_url }` block.
3. **fc356629** (2025-11-07) - Felipe Sanches added the commit hash and created the override config.yaml. The commit message references the initial commit as the source.

### Upstream Repository Inspection

The upstream repo at `appajid/gurajada` contains a single commit:
- **47d4927** (2014-11-26) by appajid: "updated copyright & version, no latin characters"

This is the only commit in the entire repository, making it unambiguously the correct onboarding commit.

Source files present:
- `Gurajada.sfd` - FontForge SFD source file
- `Gurajada.ufo/` - UFO source directory (contains fontinfo.plist, glyphs, kerning.plist, lib.plist, metainfo.plist)
- `OFL.txt` - License

No `config.yaml` exists in the upstream repo. An override config.yaml was created in the google/fonts directory with:
```yaml
buildVariable: false
sources:
  - Gurajada.ufo
```

### Commit Hash Verification

Since the upstream repo has only one commit (`47d4927`), the commit hash in METADATA.pb is trivially correct. The font was part of the initial google/fonts repository commit in March 2015, and the upstream commit predates that (November 2014).

## Conclusion

The source block for Gurajada is **complete**. The repository URL and commit hash are correct, and an override config.yaml properly references the UFO source.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/appajid/gurajada"
  commit: "47d49279bffcb4cebab2dca10f8d7b20ff5230a2"
}
```

(Override config.yaml in google/fonts family directory handles the build configuration.)

**Status**: complete
**Confidence**: HIGH
