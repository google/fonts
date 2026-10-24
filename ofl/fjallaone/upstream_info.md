# Investigation Report: Fjalla One

## Summary

| Field | Value |
|-------|-------|
| **Family Name** | Fjalla One |
| **Designer** | Sorkin Type, Irina Smirnova |
| **License** | OFL |
| **Date Added** | 2012-10-27 |
| **Category** | Sans Serif |
| **Status** | complete |
| **Confidence** | HIGH |

## Upstream Repository

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/SorkinType/FjallaOne |
| **Commit** | `e5fcc44bb44b8a84debd0cc070bad1360cc91761` |
| **Branch** | main |
| **Config** | Override config.yaml in google/fonts |

## Source Block (current METADATA.pb)

```
source {
  repository_url: "https://github.com/SorkinType/FjallaOne"
  commit: "e5fcc44bb44b8a84debd0cc070bad1360cc91761"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/FjallaOne-Regular.ttf"
    dest_file: "FjallaOne-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation Details

### Repository Verification

The upstream repository at https://github.com/SorkinType/FjallaOne is valid and accessible. It is cached locally at `upstream_repos/fontc_crater_cache/SorkinType/FjallaOne/`.

The repository contains:
- **Source file**: `sources/FjallaOne.glyphs` (Glyphs format)
- **Pre-built binaries**: `fonts/ttf/FjallaOne-Regular.ttf`, `fonts/otf/FjallaOne-Regular.otf`, `fonts/webfonts/FjallaOne-Regular.woff2`
- **No config.yaml** at the referenced commit (was removed in commit `a3cf507`)

### Commit Hash Verification

The commit `e5fcc44bb44b8a84debd0cc070bad1360cc91761` is a merge commit dated 2023-03-03 ("Merge pull request #1 from emmamarichal/main"). This commit was explicitly referenced in the google/fonts PR #5980 commit message:

> "Fjalla One Version 1.002; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.25] taken from the upstream repo https://github.com/SorkinType/FjallaOne at commit https://github.com/SorkinType/FjallaOne/commit/e5fcc44bb44b8a84debd0cc070bad1360cc91761."

**Binary verification**: The TTF file at this commit (`fonts/ttf/FjallaOne-Regular.ttf`) has:
- MD5: `62263ebc6a5c779190b558e637620432`
- Size: 209,052 bytes

The binary in google/fonts (`ofl/fjallaone/FjallaOne-Regular.ttf`) has the **identical MD5 and size**, confirming the commit hash is correct.

### Google Fonts History

1. **Initial commit** (`90abd17b4`, 2015-03-07): Fjalla One was included in the initial import of the google/fonts repository.
2. **Version 1.001 update** (`69b4c4ac3`): ttfautohinted and version incremented (via PR #1126).
3. **Version 1.002 update** (`df49a552f`, 2023-03-08): Updated to Version 1.002 via PR #5980, submitted by Emma Marichal using gftools-packager. The binary was taken directly from the upstream repo at commit `e5fcc44`.
4. **Override config.yaml** (`3b645f8db`, 2025-03-10): Auto-generated override config.yaml added to google/fonts.
5. **Source info** (`79a8f4ea6` / `b70efca9b`, 2025-11-10): Source metadata enrichment commits.

### Config.yaml Status

The upstream repository originally had a `config.yaml` at `sources/config.yaml` (added in commit `51a4cb8`), but it was **removed** in commit `a3cf507` ("removed useless config.yaml + added caret for ligatures"). The original config was:

```yaml
sources:
  - FjallaOne.glyphs
axisOrder:
  - wght
familyName: FjallaOne
```

At the referenced commit `e5fcc44`, **no config.yaml exists** in the upstream repo.

An override `config.yaml` exists in the google/fonts family directory (`ofl/fjallaone/config.yaml`):

```yaml
buildVariable: false
sources:
  - sources/FjallaOne.glyphs
```

This override correctly references the Glyphs source file at the upstream repo root-relative path. Since the override exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb `source {}` block.

### Post-Reference Upstream Changes

Three commits exist after the referenced commit `e5fcc44`:

| Commit | Date | Description |
|--------|------|-------------|
| `a26598d` | 2023-03-15 | Add soft-dotted lookup (by moyogo) |
| `4a6aa64` | 2024-05-10 | Merge PR #2 from moyogo/softdotted |
| `24c2e5a` | 2024-05-10 | Minor corrections and missing tcomma below |

These changes modify `sources/FjallaOne.glyphs` (5,143 insertions, 4,349 deletions) and would need a separate review and QA process before being incorporated into Google Fonts.

## Conclusion

Fjalla One has a **complete** source block in METADATA.pb with a verified repository URL, correct commit hash (binary-verified), and a working override config.yaml in google/fonts. No changes needed.
