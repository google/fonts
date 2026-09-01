# Cinzel Decorative - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Cinzel Decorative |
| Designer | Natanael Gama |
| Repository URL | https://github.com/NDISCOVER/Cinzel |
| Commit Hash | `1c62abfb8d5e27ea0a09169d621b32d24fdb8691` |
| Config YAML | Override in google/fonts (`ofl/cinzeldecorative/config.yaml`) |
| Status | Complete |
| Date Added | 2012-10-05 |

## How URL Found

The repository URL `https://github.com/NDISCOVER/Cinzel` was already recorded in the METADATA.pb source block. Cinzel Decorative shares the same upstream repository as Cinzel. NDISCOVER is Natanael Gama's GitHub organization.

## How Commit Determined

The commit `1c62abf` ("Glyphs Files", dated 2019-11-12) is the root/initial commit of the NDISCOVER/Cinzel repository. This commit contains only the original Glyphs source files (`Glyphs Files/Cinzel_Regular.glyphs` and `Glyphs Files/Cinzel_Decorative.glyphs`), which were the original design sources before TypeNetwork contributed UFO/designspace sources.

PR #878 ("hotfix-cinzeldecorative: v1.002 added", by Marc Foley, 2017-05-08) updated the Cinzel Decorative fonts. The PR body is empty, providing no explicit upstream reference. However, the commit `1c62abf` predates even the TypeNetwork contributions and represents the original Glyphs sources that would have been used for the static font builds.

The sources info commit (`040170f45`) explicitly notes: "Exact version of sources originally used for onboarding is still unclear."

## Config YAML Status

- **No config.yaml in upstream**: The NDISCOVER/Cinzel repository does not contain a config.yaml file at any commit.
- **Override config.yaml exists**: An override `config.yaml` is present in `ofl/cinzeldecorative/config.yaml` in the google/fonts repository.

Override config.yaml contents:
```yaml
buildVariable: false
sources:
  - Glyphs Files/Cinzel_Regular.glyphs
  - Glyphs Files/Cinzel_Decorative.glyphs
```

Files at recorded commit `1c62abf`:
```
.DS_Store
Glyphs Files/Cinzel_Decorative.glyphs
Glyphs Files/Cinzel_Regular.glyphs
```

The override config.yaml correctly references the Glyphs source files that exist at this commit.

## Verification

- Commit hash `1c62abf` verified to exist in NDISCOVER/Cinzel repo
- Source files `Glyphs Files/Cinzel_Regular.glyphs` and `Glyphs Files/Cinzel_Decorative.glyphs` confirmed present at the recorded commit
- This is the root commit of the repo, so it represents the earliest available source state
- Override config.yaml correctly references the Glyphs sources

## Confidence Level

**Medium** - The repository URL and override config.yaml are correct. However, the exact commit used for the original onboarding in 2012/2017 is uncertain. The recorded commit `1c62abf` (2019-11-12) postdates the google/fonts PR #878 (2017-05-08), suggesting the Glyphs files may have been obtained from a different source or the repo was initialized later with the original files. The sources info commit itself acknowledges this uncertainty.

## Open Questions

- The recorded commit `1c62abf` is dated 2019-11-12, but PR #878 was from 2017-05-08. This means the NDISCOVER/Cinzel repo was created after the fonts were already in google/fonts. The original source of the Glyphs files used for the 2017 hotfix remains unclear. The commit is likely the best available reference to the original design sources, even though the repo was created after onboarding.
