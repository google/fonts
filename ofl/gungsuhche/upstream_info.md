# Investigation Report: GungsuhChe

## Summary

GungsuhChe is the monospace/half-width Latin variant of Gungsuh, a Korean myeongjo (brush)-style serif font from HanYang I&C Co. It was onboarded to Google Fonts on 2024-05-15 from the same `googlefonts/batang` upstream repository as Gungsuh. Like Gungsuh, it is built from legacy TTF sources using a custom Python build script, not gftools-builder. No config.yaml is applicable.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | GungsuhChe |
| Designer           | HanYang I&C Co. |
| Repository URL     | https://github.com/googlefonts/batang |
| Commit Hash        | 6c1e09f93204c963881afbb4e25699095565f2e5 |
| Branch             | main |
| Config YAML        | N/A (no gftools-builder compatible sources) |
| Status             | **no_config_possible** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/batang"
  commit: "6c1e09f93204c963881afbb4e25699095565f2e5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/hinted/gungsuhche-Regular.ttf"
    dest_file: "GungsuhChe-Regular.ttf"
  }
  branch: "main"
}
```

### Git History in google/fonts

| Commit | Date | Description |
|--------|------|-------------|
| `b0d961c` | 2024-06-28 | GungsuhChe Japanese deleted (removed Japanese subset from both families) |
| `841233a` | 2024-06-24 | Updating vertical metrics and metadata, renamed file to `GungsuhChe-Regular.ttf` |
| `bb58d98` | 2024-06-24 | Deleted `gungsuhche-Regular.ttf` (old filename) |
| `efc134a` | 2024-06-04 | Updated DESCRIPTION.en_us.html |
| `8354e82` | 2024-05-15 | **Initial onboarding** - "Gungsuhche: Version 2.21 added" |

The onboarding commit `8354e82` explicitly states: "Taken from the upstream repo https://github.com/googlefonts/batang at commit https://github.com/googlefonts/batang/commit/6c1e09f93204c963881afbb4e25699095565f2e5."

### Upstream Repository Analysis

The `googlefonts/batang` repo is the same upstream repo used by Gungsuh, Batang, and BatangChe -- all four typefaces from the same Korean font collection. The repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/batang/`.

Commit `6c1e09f` is the HEAD of the `main` branch, dated 2024-05-15 ("updating names"). This commit added all files under `fonts/ttf/hinted/`, including `gungsuhche-Regular.ttf`.

**Source structure:**
- `sources/ttf/GungsuhChe.ttf` - Original pre-processing TTF (~16MB)
- `process.py` - Custom Python script that processes the original TTFs (removes control characters, adjusts metrics, generates hinted/unhinted/bitmap variants)
- `fonts/ttf/hinted/gungsuhche-Regular.ttf` - Processed output (~6.5MB)

**No gftools-builder compatible sources** (`.glyphs`, `.ufo`, `.designspace`) exist in the repository.

### File Size Verification

| File | Upstream (at `6c1e09f`) | google/fonts (current) |
|------|------------------------|----------------------|
| gungsuhche-Regular.ttf (hinted) | 6,577,784 bytes | N/A (replaced) |
| GungsuhChe-Regular.ttf (current) | N/A | 6,578,224 bytes |

The current file (6,578,224 bytes) is slightly larger than the original from the upstream commit (6,577,784 bytes), because of the vertical metrics update applied directly in google/fonts on 2024-06-24 (commit `841233a`). The METADATA.pb correctly still references the original upstream commit.

### Relationship to Gungsuh

GungsuhChe and Gungsuh share the same upstream repository (`googlefonts/batang`), the same commit hash, and the same build process. The only difference is GungsuhChe uses monospace/half-width Latin characters while Gungsuh uses proportional Latin characters.

## Conclusion

The source block in METADATA.pb is correctly configured. The repository URL and commit hash are verified. No config.yaml is needed or applicable because the upstream repo uses legacy TTF sources processed by a custom Python script.

### Recommended METADATA.pb Source Block

No changes needed. The current source block is correct:

```
source {
  repository_url: "https://github.com/googlefonts/batang"
  commit: "6c1e09f93204c963881afbb4e25699095565f2e5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/hinted/gungsuhche-Regular.ttf"
    dest_file: "GungsuhChe-Regular.ttf"
  }
  branch: "main"
}
```

**Status: no_config_possible** - Source block is complete. No gftools-builder config is applicable due to legacy TTF-only sources.
