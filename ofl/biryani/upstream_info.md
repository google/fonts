# Investigation Report: Biryani

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Biryani |
| Designer | Dan Reynolds, Mathieu Reguer |
| License | OFL |
| Repository URL | https://github.com/typeoff/biryani |
| Commit | `6f7831d27b7458109cd88aceba28efeda057dadb` |
| Branch | master |
| **Config YAML** | Override in google/fonts |
| Date Added | 2015-04-22 |
| **Status** | complete |

## How URL Found

The repository URL `https://github.com/typeoff/biryani` was added by Simon Cozens in commit `46a7c0576` ("Add more upstreams (a,b)", January 2024). The typeoff GitHub organization is associated with Dan Reynolds, one of the font's designers.

## How Commit Determined

The commit hash `6f7831d27b7458109cd88aceba28efeda057dadb` was added by our project in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). This commit is the HEAD of the `master` branch in the upstream repo -- a merge commit titled "Merge pull request #5 from frankrolf/master" dated 2015-04-22.

### Rationale for using HEAD

Biryani was added to google/fonts in a pre-gftools-packager era (2015). There is no gftools-packager commit referencing a specific upstream commit. The upstream repo's full history is preserved (14 commits from 2014-10-05 to 2015-04-22), and the HEAD commit is the latest.

### Timeline analysis

- Upstream repo HEAD (`6f7831d`): 2015-04-22 -- fixes negative numbers in UFO files
- Last font update in google/fonts (`0212fe7f5`, PR #808): 2017-05-08 -- "biryani: v1.004 added"

The fonts in google/fonts are Version 1.004, but the upstream repo only goes up to Version 1.003 (`606c043`, 2015-03-08). This means the v1.004 binaries were likely compiled externally (by Marc Foley, PR #808 author) from sources that may have been modified beyond what's in the upstream repo, or the version was bumped during the compilation process.

## Config YAML Status

**Not found** -- No `config.yaml` or `config.yml` exists in the upstream repository.

The upstream repo structure is:
- `Source Files/Biryani 20150307.glyphs` -- Glyphs source file
- `Source Files/Biryani-Bold.ufo/` -- UFO source (Bold)
- `Source Files/Biryani-Light.ufo/` -- UFO source (Light)
- `Font Files/TTFs with ttautohints/` -- Pre-compiled TTF files
- `Font Files/OTFs/` -- Pre-compiled OTF files

The source files (Glyphs and UFO) are present but there is no gftools-builder configuration. The font file naming also differs between upstream (e.g., "DemiBold", "UltraLight", "Heavy") and google/fonts (e.g., "SemiBold", "ExtraLight", "Black"), suggesting the fonts were reprocessed.

No override config.yaml exists in the google/fonts family directory either.

## METADATA.pb Source Block

The current METADATA.pb in google/fonts has a minimal source block with only `repository_url`. The commit hash was added by our project but hasn't been merged yet. There are no file mappings or config_yaml fields.

## History

1. **2015-04-20**: Biryani initially added to google/fonts (commit `35b05c3cd`)
2. **2015-10-02**: File naming corrections (commit `72983290`)
3. **2015-10-05**: ExtraLight style updated (commit `d4f76456f`)
4. **2017-05-08**: Version 1.004 added (commit `0212fe7f5`, PR #808 by Marc Foley)
5. **2024-01-14**: repository_url added by Simon Cozens (commit `46a7c0576`)
6. **2025-03-17**: primary_script set to Deva (commit `8b70d4c34`)

## Verification

- [x] Repository URL is valid and accessible
- [x] Commit hash exists in upstream repo (HEAD of master)
- [x] Upstream repo contains source files (Glyphs, UFO)
- [ ] No config.yaml exists in upstream repo
- [ ] No override config.yaml in google/fonts family directory
- [ ] Font version mismatch: google/fonts has v1.004, upstream only has up to v1.003

## Confidence Level

**Medium** -- The repository URL is correct and the upstream contains the original source files. The commit hash is HEAD of master which is reasonable for a pre-packager font. However, the version mismatch (v1.004 in google/fonts vs v1.003 in upstream) suggests the fonts were modified externally before being added. The absence of config.yaml means this family cannot be rebuilt with gftools-builder without creating one.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - "Source Files/Biryani 20150307.glyphs"
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. Who compiled the v1.004 binaries? Marc Foley submitted PR #808 but the PR body was empty. Were the fonts compiled from the upstream sources with a version bump, or from a different source?
2. Should a config.yaml be created for this family? The Glyphs source is present, but the weight naming differs between upstream and google/fonts, which would need to be addressed in the config.
3. Is the upstream repo still actively maintained? The last commit is from 2015.
