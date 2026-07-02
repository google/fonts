# Investigation: Lakki Reddy

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lakki Reddy |
| Slug | lakki-reddy |
| License Dir | ofl |
| Repository URL | https://github.com/appajid/lakkireddy |
| Commit Hash | bf2dceb7e47e591aa7e76d7e268636ea67d66986 |
| Config YAML | unknown |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/appajid/lakkireddy"
  commit: "bf2dceb7e47e591aa7e76d7e268636ea67d66986"
}
```

## Investigation

The METADATA.pb has both a `repository_url` and a `commit` hash. The commit `bf2dceb7e47e591aa7e76d7e268636ea67d66986` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/appajid/lakkireddy/`:

```
commit bf2dceb7e47e591aa7e76d7e268636ea67d66986
Author: appajid <ambarisha@gmail.com>
Date:   Tue Dec 9 11:20:13 2014 +0530

    updating copyright and latin characters
```

The google/fonts history shows the font was added in the initial commit (`90abd17b4`), and no later updates are recorded.

The upstream repo at `upstream_repos/fontc_crater_cache/appajid/lakkireddy/` contains:
- `LakkiReddy.sfd` — FontForge SFD source (not gftools-builder compatible)
- `LakkiReddy.ufo` — UFO source

The repository has SFD sources (FontForge format) and a UFO file, but no `config.yaml` for gftools-builder. The SFD file is a primary source format that does not work with gftools-builder directly.

## Conclusion

Commit hash and repository URL are both present and verified. No `config.yaml` exists in the upstream repo. The sources include an SFD file and a UFO file. An override `config.yaml` could potentially be created for the UFO source in google/fonts.
