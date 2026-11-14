# Investigation: Jaldi

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jaldi |
| Slug | jaldi |
| License Dir | ofl |
| Repository URL | https://github.com/Omnibus-Type/Jaldi |
| Commit Hash | 13315457c7dd2cadd03642a2edd9d9552d0c227f |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Omnibus-Type/Jaldi"
  commit: "13315457c7dd2cadd03642a2edd9d9552d0c227f"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows four commits touching this font:
- `1f3895e6b` — "jaldi: Updating to v1.007" (latest update, no upstream reference)
- `8640d2357` — "Updating Jaldi"
- `6385bf319` — "Updating Jaldi"
- `90abd17b4` — "Initial commit" (original onboarding)

The METADATA.pb was updated through several commits:
- `21e98aac8` — "More upstreams (i,j,k)" — added the `repository_url` field
- `19cdcec59` — "[Batch 1/4] port info from fontc_crater targets list" — added `commit` and `config_yaml` fields, sourced from fontc_crater's target.json (commit `ee7a65d433882450efa1d8418ed746bf07c05642` in fontc_crater repo)
- `cc250c972` — added `primary_script` field

The fontc_crater batch commit added commit hash `13315457c7dd2cadd03642a2edd9d9552d0c227f` and config_yaml `sources/config.yaml`.

The upstream repository `Omnibus-Type/Jaldi` is cached at `upstream_repos/fontc_crater_cache/Omnibus-Type/Jaldi`. Commit `13315457c7dd2cadd03642a2edd9d9552d0c227f` exists in the repo — it is the "Update README.md" commit by Yorlmar Campos, dated 2021-04-14. This commit is likely not the exact onboarding commit for the current font binary (the latest binary update via "jaldi: Updating to v1.007" doesn't reference a specific upstream commit), but it was the best available reference when the fontc_crater data was compiled.

The file `sources/config.yaml` exists in the upstream repo and is valid.

## Conclusion

The source block in METADATA.pb is complete with all fields present. The commit hash `13315457c7dd2cadd03642a2edd9d9552d0c227f` comes from the fontc_crater targets list and is verified to exist in the upstream repo. Note that the most recent binary update ("jaldi: Updating to v1.007") did not record an upstream commit, so there may be a newer relevant commit in the upstream. However, the current data is the best available and no correction is needed at this time.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`13315457`](https://github.com/Omnibus-Type/Jaldi/commit/13315457) (a 2021 README commit, copied from fontc_crater's targets list in [google/fonts `19cdcec5`](https://github.com/google/fonts/commit/19cdcec5)) to [`4460fe00`](https://github.com/Omnibus-Type/Jaldi/commit/4460fe00) ("`lookupflag IgnoreMarks;` in `cjct`", 2015-05-31, tag 1.007, on the default `gh-pages` branch).

The shipped v1.007 TTFs, added by [google/fonts `1f3895e6`](https://github.com/google/fonts/commit/1f3895e6) on 2015-06-04, are byte-identical to `Fonts/Jaldi-*.ttf` as committed with `SRC/Jaldi-[2048].glyphs` in `4460fe00`: Regular md5 `8e249fe3a198dea4cd46ce23071ef9c5`, Bold `84855c7c0bde00c8fca28f42d76855de`. Later commits only add a GlyphData.xml, until [`40f45fea`](https://github.com/Omnibus-Type/Jaldi/commit/40f45fea) (2021) replaced the 2048-UPM source with the unshipped v1.010 `sources/Jaldi.glyphs`.

`4460fe00` has no `sources/config.yaml`, so `config_yaml` was dropped from METADATA.pb and an override `config.yaml` names `SRC/Jaldi-[2048].glyphs` (Regular and Bold instances).
