# Investigation: Lancelot

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lancelot |
| Slug | lancelot |
| License Dir | ofl |
| Repository URL | https://github.com/antonxheight/Lancelot |
| Commit Hash | 3039d277fadddec95a3dc5aa58182b0aa20659b8 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/antonxheight/Lancelot"
  commit: "3039d277fadddec95a3dc5aa58182b0aa20659b8"
}
```

## Investigation

The METADATA.pb has both `repository_url` and `commit` hash. The commit `3039d277fadddec95a3dc5aa58182b0aa20659b8` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/antonxheight/Lancelot/`:

```
commit 3039d277fadddec95a3dc5aa58182b0aa20659b8
Author: Anton <xheight@hot.ee>
Date:   Tue Nov 15 19:08:22 2011 +0100

    Pushing Lancelot fontlab workfile
```

The google/fonts history shows:
- `8ccda7bf7` — "Fix fsType for 40 font files"
- `90abd17b4` — "Initial commit" (first onboarding)

The upstream repo at `upstream_repos/fontc_crater_cache/antonxheight/Lancelot/` contains:
- `Lancelot_source/` — likely FontLab source files
- `Lancelot_TTF/` — prebuilt TTF files
- `README`

The commit message "Pushing Lancelot fontlab workfile" confirms this is a FontLab VFB project. There is no `config.yaml` in the upstream repo, and FontLab VFB files are not directly compatible with gftools-builder.

## Conclusion

Commit hash and repository URL are both present and verified. The upstream sources are FontLab VFB files with no `config.yaml`. Since the sources are FontLab format (not gftools-builder compatible), creating a `config.yaml` is not straightforward. Status is `missing_config` due to FontLab sources requiring special handling.
