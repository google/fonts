# Investigation: Cairo Play

## Summary

| Field | Value |
|-------|-------|
| Family Name | Cairo Play |
| Slug | cairo-play |
| License Dir | ofl |
| Repository URL | https://github.com/Gue3bara/Cairo |
| Commit Hash | 73d16933c6a0f341c27a69e401da83dcb0d53114 |
| Config YAML | sources/cairoplay.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Gue3bara/Cairo"
  commit: "73d16933c6a0f341c27a69e401da83dcb0d53114"
  config_yaml: "sources/cairoplay.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/CairoPlay/variable/CairoPlay[slnt,wght].ttf"
    dest_file: "CairoPlay[slnt,wght].ttf"
  }
  branch: "master"
}
```

## Investigation

Cairo Play is a variable font (wght 200-1000, slnt -11 to +11) by Mohamed Gaber and Accademia di Belle Arti di Urbino. It was onboarded via gftools-packager.

The last binary update was in google/fonts commit `27c225737` ("Cairo Play: Version 3.130;gftools[0.9.24] added", PR #5972, Yanone, 2023-03-08). The commit message explicitly states: "Cairo Play Version 3.130;gftools[0.9.24] taken from the upstream repo https://github.com/Gue3bara/Cairo at commit https://github.com/Gue3bara/Cairo/commit/73d16933c6a0f341c27a69e401da83dcb0d53114."

The `config_yaml` field was added later by Felipe Sanches in commit `53995c52a` ("[METADATA.pb] Populate font sources related fields for a few font families.", 2025-03-25), which also removed the `branch: "master"` field (later restored in commit `f19b6da7d`).

The upstream repo is cached at `upstream_repos/fontc_crater_cache/Gue3bara/Cairo/`. The commit `73d16933` (message: "Merge pull request #94 from yanone/master", Mohamed Gaber, 2023-03-06) was verified to exist. The config file `sources/cairoplay.yaml` was verified to exist at the recorded commit with contents:

```yaml
buildStatic: false
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
outputDir: ../fonts/CairoPlay
sources:
  - CairoPlay.glyphs
axisOrder:
  - slnt
  - wght
familyName: "Cairo Play"
```

This is a variable font built from a Glyphs source. The `config_yaml` field in METADATA.pb correctly points to `sources/cairoplay.yaml` in the upstream repository.

## Conclusion

All source metadata is complete and verified. The repository URL, commit hash, and config_yaml path are all in place and confirmed by the gftools-packager commit message (PR #5972). Status is `complete`.


## Source-metadata review (2026-06-02) — build-time-generated `.glyphs` (no `.ufoz`; PENDING upstream fix)

**Model**: Claude Opus 4.8

fontc_crater reports `missing source 'sources/CairoPlay.glyphs'` for this family. Unlike the `.ufoz` families in this batch, **there is no committed `.ufoz` to declare**: `sources/CairoPlay.glyphs` is generated at build time from the committed `sources/Cairo.glyphs` by `scripts/makeplay.py` (run by `build.sh`, then `rm`-ed), so it is absent from the static tree.

Declaring the raw `sources/Cairo.glyphs` directly is **not** a valid workaround — it would skip the `makeplay` transform and build the wrong product. So no override config is added here.

**PENDING (work on later):** an upstream PR to `Gue3bara/Cairo` that commits the generated `sources/CairoPlay.glyphs` (conventionally under `sources/generated/`) and points `sources/cairoplay.yaml` at it. (This is the same `sources/generated/` pattern recommended for the other build-time-generated families.)
