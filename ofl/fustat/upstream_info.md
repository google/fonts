# Investigation Report: Fustat

## Summary

Fustat is a variable-weight Arabic/Latin sans-serif family designed by Mohamed Gaber, Laura Garcia Mut, and engineered by Khaled Hosny. It was first onboarded to Google Fonts on 2024-06-05 (v1.007) and updated to v1.010 on 2025-05-08. The upstream repository is at `https://github.com/Kief-Type-Foundry/Fustat` and the METADATA.pb already has a complete and correct source block with repository URL, commit hash, config_yaml path, archive_url, and file mappings.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Fustat |
| Repository URL    | https://github.com/Kief-Type-Foundry/Fustat |
| Commit Hash       | `642499b606f79bc6c25e63a4f8335a40afd96a13` |
| Config YAML       | `sources/config.yaml` (in upstream repo) |
| Source Files      | `sources/Fustat.glyphspackage` |
| Status            | **complete** |
| Confidence        | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb already contains a comprehensive source block:
- `repository_url`: `https://github.com/Kief-Type-Foundry/Fustat`
- `commit`: `642499b606f79bc6c25e63a4f8335a40afd96a13`
- `archive_url`: Release download URL for v1.010
- `config_yaml`: `sources/config.yaml`
- `branch`: `main`
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and the variable font binary

### Git History in google/fonts

- `82351ff2e` (2024-06-05): Initial onboarding as v1.007, taken from upstream commit `3b33a70591...` by Yanone.
- `6bfb6e6b5` (2025-05-08): Updated to v1.010, taken from upstream commit `642499b606...` by Yanone. Resolves issue #8302.
- `19cdcec59` (2025-03-31): Batch port of fontc_crater target info added source block details.

### Upstream Repository Verification

The upstream repo is cached at `upstream_repos/fontc_crater_cache/Kief-Type-Foundry/Fustat/`. Findings:
- Remote URL confirmed: `https://github.com/Kief-Type-Foundry/Fustat`
- Commit `642499b` ("Fustat 1.010", 2025-05-08) is the HEAD commit and matches the METADATA.pb reference.
- The commit was authored by Khaled Hosny and modifies `sources/Fustat.glyphspackage/fontinfo.plist` plus documentation images.
- `sources/config.yaml` exists at this commit and contains:
  ```yaml
  familyName: Fustat
  sources:
    - Fustat.glyphspackage
  buildStatic: false
  ```
- Source file `sources/Fustat.glyphspackage` is present (Glyphs package format, gftools-buildable).

### Commit Hash Verification

The commit message in google/fonts explicitly references `642499b606f79bc6c25e63a4f8335a40afd96a13`. The upstream commit is dated 2025-05-08, same day as the google/fonts commit. The commit is the HEAD of the upstream repo. This is consistent and verified.

## Conclusion

The METADATA.pb source block for Fustat is already complete and correct. No changes are needed.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/Kief-Type-Foundry/Fustat"
  commit: "642499b606f79bc6c25e63a4f8335a40afd96a13"
  archive_url: "https://github.com/Kief-Type-Foundry/Fustat/releases/download/v1.010/Fustat-v1.010.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Fustat[wght].ttf"
    dest_file: "Fustat[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: HIGH
