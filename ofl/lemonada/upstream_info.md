# Investigation: Lemonada

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lemonada |
| Slug | lemonada |
| License Dir | ofl |
| Repository URL | https://github.com/Gue3bara/Lemonada |
| Commit Hash | 21a53a1760f6f3c3e585bc50bc3463e97f1fa7e6 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Gue3bara/Lemonada"
  commit: "21a53a1760f6f3c3e585bc50bc3463e97f1fa7e6"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb has `repository_url`, `commit` hash, and `config_yaml` all populated. The commit `21a53a1760f6f3c3e585bc50bc3463e97f1fa7e6` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/Gue3bara/Lemonada/`:

```
commit 21a53a1760f6f3c3e585bc50bc3463e97f1fa7e6
Author: Mohamed Gaber <gaber@gaberism.net>
Date:   Sun Apr 3 12:32:17 2022 +0200

    ready for review
```

The `config.yaml` exists at `sources/config.yaml` in the upstream repo and specifies:
```yaml
sources:
  - Lemonada.glyphs
axisOrder:
  - wght
familyName: Lemonada
```

The google/fonts history shows:
- `0a3059191` — "Lemonada v4.005 (stat fix) (#3640)"
- `fbaa49d6e` — "lemonada: v4.005 added"

All fields are present and verified.

## Conclusion

All source metadata fields are complete and verified. No action needed.
