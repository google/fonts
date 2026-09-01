# Investigation: Goudy Bookletter 1911

## Summary

Goudy Bookletter 1911 is a serif display typeface by Barry Schwartz, based on Frederic Goudy's Kennerley Oldstyle. It was added to Google Fonts in the initial repository commit (2015-03-07). The upstream repository at `theleagueof/goudy-bookletter-1911` contains a single commit with UFO sources but no `config.yaml`. The font has never been updated since initial onboarding. An override config.yaml can be created for gftools-builder using the UFO source.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Goudy Bookletter 1911                                              |
| Designer           | Barry Schwartz                                                     |
| Repository URL     | https://github.com/theleagueof/goudy-bookletter-1911               |
| Commit Hash        | 85ff5b834b4f63feb36fd2053949c19660580e48                           |
| Config YAML        | None in upstream; override config.yaml needed in google/fonts      |
| Source Format       | UFO (source/GoudyBookletter1911.ufo)                              |
| Status             | missing_config                                                     |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Current State

The current METADATA.pb already has a source block with the repository URL and commit hash:

```
source {
  repository_url: "https://github.com/theleagueof/goudy-bookletter-1911"
  commit: "85ff5b834b4f63feb36fd2053949c19660580e48"
}
```

The repository_url was added by Simon Cozens in commit `474a446c0` ("More upstreams (g,h)", 2024-01-14). The commit hash was added in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25).

### Upstream Repository Analysis

- **Repository**: https://github.com/theleagueof/goudy-bookletter-1911
- **Cached at**: upstream_repos/fontc_crater_cache/theleagueof/goudy-bookletter-1911
- **Branches**: master only
- **Total commits**: 1 (single initial commit)
- **Commit**: `85ff5b8` by micah rich, 2011-05-25

The repository contains:
- `source/GoudyBookletter1911.ufo` - UFO source (gftools-builder compatible)
- `GoudyBookletter1911.otf` - Pre-built OTF binary
- `webfonts/goudy_bookletter_1911-webfont.ttf` - Pre-built TTF (40,896 bytes)
- No `config.yaml` or build configuration

### Onboarding History

The font was included in the google/fonts initial commit (`90abd17b4`, 2015-03-07) along with all other fonts. The TTF in google/fonts is 73,496 bytes, while the TTF in the upstream webfonts directory is 40,896 bytes -- they are different files. The font in google/fonts was never updated (same binary since the initial commit).

Since the font predates gftools-packager, there is no PR or commit message referencing the upstream repo. However, the only commit in the upstream repo is `85ff5b8`, and this is the only possible commit to reference.

### Config YAML Assessment

The upstream repo has a `.ufo` source file at `source/GoudyBookletter1911.ufo`, which is compatible with gftools-builder. However, there is no `config.yaml` in the upstream repo. An override config.yaml could be created in the google/fonts family directory:

```yaml
sources:
  - source/GoudyBookletter1911.ufo
```

## Conclusion

The source block in METADATA.pb is already correct with repository URL and commit hash. The only missing piece is a build configuration. An override `config.yaml` should be added to the google/fonts family directory to enable building from the UFO source.

### Current METADATA.pb Source Block (already correct)

```
source {
  repository_url: "https://github.com/theleagueof/goudy-bookletter-1911"
  commit: "85ff5b834b4f63feb36fd2053949c19660580e48"
}
```

### Recommended Override config.yaml (for google/fonts directory)

```yaml
sources:
  - source/GoudyBookletter1911.ufo
```

**Status**: missing_config (override config.yaml needed)
**Confidence**: HIGH -- only one commit exists in the upstream repo, making the commit hash unambiguous.
