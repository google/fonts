# Bayon - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bayon |
| Repository URL | https://github.com/danhhong/Bayon |
| Commit Hash | 1749b1d8a8321d4294aae0f73ebb473535c39aee |
| Config YAML | Source/builder.yaml |
| Status | complete |
| Category | SANS_SERIF |
| Designer | Danh Hong |
| Date Added | 2011-03-02 |
| Primary Script | Khmr (Khmer) |

## How the Repository URL Was Found

The repository URL was recorded directly in the gftools-packager commit message when the font was updated. The commit `b95081fc5` in google/fonts ("Bayon: Version 8.001; ttfautohint (v1.8.3) added", PR #3498, September 2021) explicitly states:

> "Bayon Version 8.001; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/danhhong/Bayon.git at commit https://github.com/danhhong/Bayon/commit/1749b1d8a8321d4294aae0f73ebb473535c39aee."

The METADATA.pb `source` block also contains the repository URL.

## How the Commit Hash Was Determined

The commit hash `1749b1d8a8321d4294aae0f73ebb473535c39aee` was explicitly referenced in the gftools-packager commit message and PR #3498 body. The PR was authored by Yanone (Jan Gerner) and co-authored by Rosalie Wagner.

The commit in the upstream repo is titled "Merge pull request #1 from yanone/master", confirming it was the result of Yanone's work to update the Bayon font.

The font binary was last updated in google/fonts by this commit (`b95081fc5`) on September 8, 2021.

## Config YAML Status

**config.yaml exists** as `Source/builder.yaml` at the recorded commit. Its contents:

```yaml
sources:
  - Bayon.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

This is a valid gftools-builder configuration pointing to `Bayon.glyphs` as the source, building static TTF only (no variable font, no OTF, no webfont).

The METADATA.pb `source` block correctly references `config_yaml: "Source/builder.yaml"`.

## Verification

- **Repository exists**: Yes, cached at `upstream_repos/fontc_crater_cache/danhhong/Bayon/`
- **Commit exists**: Yes, `1749b1d` confirmed ("Merge pull request #1 from yanone/master")
- **Config YAML exists at commit**: Yes, `Source/builder.yaml` is present and valid
- **Commit hash matches PR reference**: Yes, both the PR body and merge commit message reference `1749b1d8a8321d4294aae0f73ebb473535c39aee`
- **Source block in METADATA.pb**: Complete with repository_url, commit, config_yaml, branch, and file mappings
- **Font files mapped**: `Release/ttf/Bayon-Regular.ttf` -> `Bayon-Regular.ttf`

## Confidence Level

**High** - All data is fully verified. The commit hash was explicitly referenced by the gftools-packager in both the commit message and PR body. The config.yaml exists at the recorded commit. The source block is complete.

## Open Questions

None. This family is fully documented and verified.
