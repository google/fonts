# Investigation: Bungee Hairline

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bungee Hairline |
| Slug | bungee-hairline |
| License Dir | ofl |
| Repository URL | https://github.com/djrrb/Bungee |
| Commit Hash | eb03cf69adab5094f6b84e95357789cdf3bfeb99 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/djrrb/Bungee"
  commit: "eb03cf69adab5094f6b84e95357789cdf3bfeb99"
  archive_url: "https://github.com/djrrb/Bungee/releases/download/v2.000/Bungee-fonts.zip"
  files {
    source_file: "Bungee_Basic/BungeeHairline-Regular.ttf"
    dest_file: "BungeeHairline-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The version 2.000 update was onboarded via google/fonts commit `93c3a3d13` ("Bungee Hairline: Version 2.000 added", Viviana Monsalve, 2024-05-30). The commit message explicitly states: "Taken from the upstream repo https://github.com/djrrb/Bungee at commit https://github.com/djrrb/Bungee/commit/eb03cf69adab5094f6b84e95357789cdf3bfeb99."

Earlier, the repository URL had been added without a commit hash by Simon Cozens in commit `46a7c0576` ("Add more upstreams (a,b)", 2024-01-14). The Bungee Hairline commit hash was added to METADATA.pb only when v2.000 was onboarded.

The repository URL `https://github.com/djrrb/Bungee` is the shared upstream for all Bungee variants. It is cached at `upstream_repos/fontc_crater_cache/djrrb/Bungee/`.

The commit `eb03cf69adab5094f6b84e95357789cdf3bfeb99` (message: "Bump fontbakery", Just van Rossum, 2024-05-30) is the HEAD of the master branch at the time of the v2.000 onboarding. The METADATA.pb also includes an archive_url pointing to the v2.000 release ZIP, which is the actual source of the binary.

The upstream repository does not contain a `config.yaml`. An override `config.yaml` was created in the google/fonts family directory (`ofl/bungeehairline/config.yaml`) by Felipe Sanches in commit `f6c68379a` ("Add override config.yaml for 50 font families", 2026-02-16). Contents:

```yaml
sources:
  - sources/2-build/Bungee_Basic/Bungee-Hairline.ufo
familyName: Bungee Hairline
buildStatic: true
buildOTF: false
```

The source file `sources/2-build/Bungee_Basic/Bungee-Hairline.ufo` was verified to exist at the recorded commit `eb03cf69`. Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Conclusion

All source metadata is complete and verified. The repository URL, commit hash, and override config.yaml are all in place. The commit hash is well-documented in the google/fonts commit message for the v2.000 update. Status is `complete`.
