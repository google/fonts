# Investigation Report: Gungsuh

## Summary

Gungsuh is a Korean myeongjo (brush)-style serif font originally from HanYang I&C Co., first shipped with Windows 95. It was onboarded to Google Fonts on 2024-05-15 from the `googlefonts/batang` upstream repository. The font is built from legacy TTF sources using a custom Python build script (`process.py`), not gftools-builder. No `.glyphs`, `.ufo`, or `.designspace` source files exist; gftools-builder config is not applicable.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Gungsuh |
| Designer           | HanYang I&C Co. |
| Repository URL     | https://github.com/googlefonts/batang |
| Commit Hash        | 6c1e09f93204c963881afbb4e25699095565f2e5 |
| Branch             | main |
| Config YAML        | N/A (no gftools-builder compatible sources) |
| Status             | **no_config_possible** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb already has a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/batang"
  commit: "6c1e09f93204c963881afbb4e25699095565f2e5"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/hinted/gungsuh-Regular.ttf"
    dest_file: "Gungsuh-Regular.ttf"
  }
  branch: "main"
}
```

### Git History in google/fonts

| Commit | Date | Description |
|--------|------|-------------|
| `b0d961c` | 2024-06-28 | GungsuhChe Japanese deleted (removed Japanese subset from both families) |
| `a8db7f2` | 2024-06-24 | Updated vertical metrics and metadata, renamed file to `Gungsuh-Regular.ttf` |
| `b6d74b7` | 2024-06-24 | Deleted `gungsuh-Regular.ttf` (old filename) |
| `c797e51` | 2024-06-04 | Updated DESCRIPTION.en_us.html |
| `8d96d42` | 2024-05-15 | **Initial onboarding** - "Gungsuh: Version 2.21 added" |

The onboarding commit `8d96d42` explicitly states: "Taken from the upstream repo https://github.com/googlefonts/batang at commit https://github.com/googlefonts/batang/commit/6c1e09f93204c963881afbb4e25699095565f2e5."

### Upstream Repository Analysis

The `googlefonts/batang` repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/batang/`. It has 16 total commits. The commit `6c1e09f` is the HEAD of the `main` branch ("updating names"), dated 2024-05-15.

**Source structure:**
- `sources/ttf/` - Contains the original pre-processing TTF files (~20MB each): `Batang.ttf`, `BatangChe.ttf`, `Gungsuh.ttf`, `GungsuhChe.ttf`
- `process.py` - Custom Python build script that processes original TTFs (removes control character glyphs, adjusts metrics, generates hinted/unhinted/bitmap variants)
- `Makefile` - Build automation using `process.py`
- `fonts/ttf/hinted/` - Output directory with processed TTFs (~6.5MB each)

**No gftools-builder compatible sources exist.** The fonts are derived from legacy binary TTFs via custom Python processing, not from `.glyphs`, `.ufo`, or `.designspace` sources. A `config.yaml` is neither present nor applicable.

### File Size Verification

| File | Upstream (at `6c1e09f`) | google/fonts (current) |
|------|------------------------|----------------------|
| gungsuh-Regular.ttf (hinted) | 6,582,408 bytes | N/A (replaced) |
| Gungsuh-Regular.ttf (current) | N/A | 6,582,836 bytes |

The current file in google/fonts (6,582,836 bytes) is slightly larger than the file from the upstream commit (6,582,408 bytes). This is because Aaron (the batang maintainer) updated vertical metrics and nbspace width on 2024-06-24 (commit `a8db7f2`), after the initial onboarding. The METADATA.pb still correctly references the upstream commit `6c1e09f`, as the vertical metrics fix was applied directly in google/fonts.

### Note on the `files` Block

The METADATA.pb references `fonts/ttf/hinted/gungsuh-Regular.ttf` as the source file. This is the processed/hinted output from `process.py`, not a compilable source. The source block uses the `files` mapping to copy this pre-built binary rather than building from source.

## Conclusion

The source block in METADATA.pb is correctly configured. The repository URL and commit hash are verified. No config.yaml is needed or possible because the upstream repo uses legacy TTF sources processed by a custom Python script, not gftools-builder compatible sources.

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
    source_file: "fonts/ttf/hinted/gungsuh-Regular.ttf"
    dest_file: "Gungsuh-Regular.ttf"
  }
  branch: "main"
}
```

**Status: no_config_possible** - Source block is complete. No gftools-builder config is applicable due to legacy TTF-only sources.
