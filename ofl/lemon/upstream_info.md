# Investigation: Lemon

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lemon |
| Slug | lemon |
| License Dir | ofl |
| Repository URL | https://github.com/etunni/lemon |
| Commit Hash | 88027507a29de7878336812a328d25245c106e9b |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/etunni/lemon"
  commit: "88027507a29de7878336812a328d25245c106e9b"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Lemon-Regular.ttf"
    dest_file: "Lemon-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb has `repository_url` and `commit` hash. The commit `88027507a29de7878336812a328d25245c106e9b` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/etunni/lemon/`:

```
commit 88027507a29de7878336812a328d25245c106e9b
Merge: c01f5a4 bf8b2e9
Author: Eduardo Rodríguez Tunni <edu@tipo.net.ar>
Date:   Wed Mar 1 10:45:37 2023 -0300
```

The google/fonts history shows:
- `350a3a9ac` — "[gftools-packager] Lemon: Version 1.003; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.24] added"

The upstream repo at `upstream_repos/fontc_crater_cache/etunni/lemon/` contains:
- `sources/Lemon.glyphs` — Glyphs source file

The `sources/` directory has `Lemon.glyphs` but no `config.yaml`. While a Glyphs file is gftools-builder compatible, no `config.yaml` was found.

## Conclusion

Commit hash and repository URL are both present and verified. The upstream has a Glyphs source file but no `config.yaml`. An override `config.yaml` could be created for this family in google/fonts, pointing to `sources/Lemon.glyphs` in the upstream repo.
