# Investigation Report: Boldonse

## Summary

Boldonse is a display typeface by Universitype, added to Google Fonts on 2025-02-19. It is a relatively new addition with a single static weight. The upstream repository is hosted under the googlefonts organization, and the entire repo history consists of a single commit.

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Boldonse |
| Designer | Universitype |
| Repository URL | https://github.com/googlefonts/boldonse |
| Commit Hash | `ebf7dd8db35ccdb0fb262331234634d92ac1231f` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| License | OFL |
| Date Added | 2025-02-19 |

## How URL Found

The repository URL `https://github.com/googlefonts/boldonse` is stated in:
- The copyright string in METADATA.pb
- The commit message adding the font to google/fonts

## How Commit Determined

The commit hash `ebf7dd8db35ccdb0fb262331234634d92ac1231f` is recorded in the commit message adding the font (google/fonts commit `5bf2c8330`):

> Boldonse: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added
> Taken from the upstream repo https://github.com/googlefonts/boldonse at commit ebf7dd8db35ccdb0fb262331234634d92ac1231f.

The upstream commit is titled "Renamed folder" and is the only commit in the entire repository. This is a straightforward onboarding case.

## Config YAML Status

The config file at `sources/config.yaml` exists at the recorded commit and contains:
```yaml
sources:
  - "UT Boldonse Font.glyphs"
buildOTF: false
buildWebfont: false
```

This is a valid gftools-builder configuration for building a static TTF font.

## Verification

- **Commit exists in upstream**: Yes, verified. `ebf7dd8` is the only commit in the repository (HEAD of main).
- **Config.yaml exists at commit**: Yes, `sources/config.yaml` is present and valid.
- **Source files match METADATA.pb**: The METADATA.pb references `fonts/ttf/Boldonse-Regular.ttf` as the source file, along with article files (ARTICLE.en_us.html and several images).
- **Branch correct**: main, confirmed.
- **Upstream repo cached**: Yes, at `upstream_repos/fontc_crater_cache/googlefonts/boldonse`.

## Confidence Level

**HIGH** -- The commit hash is stated in the onboarding commit message. The upstream repo has only one commit, making verification trivial. The config.yaml is present and valid.

## Open Questions

None. This family's source documentation is complete and verified.
