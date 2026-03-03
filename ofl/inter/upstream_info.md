# Investigation: Inter

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inter |
| Slug | inter |
| License Dir | ofl |
| Repository URL | https://www.github.com/rsms/inter |
| Commit Hash | 66647c0bbbe41a850d79d9c76fb13add3378940f |
| Config YAML | override config.yaml in google/fonts (ofl/inter/config.yaml) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://www.github.com/rsms/inter"
  commit: "66647c0bbbe41a850d79d9c76fb13add3378940f"
  archive_url: "https://github.com/rsms/inter/files/15438431/Inter-4.1-GoogleFonts.zip"
  files {
    source_file: "Inter[opsz,wght].ttf"
    dest_file: "Inter[opsz,wght].ttf"
  }
  files {
    source_file: "Inter-Italic[opsz,wght].ttf"
    dest_file: "Inter-Italic[opsz,wght].ttf"
  }
  branch: "master"
}
```

## Investigation

The font was most recently updated in google/fonts by commit `e1d648010` ("Inter: Version 4.001;git-66647c0bb added"). The commit body confirms:

> Taken from the upstream repo https://www.github.com/rsms/inter at commit https://www.github.com/rsms/inter/commit/66647c0bbbe41a850d79d9c76fb13add3378940f.
> Resolves #3429

The METADATA.pb uses an `archive_url` (a zip file from a GitHub release) as the actual source for the font binaries. This is a special case — the fonts were taken from a pre-built release archive rather than built from source.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/rsms/inter`. The commit `66647c0bbbe41a850d79d9c76fb13add3378940f` was verified to exist in the cached repo (2024-05-24, "makefile: make sure dist runs googlefonts so that dist_zip_gf succeed").

The `repository_url` uses `www.github.com` instead of `github.com` — this is a minor inconsistency but functional.

**Source format**: The repository contains `src/Inter-Roman.glyphspackage` and `src/Inter-Italic.glyphspackage` (Glyphs Package format). There is **no `config.yaml`** in the upstream repository.

An override `config.yaml` exists in the google/fonts family directory at `ofl/inter/config.yaml`:
```yaml
sources:
  - src/Inter-Roman.glyphspackage
  - src/Inter-Italic.glyphspackage
familyName: Inter
buildVariable: true
buildOTF: false
```

Per policy, when an override `config.yaml` exists locally, the `config_yaml` field in METADATA.pb is not needed. The current METADATA.pb does not set `config_yaml`, which is correct.

The family also has a `minisite_url: "https://rsms.me/inter"` field.

## Conclusion

The source block is complete and correct. The `repository_url` and `commit` are verified against the cached repo. An override `config.yaml` exists in the google/fonts directory. The `archive_url` field indicates fonts were taken from a pre-built release zip rather than built from source. No changes are strictly needed. The `www.github.com` URL prefix is a minor cosmetic inconsistency but functional.
