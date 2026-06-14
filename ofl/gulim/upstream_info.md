# Investigation Report: Gulim

## Summary

Gulim is a Korean gothic-style (sans-serif) font originally designed by HanYang I&C Co. and first shipped with Windows 95. It was onboarded to Google Fonts in May 2024 by Aaron Bell from the upstream repository `googlefonts/gulim`. The font sources are pre-compiled TTF files processed by a custom Python script (`process.py`), not standard gftools-builder sources (.glyphs/.ufo/.designspace). There is no `config.yaml` in the upstream repo, and creating a gftools-builder override config is not feasible because the build process is a custom Python pipeline that manipulates pre-existing TTF binaries. The existing source block in METADATA.pb is correct.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gulim                                                              |
| Repository URL     | https://github.com/googlefonts/gulim                               |
| Commit Hash        | 012723a8d5b6a6dc920330f26d165422c3014fd6                           |
| Config YAML        | None (custom Python build, not gftools-builder compatible)         |
| Status             | no_config_possible                                                 |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/gulim/METADATA.pb` contains a complete source block:
- `repository_url`: `https://github.com/googlefonts/gulim`
- `commit`: `012723a8d5b6a6dc920330f26d165422c3014fd6`
- `branch`: `main`
- Files mapping `fonts/ttf/hinted/gulim-Regular.ttf` to `Gulim-Regular.ttf` and `OFL.txt` to `OFL.txt`

### Git History in google/fonts

The family was onboarded in commit `bb74e2b08` (2024-05-15) by Aaron Bell with the message:
> "Gulim: Version 2.21 added"
> "Taken from the upstream repo https://github.com/googlefonts/gulim at commit https://github.com/googlefonts/gulim/commit/012723a8d5b6a6dc920330f26d165422c3014fd6."

Subsequent commits:
1. `bac646415` - Updated DESCRIPTION.en_us.html
2. `deaba5e50` (2024-06-21) - Deleted original `gulim-Regular.ttf` (lowercase filename)
3. `9ade71526` (2024-06-24) - "Other FB-related updates" by Aaron Bell: added `Gulim-Regular.ttf` (capitalized filename, 4,719,024 bytes vs original 4,718,604 bytes), updated METADATA.pb naming conventions
4. `7134cb9a8` (2024-06-28) - "Gulim Japanese deleted" by Viviana Monsalve: removed Japanese subset from METADATA.pb

The current binary (4,719,024 bytes) differs slightly from the upstream commit's binary (4,718,604 bytes), indicating some post-processing was done during the FB-related updates. However, the METADATA.pb still references the original upstream commit, which is appropriate since the upstream repo was not modified.

### Upstream Repository Analysis

The upstream repo at `googlefonts/gulim` (cached at `fontc_crater_cache/googlefonts/gulim`) has 11 total commits, with `012723a` being the HEAD (latest commit). The repo was created by Aaron Bell and contains:

- **Source files**: `sources/ttf/` directory containing pre-compiled TTF files (Gulim.ttf, GulimChe.ttf, Dotum.ttf, DotumChe.ttf)
- **Build system**: Custom `process.py` Python script and `Makefile` -- NOT gftools-builder
- **Output**: `fonts/ttf/hinted/`, `fonts/ttf/unhinted/`, `fonts/ttf/bitmap/`, and `fonts/ttc/` directories

The build process in `process.py`:
1. Takes pre-existing TTF files from `sources/ttf/`
2. Removes control character glyphs
3. Updates copyright and licensing metadata
4. Applies hinting via `gftools fix-hinting`
5. Creates TTC (TrueType Collection)
6. Subsets into bitmap, hinted, and unhinted variants

This is fundamentally different from gftools-builder workflow -- there are no `.glyphs`, `.ufo`, or `.designspace` source files. The "sources" are pre-compiled TTF binaries from the original HanYang release.

### Config YAML Assessment

A gftools-builder `config.yaml` is not applicable for this family. The build process requires a custom Python script that manipulates pre-existing TTF binaries. There are no gftools-builder compatible sources to reference.

## Conclusion

The existing METADATA.pb source block is correct and complete. The repository URL and commit hash are verified. No config.yaml can be created because the upstream repo uses a custom Python build pipeline with pre-compiled TTF sources rather than gftools-builder compatible source files.

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
    source_file: "fonts/ttf/hinted/gulim-Regular.ttf"
    dest_file: "Gulim-Regular.ttf"
  }
  branch: "main"
}
```

**Status**: no_config_possible
**Confidence**: HIGH
