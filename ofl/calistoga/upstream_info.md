# Investigation Report: Calistoga

## Source Data

| Field | Value |
|---|---|
| Family Name | Calistoga |
| Designer | Yvonne Schuttler, Sorkin Type, Eben Sorkin |
| License | OFL |
| Repository URL | https://github.com/SorkinType/Calistoga |
| Commit Hash | `61662683b93028d797e7ddb327fd33ff7e2838d4` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| Status | complete |

## How URL Found

The repository URL `https://github.com/SorkinType/Calistoga` is recorded in METADATA.pb and matches the copyright notice: "Copyright 2019 The Calistoga Project Authors (https://github.com/SorkinType/Calistoga)". It has been consistent since the font was first onboarded.

## How Commit Determined

The commit `61662683b93028d797e7ddb327fd33ff7e2838d4` was explicitly referenced in the google/fonts commit `6f6932903` with the message:

> Taken from the upstream repo https://github.com/SorkinType/Calistoga at commit https://github.com/SorkinType/Calistoga/commit/61662683b93028d797e7ddb327fd33ff7e2838d4.

This is the "Version 1.010" update which superseded the earlier "Version 1.008" (PR #5502, which referenced commit `29e91526`). The METADATA.pb diff in commit `6f6932903` shows the commit hash being updated from `29e91526...` to `61662683...`.

The commit `61662683` is the HEAD of the upstream repository (a "Merge pull request #9 from emmamarichal/main").

## Config YAML Status

The config file `sources/config.yaml` exists at the recorded commit in the upstream repo. It contains:

```yaml
sources:
  - Calistoga.glyphs
familyName: Calistoga
buildVariable: False
```

This is a static font (single weight, Regular only), built from `Calistoga.glyphs` source.

## Verification

- **Commit exists in upstream repo**: Yes, verified as HEAD of main branch
- **Config YAML exists at commit**: Yes, `sources/config.yaml` confirmed
- **Repository URL accessible**: Yes
- **gftools-packager commit message**: Explicitly cites the commit hash in google/fonts commit `6f6932903`
- **Two update rounds tracked**: Version 1.008 (PR #5502, commit `29e9152`) then Version 1.010 (commit `6166268`)

## Confidence Level

**High** - All data is consistent. The commit hash is verified via explicit reference in the gftools-packager commit message, and the config.yaml exists in the upstream repo.

## Open Questions

None. All source data is complete and verified.
