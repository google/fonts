# Investigation Report: GulimChe

## Summary

GulimChe is the monospace/half-width Latin variant of the Gulim Korean gothic-style font, originally designed by HanYang I&C Co. It shares the same upstream repository (`googlefonts/gulim`) as Gulim. It was onboarded to Google Fonts in May 2024 by Aaron Bell. Like Gulim, the font sources are pre-compiled TTF files processed by a custom Python script, not standard gftools-builder sources. The existing source block in METADATA.pb is correct.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | GulimChe                                                           |
| Repository URL     | https://github.com/googlefonts/gulim                               |
| Commit Hash        | 012723a8d5b6a6dc920330f26d165422c3014fd6                           |
| Config YAML        | None (custom Python build, not gftools-builder compatible)         |
| Status             | no_config_possible                                                 |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/gulimche/METADATA.pb` contains a complete source block:
- `repository_url`: `https://github.com/googlefonts/gulim`
- `commit`: `012723a8d5b6a6dc920330f26d165422c3014fd6`
- `branch`: `main`
- Files mapping `fonts/ttf/hinted/gulimche-Regular.ttf` to `GulimChe-Regular.ttf` and `OFL.txt` to `OFL.txt`

### Git History in google/fonts

The family was onboarded in commit `c5a9e0e8e` (2024-05-15) by Aaron Bell with the message:
> "Gulimche: Version 2.21 added"
> "Taken from the upstream repo https://github.com/googlefonts/gulim at commit https://github.com/googlefonts/gulim/commit/012723a8d5b6a6dc920330f26d165422c3014fd6."

Subsequent commits:
1. `be05c0244` - Updated DESCRIPTION.en_us.html
2. `4d6e0685d` (2024-06-21) - Deleted original `gulimche-Regular.ttf` (lowercase filename)
3. `a633debf8` (2024-06-24) - "Updating metadata and vertical metrics" by Aaron Bell: added `GulimChe-Regular.ttf` (capitalized filename, 4,711,736 bytes vs original 4,711,304 bytes), updated METADATA.pb naming conventions
4. `7b414500c` (2024-06-28) - "Gulimche Japanese deleted" by Viviana Monsalve: removed Japanese subset from METADATA.pb

The current binary (4,711,736 bytes) differs slightly from the upstream commit's binary (4,711,304 bytes), indicating post-processing was done during the metadata/vertical metrics updates. However, the METADATA.pb still references the original upstream commit, which is appropriate.

### Upstream Repository Analysis

GulimChe shares the same upstream repo as Gulim: `googlefonts/gulim` (cached at `fontc_crater_cache/googlefonts/gulim`). The repository contains four font families built from the same source:
- Gulim (proportional Latin)
- GulimChe (monospace/half-width Latin)
- Dotum (proportional Latin, different style)
- DotumChe (monospace/half-width Latin, different style)

The commit `012723a` is the HEAD (latest) of the repository. The source TTF files are at `sources/ttf/GulimChe.ttf` and the processed output at `fonts/ttf/hinted/gulimche-Regular.ttf`.

### Config YAML Assessment

Same as Gulim: a gftools-builder `config.yaml` is not applicable. The build process uses a custom `process.py` Python script that manipulates pre-compiled TTF binaries. There are no `.glyphs`, `.ufo`, or `.designspace` sources.

## Conclusion

The existing METADATA.pb source block is correct and complete. The repository URL, commit hash, and file mappings are all verified. Both Gulim and GulimChe share the same upstream repo and commit, which is expected since they are built from the same source collection.

### Recommended METADATA.pb Source Block

The current source block is correct as-is:

```
source {
  repository_url: "https://github.com/googlefonts/gulim"
  commit: "012723a8d5b6a6dc920330f26d165422c3014fd6"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/hinted/gulimche-Regular.ttf"
    dest_file: "GulimChe-Regular.ttf"
  }
  branch: "main"
}
```

**Status**: no_config_possible
**Confidence**: HIGH
