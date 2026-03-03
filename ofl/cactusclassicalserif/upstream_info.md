# Investigation: Cactus Classical Serif

## Summary

| Field | Value |
|-------|-------|
| Family Name | Cactus Classical Serif |
| Slug | cactus-classical-serif |
| License Dir | ofl |
| Repository URL | https://github.com/MoonlitOwen/CactusSerif |
| Commit Hash | a267f9f32087eb9e6a9203c734cb952a64bc05be |
| Config YAML | source/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/MoonlitOwen/CactusSerif"
  commit: "a267f9f32087eb9e6a9203c734cb952a64bc05be"
  config_yaml: "source/config.yaml"
}
```

## Investigation

The repository URL changed over the life of this font:
- **Original (v1.000)**: `https://github.com/aaronbell/CactusSerif` — used for initial onboarding in commit `344f7a69b` (2024-05-14) by Aaron Bell.
- **Updated (v1.005)**: `https://github.com/MoonlitOwen/CactusSerif` — repo moved when v1.005 was submitted via PR #9545. The METADATA.pb was corrected in google/fonts commit `bdb9dcdf6` ("sources info for Cactus Classical Serif: Version 1.005 (PR #9545)", Felipe Sanches, 2025-11-28).

The commit `a267f9f32087eb9e6a9203c734cb952a64bc05be` (message: "Upload built fonts", NightFurySL2001, 2025-06-09) is the commit where the v1.005 fonts were built in the MoonlitOwen/CactusSerif repo. Aaron Bell's google/fonts commit `a05de1830` (2025-06-09) imported the font from this exact build. The upstream repo is cached at `upstream_repos/fontc_crater_cache/MoonlitOwen/CactusSerif/`.

The `config.yaml` at path `source/config.yaml` was verified to exist at the recorded commit. Contents:

```yaml
sources:
  - temp/CactusClassicalSerif-Regular.ufo
familyName: "Cactus Classical Serif"
removeOutlineOverlaps: True
extraFontmakeArgs: "--production-names --overlaps-backend pathops"
autohintOTF: False
autohintTTF: False
buildWebfont: False
buildSmallCap: False
version: 1.005
```

This is a static font built from a UFO source. The `config_yaml` field in METADATA.pb correctly points to `source/config.yaml` in the upstream repository.

## Conclusion

All source metadata is complete and verified. The repository URL (corrected from aaronbell to MoonlitOwen), commit hash, and config_yaml path are all in place. Status is `complete`. The migration from aaronbell to MoonlitOwen is clearly documented in PR #9545.
