# Bebas Neue - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bebas Neue |
| Repository URL | https://github.com/dharmatype/Bebas-Neue |
| Commit Hash | 686d14af640c17af3691c597778f121d840d9051 |
| Config YAML | (none in upstream; override in google/fonts) |
| Status | complete |
| Category | DISPLAY, SANS_SERIF |
| Designer | Ryoichi Tsunekawa |
| Date Added | 2019-10-16 |

## How the Repository URL Was Found

The repository URL `https://github.com/dharmatype/Bebas-Neue` was recorded in the Font Bakery Dashboard PR that initially added Bebas Neue to Google Fonts. PR #2208 ("[Font Bakery Dashboard] create family: Bebas Neue", October 2019) contains metadata fields including:

> **upstream** `"https://github.com/dharmatype/Bebas-Neue"`
> **repository** https://github.com/dharmatype/Bebas-Neue

The METADATA.pb `source` block also contains `repository_url: "https://github.com/dharmatype/Bebas-Neue"`.

## How the Commit Hash Was Determined

The commit hash `686d14af640c17af3691c597778f121d840d9051` was explicitly recorded in the Font Bakery Dashboard PR #2208 body:

> **commit** 686d14af640c17af3691c597778f121d840d9051
> **commitDate** 2019-10-07T22:21:38.000Z

This commit in the upstream repo is titled "Update DESCRIPTION.en_us.html" and is dated October 8, 2019 (JST), which aligns with the commitDate in the PR. The font was added to google/fonts in commit `1e42f687f` on October 17, 2019.

The font binary in google/fonts has not been modified since the initial addition - the font files path in the upstream repo is `fonts/BebasNeue(2018)ByDhamraType/ttf/`.

## Config YAML Status

**No config.yaml exists** in the upstream repository at the recorded commit (or any commit). The upstream repo has:
- `sources/BebasNeueV2.0(2018).glyphs` - Glyphs source file
- No build configuration file

However, an **override config.yaml exists** in the google/fonts family directory at `ofl/bebasneue/config.yaml`:

```yaml
sources:
  - sources/BebasNeueV2.0(2018).glyphs
```

This override was added in commit `5ddf312e6` ("Add config_yaml enrichment for 82 font families") in google/fonts. Since the override exists locally, the `config_yaml` field is correctly omitted from the METADATA.pb `source` block (google-fonts-sources auto-detects local overrides).

## Verification

- **Repository exists**: Yes, cached at `upstream_repos/fontc_crater_cache/dharmatype/Bebas-Neue/`
- **Commit exists**: Yes, `686d14a` confirmed ("Update DESCRIPTION.en_us.html", dated 2019-10-08)
- **Commit hash matches PR reference**: Yes, PR #2208 explicitly records `686d14af640c17af3691c597778f121d840d9051`
- **Override config.yaml exists**: Yes, at `ofl/bebasneue/config.yaml` pointing to `sources/BebasNeueV2.0(2018).glyphs`
- **Source block in METADATA.pb**: Has `repository_url` only (commit hash in METADATA.pb was added later; config_yaml correctly omitted due to override)
- **Repo structure at commit**: Contains `sources/BebasNeueV2.0(2018).glyphs`, `fonts/`, `documentation/`, standard metadata files

## Confidence Level

**High** - The commit hash was explicitly recorded by the Font Bakery Dashboard in the onboarding PR. The upstream repo exists and the commit is verified. The override config.yaml properly references the Glyphs source file. All data is consistent.

## Open Questions

None. This family is fully documented and verified. The source block in METADATA.pb only has `repository_url` without commit hash - it could be enriched with the commit hash for completeness, though the tracking data already records it.
