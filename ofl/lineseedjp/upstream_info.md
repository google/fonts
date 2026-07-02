# Investigation Report: LINE Seed JP

**Model**: Claude Opus 4.6

## Summary

| Field | Value |
|---|---|
| **Family Name** | LINE Seed JP |
| **Slug** | lineseedjp |
| **Designer** | LY Corporation, Fontrix, Fontworks |
| **License** | OFL |
| **Primary Script** | Jpan |
| **Repository URL** | https://github.com/line/seed |
| **Commit Hash** | `ea7a320d85172a57dc458507267d82e7c0f2d49a` |
| **Config YAML** | `LINESeedJP/sources/config.yaml` (in upstream repo) |
| **Status** | complete |
| **Confidence** | HIGH |

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/line/seed"
  config_yaml: "LINESeedJP/sources/config.yaml"
}
```

The source block has `repository_url` and `config_yaml` but is **missing the `commit` field**. The commit hash `ea7a320d85172a57dc458507267d82e7c0f2d49a` should be added.

## Investigation Details

### Onboarding History

LINE Seed JP was onboarded to Google Fonts via [PR #10011](https://github.com/google/fonts/pull/10011), created by Aaron Bell (@aaronbell) on 2025-11-20 and merged by Emma Marichal (@emmamarichal) on 2025-11-21. The PR title was "LINE Seed JP : 1.008 added".

The PR body explicitly stated:
> Taken from the upstream repo https://github.com/line/seed at commit https://github.com/line/seed/commit/ea7a320d85172a57dc458507267d82e7c0f2d49a

The PR also referenced "Closes #7561", which appeared to be an issue requesting the addition of LINE Seed JP.

### Commit History in google/fonts

1. `6ffeafaa8` (2025-11-20, Aaron) — "Adding LINE Seed JP" — original onboarding commit
2. `6b65ef9a3` (2025-11-21, Aaron) — "Making minor updates to metadata"
3. `4128478be` (2026-02-18, Emma Marichal) — "Update link to LINE Seed typeface"
4. `5ddf312e6` (2026-02-20, Felipe Sanches) — "Add config_yaml enrichment for 82 font families" — added `config_yaml` field to source block

### Upstream Repository Analysis

The upstream repository at https://github.com/line/seed was verified as the correct source. Key observations:

- **Repo structure**: Contains `LINESeedJP/sources/` directory with `.glyphspackage` source files (Thin, Regular, Bold, ExtraBold) and `config.yaml`
- **Maintainers**: The repo is maintained by TAMADA Akihiro (spring-raining) from LY Corporation, with contributions from Aaron Bell (@aaronbell) and Simon Cozens
- **Tags**: Three release tags exist: `v20231127`, `v20241007`, `v20251119`
- **Tag `v20251119`** points exactly to commit `ea7a320d85172a57dc458507267d82e7c0f2d49a`, confirming the onboarding used this tagged release

### Commit Hash Verification

The referenced commit `ea7a320d85172a57dc458507267d82e7c0f2d49a` ("ci: Update the release steps", 2025-11-19) was verified:

1. **Explicitly referenced** in the PR #10011 body by the onboarder
2. **Tagged as `v20251119`** in the upstream repo, confirming it was a release point
3. **Dated 2025-11-19**, one day before the google/fonts PR was created (2025-11-20) — consistent timing
4. **Is HEAD of origin/main** — no additional commits have been made to the upstream repo since onboarding
5. **Aaron Bell contributed** to this commit range — he made commits `41dd6f9` and `b3c59339` in the upstream repo (updating sources per fontspector and updating copyright string), which were merged via PR #9, followed by CI fixes by spring-raining that culminated in `ea7a320`

The commit hash is confirmed with HIGH confidence.

### Config YAML Verification

The config file at `LINESeedJP/sources/config.yaml` in the upstream repo was verified. At commit `ea7a320`, it contained:

```yaml
sources:
  - LINESeedJP-Thin.glyphspackage
  - LINESeedJP-Regular.glyphspackage
  - LINESeedJP-Bold.glyphspackage
  - LINESeedJP-ExtraBold.glyphspackage
familyName: LINE Seed JP
autohintTTF: false
autohintOTF: false
extraStaticFontmakeArgs: --subroutinizer compreffor
```

No override `config.yaml` exists in the google/fonts family directory. The `config_yaml` field in METADATA.pb correctly points to the upstream file path.

### What Needs to Be Fixed

The METADATA.pb source block is missing the `commit` field. The recommended update:

```
source {
  repository_url: "https://github.com/line/seed"
  commit: "ea7a320d85172a57dc458507267d82e7c0f2d49a"
  config_yaml: "LINESeedJP/sources/config.yaml"
}
```

## Cached Repo Status

- **Path**: upstream_repos/fontc_crater_cache/line/seed
- **Branch**: main (up to date with origin/main)
- **Status**: Clean, no local modifications
- **HEAD**: `ea7a320d85172a57dc458507267d82e7c0f2d49a`
