# Investigation: Langar

## Summary

| Field | Value |
|-------|-------|
| Family Name | Langar |
| Slug | langar |
| License Dir | ofl |
| Repository URL | https://github.com/typeland/Langar |
| Commit Hash | 82c844e60ab055cef1169f7825bc119ea3bd5090 |
| Config YAML | unknown |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/typeland/Langar"
  commit: "82c844e60ab055cef1169f7825bc119ea3bd5090"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/TTF/Langar-Regular.ttf"
    dest_file: "Langar-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb has both `repository_url` and `commit` hash, with explicit file mappings. The commit `82c844e60ab055cef1169f7825bc119ea3bd5090` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/typeland/Langar/`:

```
commit 82c844e60ab055cef1169f7825bc119ea3bd5090
Author: Alessia Mazzarella <>
Date:   Thu Nov 26 12:13:08 2020 +0000

    Updated Test Docs
```

The google/fonts history shows:
- `eff7e984b` — "Langar: Version 1.001; ttfautohint (v1.8.3) added (#2838)"

The file mappings reference `Fonts/TTF/Langar-Regular.ttf`, suggesting the upstream repo distributes prebuilt TTF files rather than using gftools-builder sources. No `config.yaml` was found in the upstream repo.

## Conclusion

Commit hash and repository URL are both present and verified. The upstream repo provides prebuilt TTF binaries, and no `config.yaml` is present. The explicit file mapping in METADATA.pb suggests this was onboarded using gftools-packager in file-copy mode rather than a build pipeline.
