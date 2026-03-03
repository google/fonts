# Investigation: Kedebideri

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kedebideri |
| Slug | kedebideri |
| License Dir | ofl |
| Repository URL | https://github.com/silnrsi/font-kedebideri |
| Commit Hash | 4973b2e0258ef40acc0da3c2c1d155630faecc2c |
| Config YAML | none (SIL smith build system) |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/silnrsi/font-kedebideri"
  commit: "4973b2e0258ef40acc0da3c2c1d155630faecc2c"
  archive_url: "https://github.com/silnrsi/font-kedebideri/releases/download/v3.001/Kedebideri-3.001.zip"
  files {
    source_file: "Kedebideri-3.001/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Kedebideri-3.001/Kedebideri-Regular.ttf"
    dest_file: "Kedebideri-Regular.ttf"
  }
  ...
  branch: "main"
}
primary_language: "zag_Berf"
stroke: "SANS_SERIF"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `archive_url` but no `config_yaml`. The upstream repository `silnrsi/font-kedebideri` is cached at `upstream_repos/fontc_crater_cache/silnrsi/font-kedebideri`.

This is a SIL International font for the Zaghawa script (Beria). The `source/` directory contains:
- `Kedebideri.designspace` (Designspace format)
- `KedebideriAxis.designspace`
- `masters/` (UFO masters)
- `opentype/` (OpenType feature files)

The repository uses SIL's wscript/smith build system, not gftools-builder. No `config.yaml` exists in the repository. The commit hash `4973b2e` is recorded and corresponds to the v3.001 release.

The latest git log entry is `142f05a` ("Update copyright date to 2026..."), which is more recent than the recorded commit hash.

## Conclusion

The source block has repository URL and commit hash. However, the SIL smith build system is not compatible with gftools-builder, so no `config.yaml` is possible. Status is missing_config with the understanding that the build system incompatibility makes config.yaml creation infeasible.
