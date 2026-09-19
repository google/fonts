# Investigation: Iceland

## Summary

| Field | Value |
|-------|-------|
| Family Name | Iceland |
| Slug | iceland |
| License Dir | ofl |
| Repository URL | https://github.com/cyrealtype/Iceland |
| Commit Hash | bb43144b50825221060747ddba7b23bc05e7c960 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cyrealtype/Iceland"
  commit: "bb43144b50825221060747ddba7b23bc05e7c960"
}
```

## Investigation

The METADATA.pb at `ofl/iceland/METADATA.pb` already contains a complete source block with both a repository URL and a commit hash. The font was added to google/fonts in the initial commit (90abd17b4f97671435798b6147b698aa9087612f, dated 2015-03-07) by Dave Crossland, and the current METADATA.pb source block was added or updated at some point after that.

The referenced repository `https://github.com/cyrealtype/Iceland` is available in the upstream cache at `upstream_repos/fontc_crater_cache/cyrealtype/Iceland`. The remote URL confirms this is `https://github.com/cyrealtype/Iceland`.

Commit `bb43144b50825221060747ddba7b23bc05e7c960` exists in the cached repo with the message "adding img" (dated 2016-04-06). This is the most recent commit in the repository. The repository contains the font source files: `src/Iceland-Regular-OTF.vfb`, `src/Iceland-Regular-TTF.vfb` (FontLab VFB format), `src/Iceland-Regular-OTF.otf`, and `src/sample.png`. The VFB source file `src/Iceland-Regular-TTF.vfb` was verified to exist at this commit.

There is no `config.yaml` in the upstream repository. However, an override `config.yaml` exists in `ofl/iceland/config.yaml` within google/fonts with the following content:

```yaml
buildVariable: false
sources:
  - src/Iceland-Regular-TTF.vfb
  - src/Iceland-Regular-OTF.vfb
```

This config references VFB source files that exist in the upstream repo at the referenced commit.

Note: A separate `https://github.com/librefonts/iceland` repository does not appear to exist in the cache. The `cyrealtype/Iceland` repo is the canonical upstream for Iceland, designed by Cyreal (Alex Tarbovsky).

## Conclusion

The source block in METADATA.pb is complete and correct. The repository URL points to `cyrealtype/Iceland`, the commit hash `bb43144` is verified to exist in the cached repo, and an override `config.yaml` is present in the google/fonts family directory. No action is needed.
