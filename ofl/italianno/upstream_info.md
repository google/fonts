# Investigation: Italianno

## Summary

| Field | Value |
|-------|-------|
| Family Name | Italianno |
| Slug | italianno |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/italianno |
| Commit Hash | 3e3995ef5b90bd2b9dc587fb8f831f3a158cb95b |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/italianno"
  commit: "3e3995ef5b90bd2b9dc587fb8f831f3a158cb95b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Italianno-Regular.ttf"
    dest_file: "Italianno-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font was most recently updated in google/fonts in commit `c7039c870` ("Italianno: Version 1.100; ttfautohint (v1.8.3) added (#3379)", 2021-05-05). The commit body confirms:

> Italianno Version 1.100; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/italianno at commit https://github.com/googlefonts/italianno/commit/d183cfb030ba783dd91c010926e315afe33815d0.

The original onboarding commit was `d183cfb030ba783dd91c010926e315afe33815d0`. However, the current METADATA.pb shows commit `3e3995ef5b90bd2b9dc587fb8f831f3a158cb95b`.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/italianno`. The cached repo has **only one commit**: `3e3995ef5b90bd2b9dc587fb8f831f3a158cb95b` (2021-08-30, "original font file deleted" by Viviana Monsalve). The original commit `d183cfb` does **not** exist in the cached repository. This suggests the repository was recreated or its history was reset.

The single commit `3e3995ef` in the current repo appears to be a fresh setup that added all the project files: `.github/workflows/CI-static-ttf.yml`, `.gitignore`, `AUTHORS.txt`, `CONTRIBUTORS.txt`, `DESCRIPTION.en_us.html`, `OFL.txt`, font files in `fonts/`, `requirements.txt`, `sources/Italianno.glyphs`, and `sources/config.yml`.

**Source format**: The repository contains `sources/Italianno.glyphs` (a single Glyphs source file). A `config.yml` exists at `sources/config.yml`:
```yaml
sources:
  - Italianno.glyphs
familyName: "Italianno"
buildVariable: false
# autohintTTF: false
```

The commit `3e3995ef` in METADATA.pb is verified to exist in the cached repo. The `config_yaml: "sources/config.yml"` is correctly set and the file exists.

Note: Confidence is MEDIUM because the original onboarding commit (`d183cfb`) no longer exists. The current commit (`3e3995ef`) represents a fresh setup of the repository after a reset. The fonts in google/fonts were built from `d183cfb`, not `3e3995ef`.

## Conclusion

The source block is structurally complete. The `repository_url`, `commit`, and `config_yaml` are all set. The commit `3e3995ef` exists in the current (single-commit) repository. However, this commit is the result of a repository reset — the actual onboarding commit `d183cfb` no longer exists. The current state is acceptable since the single existing commit includes all source files and the `config.yml`.
