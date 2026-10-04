# Investigation Report: Gayathri

## Summary

Gayathri is a Malayalam display typeface designed by Binoy Dominic with OpenType engineering by Kavya Manohar, part of the Swathanthra Malayalam Computing (SMC) project. It was onboarded to Google Fonts on 2019-06-10 by Marc Foley. The upstream repository is on GitHub at `smc/Gayathri` (also mirrored on GitLab at `smc/fonts/gayathri`). The onboarding commit is explicitly documented in the google/fonts commit message. The upstream repo has gftools-builder-compatible sources (.designspace + .ufo) at the referenced commit but no config.yaml, so an override config.yaml would be needed.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gayathri                                                           |
| Repository URL    | https://github.com/smc/Gayathri                                   |
| Commit Hash       | 5ad0cb435bd61227de1e95dc54ee85bfca671c53                           |
| Commit Date       | 2019-06-02                                                        |
| Commit Message    | Fix the name tableentry for copyright                             |
| Config YAML       | None (upstream has no config.yaml; override needed)                |
| Source Files      | sources/Gayathri.designspace, sources/Gayathri-{Thin,Regular,Bold}.ufo |
| Onboarding PR     | Direct commit 9c887c8b (no PR, pushed directly to main)           |
| Onboarder         | Marc Foley (m.foley.88@gmail.com)                                 |
| Date Added        | 2019-06-10                                                        |
| Status            | missing_config                                                    |
| Confidence        | HIGH                                                              |

## Investigation Details

### 1. METADATA.pb Analysis

The current METADATA.pb has no `source { }` block. Key metadata:
- Name: Gayathri
- Designer: SMC, Binoy Dominic
- License: OFL
- Date added: 2019-06-10
- Primary script: Mlym (Malayalam)
- Copyright references `https://gitlab.com/smc/fonts/gayathri`

### 2. Git History in google/fonts

The font was added in commit `9c887c8b` on 2019-06-10 by Marc Foley with the message:

> gayathri: v1.000 added.
>
> Taken from the upstream repo https://github.com/smc/gayathri at commit https://github.com/smc/Gayathri/commit/5ad0cb435bd61227de1e95dc54ee85bfca671c53

This commit was pushed directly to main (not via a PR). It added:
- ofl/gayathri/DESCRIPTION.en_us.html
- ofl/gayathri/Gayathri-Bold.ttf
- ofl/gayathri/Gayathri-Regular.ttf
- ofl/gayathri/Gayathri-Thin.ttf
- ofl/gayathri/METADATA.pb
- ofl/gayathri/OFL.txt

No subsequent updates to the binary font files have been made.

### 3. Upstream Repository

The upstream repo exists at two locations:
- **GitHub**: https://github.com/smc/Gayathri (used for onboarding)
- **GitLab**: https://gitlab.com/smc/fonts/gayathri (referenced in copyright string)

The commit `5ad0cb435bd61227de1e95dc54ee85bfca671c53` (2019-06-02) exists in the GitHub repo and is titled "Fix the name tableentry for copyright". This commit predates the onboarding (2019-06-10) by 8 days, which is consistent.

### 4. Source Files at Referenced Commit

At commit `5ad0cb435`, the sources directory contains:
- `sources/Gayathri.designspace` (designspace format 3, weight axis 100-900)
- `sources/Gayathri-Thin.ufo`
- `sources/Gayathri-Regular.ufo`
- `sources/Gayathri-Bold.ufo`
- `sources/features/` (feature files)
- `sources/design/` (design files)

The designspace defines three masters: Thin (weight 200), Regular (weight 400), and Bold (weight 700).

Note: The designspace file was later removed from the repo in commit `406d7f4c` ("Remove unused designspace file"), but it existed at the referenced onboarding commit.

### 5. Build System

The original build used a Makefile with direct fontmake invocations to produce static OTF and TTF files (no variable font). There is no config.yaml in the upstream repo at any commit.

The font ships as three static TTF files in Google Fonts (Thin, Regular, Bold), not as a variable font. An override config.yaml for gftools-builder would need to reference `sources/Gayathri.designspace` and configure static instance generation.

### 6. Repository Cache

The upstream repo has been cloned to `upstream_repos/fontc_crater_cache/smc/Gayathri/`.

## Conclusion

The source metadata for Gayathri is straightforward to determine. The onboarding commit message explicitly provides both the repository URL and the commit hash. The upstream repo has gftools-builder-compatible sources (designspace + UFO) but lacks a config.yaml file.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/smc/Gayathri"
  commit: "5ad0cb435bd61227de1e95dc54ee85bfca671c53"
}
```

Note: An override config.yaml in the google/fonts family directory would be needed for gftools-builder compatibility. The config should reference `sources/Gayathri.designspace` and configure static font generation for three weights (Thin 100, Regular 400, Bold 700). When that override is created, the `config_yaml` field can be omitted from METADATA.pb as google-fonts-sources auto-detects local overrides.

### Status: missing_config
### Confidence: HIGH
