# Investigation Report: Holtwood One SC

## Summary

Holtwood One SC is a display slab serif font by Vernon Adams, added to Google Fonts on 2011-05-04. The font was significantly updated in April 2024 by Emma Marichal, who created the upstream repo `googlefonts/HoltwoodFont`, rebuilt the font from `.glyphs` sources, and added it to google/fonts at commit `4e8e360`. The METADATA.pb already has a complete source block with repository URL, commit hash, branch, file mappings, and config_yaml path. This family is fully documented.

## Key Findings

| Field             | Value                                                      |
|-------------------|------------------------------------------------------------|
| Family Name       | Holtwood One SC                                            |
| Designer          | Vernon Adams                                               |
| Repository URL    | https://github.com/googlefonts/HoltwoodFont                |
| Commit Hash       | 4e8e360635badb21940ad39fa97a495bf879e89b                   |
| Config YAML       | sources/config.yaml                                        |
| Status            | complete                                                   |
| Confidence        | HIGH                                                       |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb has a comprehensive source block:

```
source {
  repository_url: "https://github.com/googlefonts/HoltwoodFont"
  commit: "4e8e360635badb21940ad39fa97a495bf879e89b"
  files {
    source_file: "fonts/ttf/HoltwoodOneSC-Regular.ttf"
    dest_file: "HoltwoodOneSC-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

All fields are present and correct: repository URL, commit hash, file mappings, branch, and config_yaml.

### Git History in google/fonts

The TTF file history for `ofl/holtwoodonesc/` shows:

1. **`95c283921`** (2024-04-25) - "Holtwood One SC: Version 1.100; ttfautohint (v1.8.4.7-5d5b) added" by Emma Marichal - This is the most recent update of the binary TTF file. The commit message explicitly states: "Taken from the upstream repo https://github.com/googlefonts/HoltwoodFont at commit https://github.com/googlefonts/HoltwoodFont/commit/4e8e360635badb21940ad39fa97a495bf879e89b."
2. The source block and config_yaml were added by this commit. The `config_yaml` field was later added by commit `19cdcec59` (Mar 2025, batch port from fontc_crater targets list).

### Upstream Repository Analysis

The upstream repo at `googlefonts/HoltwoodFont` is cached at `upstream_repos/fontc_crater_cache/googlefonts/HoltwoodFont/`. The repo contains exactly one commit:

- **`4e8e360`** (2024-04-25) - "update ofl" by Emma Marichal

This single commit created the entire repo with:
- `sources/HoltwoodOneSC.glyphs` - The Glyphs source file
- `sources/config.yaml` - gftools-builder configuration
- `fonts/ttf/HoltwoodOneSC-Regular.ttf` - Pre-built TTF
- `fonts/otf/HoltwoodOneSC-Regular.otf` - Pre-built OTF
- `fonts/webfonts/HoltwoodOneSC-Regular.woff2` - Pre-built WOFF2
- `documentation/1.png` - Sample image
- `AUTHORS.txt`, `CONTRIBUTORS.txt`, `OFL.txt`, `README.md`

### Config YAML in Upstream

The upstream `sources/config.yaml` contains:

```yaml
    sources:
        - HoltwoodOneSC.glyphs
    familyName: Holtwood One SC
    buildVariable: false
```

This is a valid gftools-builder config that builds from the `.glyphs` source as a static-only font.

### Commit Hash Verification

The commit hash `4e8e360635badb21940ad39fa97a495bf879e89b` in METADATA.pb matches:
- The only commit in the upstream repo
- The commit explicitly referenced in the google/fonts commit message for `95c283921`
- The TTF file at `fonts/ttf/HoltwoodOneSC-Regular.ttf` in the upstream repo is the same file copied to google/fonts

This is a straightforward verification since there is only one commit in the repo.

## Conclusion

**Status: complete** - This family is fully documented with all metadata fields present and verified. The repository URL, commit hash, file mappings, branch, and config_yaml are all correct in METADATA.pb. No changes needed.
