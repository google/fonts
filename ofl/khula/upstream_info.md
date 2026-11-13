# Investigation: Khula

## Summary

| Field | Value |
|-------|-------|
| Family Name | Khula |
| Slug | khula |
| License Dir | ofl |
| Repository URL | https://github.com/erinmclaughlin/Khula |
| Commit Hash | 1389c0184856d690ea489f86e84c546e4473722d |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/erinmclaughlin/Khula"
  commit: "1389c0184856d690ea489f86e84c546e4473722d"
}
primary_script: "Deva"
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `erinmclaughlin/Khula` is cached at `upstream_repos/fontc_crater_cache/erinmclaughlin/Khula`.

The repository contains UFO sources in the `UFO/` directory:
- `UFO/Bold/`, `UFO/ExtraBold/`, `UFO/Light/`, `UFO/Regular/`, `UFO/SemiBold/`
- `Khula_superpolator.sp3` (Superpolator source for interpolation)

No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/khula/config.yaml` provides an override:

```yaml
sources:
  - UFO/Light/Khula-Light.ufo
  - UFO/Regular/Khula-Regular.ufo
  - UFO/SemiBold/Khula-Semibold.ufo
  - UFO/Bold/Khula-Bold.ufo
  - UFO/ExtraBold/Khula-ExtraBold.ufo
familyName: "Khula"
buildVariable: false
```

The latest commit in the upstream repo is `703fbf36` ("Merge pull request #5 from JosephWeaver/patch-1"), but the METADATA.pb records commit `1389c018` ("Update README.md"), which is an earlier commit in the history. This indicates the onboarding was done at commit `1389c018`.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

## Override config corrected (2026-11-13)

**Model**: Claude Fable 5.2

The override listed `Khula_superpolator.sp3`, a Superpolator file that no build tool reads. It was replaced with the five static UFOs under `UFO/`, which the 2015 release was built from (the same layout as the Yantramanav override).

With gftools 0.10.8, fontmake 3.12.2 and glyphsLib 6.17.1, the new config builds five fonts with the shipped codepoints. Each has 570 glyphs; the shipped fonts have 571 (an added `.null`). The Semibold builds as `Khula-Semibold.ttf`, family name "Khula Semibold", because the UFO spells it so; Google Fonts ships `Khula-SemiBold.ttf`.
