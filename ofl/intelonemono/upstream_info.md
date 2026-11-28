# Investigation: Intel One Mono

## Source-metadata correction (2026-10-15)

**Model**: Claude Opus 5.5

### Initial state

METADATA.pb recorded https://github.com/intel/intel-one-mono at `99e2d6ca170744c62bfb5f52547435f23720abe1`, with an override `config.yaml` in google/fonts naming `sources/masters/IntelOneMono-Roman.designspace` and `IntelOneMono-Italic.designspace`. fontc_crater built the Roman and failed the Italic in both compilers (`'numbersign_underscore_parenleft' has interpolation-incompatible paths`). fontc_crater triage pointed out that the fix is in the googlefonts fork, which is what Google Fonts shipped from.

### Actions taken

The 12 shipped binaries (the two variable fonts and the ten statics, v1.005) were looked up by blob hash in both repositories. None is in https://github.com/intel/intel-one-mono at any commit. All 12 are byte-identical to the files of https://github.com/googlefonts/intel-one-mono at `06572f3e0bbd90622b7f9e8b53e5994a1fd9f593` ("regen fonts", Marc Foley, 2025-06-13 09:59 +0100), seven minutes before he committed them to google/fonts (`fbba48d1d`, "intelonemono: v1.005 add SemiBold instances"). That commit reached the fork's main through `0e8ab5387da525919a8ef679b10c4200e0a78f0f` (merge of googlefonts/intel-one-mono#2). The fork also carries the outline-compatibility fixes the intel repository lacks (Yanone, April 2025).

The source block now records the fork at `06572f3e`, with the fork's own `sources/config.yaml`, which builds the fonts with gftools-builder (VTT hinting from `hinting/`). The override `config.yaml` was removed: it named `IntelOneMono-Roman.designspace`, which the fork renamed to `IntelOneMono.designspace`. The file mapping lists the license and all 12 fonts. The `article/` entries were removed from it: `article/ARTICLE.en_us.html` and `article/showing.png` were edited in google/fonts itself (`7801f1106`, `d982a73c7`) and are in neither repository, so copying them from upstream would undo those edits.

### Final state

```
source {
  repository_url: "https://github.com/googlefonts/intel-one-mono"
  commit: "06572f3e0bbd90622b7f9e8b53e5994a1fd9f593"
  config_yaml: "sources/config.yaml"
  branch: "main"
}
```

fontc_crater (googlefonts/fontc main da343d39, gftools 0.10.3) on this entry: both designspaces build in the default mode, and fontc's output is identical to fontmake's. In gftools mode both fail because gftools passes the config's `extraFontmakeArgs: "--fea-include-dir=features"` to fontc, which has no such option.

The 2026-06-02 correction below said the shipped build's commit was not recoverable; it was, in the googlefonts fork.

## Previous investigations

### Summary

| Field | Value |
|-------|-------|
| Family Name | Intel One Mono |
| Slug | intel-one-mono |
| License Dir | ofl |
| Repository URL | https://github.com/intel/intel-one-mono |
| Commit Hash | cec102c3890991d35e3766424923fa4afc099a1d |
| Config YAML | override config.yaml in google/fonts (ofl/intelonemono/config.yaml) |
| Status | needs_correction |
| Confidence | LOW |

### Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/intel/intel-one-mono"
  commit: "cec102c3890991d35e3766424923fa4afc099a1d"
  files {
    source_file: "article/ARTICLE.en_us.html"
    dest_file: "article/ARTICLE.en_us.html"
  }
  files {
    source_file: "article/showing.png"
    dest_file: "article/showing.png"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/IntelOneMono[wght].ttf"
    dest_file: "IntelOneMono[wght].ttf"
  }
  files {
    source_file: "fonts/variable/IntelOneMono-Italic[wght].ttf"
    dest_file: "IntelOneMono-Italic[wght].ttf"
  }
  branch: "main"
}
```

### Investigation

The font was added to google/fonts in commit `f9bed585f` ("Intel One Mono: Version 1.004 added"). The original onboarding commit body stated:

> Taken from the upstream repo https://github.com/googlefonts/intel-one-mono at commit https://github.com/googlefonts/intel-one-mono/commit/cec102c3890991d35e3766424923fa4afc099a1d.

This means the original onboarding used the **googlefonts/intel-one-mono mirror**, not the canonical `intel/intel-one-mono` repository.

The METADATA.pb was subsequently updated in commit `d0e1cc42c` (2025-06-03, "intelonemono: add hinted statics" by Marc Foley) which changed:
- `repository_url` from `https://github.com/googlefonts/intel-one-mono` to `https://github.com/intel/intel-one-mono`
- `copyright` fields from `googlefonts/intel-one-mono` to `intel/intel-one-mono`
- **But the `commit` field `cec102c3` was NOT changed**

This creates an inconsistency: the commit hash `cec102c3890991d35e3766424923fa4afc099a1d` comes from the `googlefonts/intel-one-mono` mirror but the `repository_url` now points to `intel/intel-one-mono`. This hash does **not exist** in the `intel/intel-one-mono` repository (verified against the cached repo at `upstream_repos/fontc_crater_cache/intel/intel-one-mono`).

Subsequent updates to google/fonts:
- `d27aca07a` — "intelonemono: Update vf" — updated variable fonts only
- `fbba48d1d` — "intelonemono: v1.005 add SemiBold instances" — added static instances

**Source format**: The upstream repository uses `.designspace` and `.ufo` sources. There is **no `config.yaml`** in the intel/intel-one-mono repository itself.

An override `config.yaml` exists in the google/fonts family directory at `ofl/intelonemono/config.yaml`:
```yaml
sources:
  - sources/masters/IntelOneMono-Roman.designspace
  - sources/masters/IntelOneMono-Italic.designspace
```

Per policy, when an override `config.yaml` exists locally, the `config_yaml` field in METADATA.pb is not needed. The current METADATA.pb does not set `config_yaml`, which is correct.

### Conclusion

The `repository_url` was corrected to point to the canonical `intel/intel-one-mono` repo, but the `commit` hash `cec102c3` was not updated and is now incorrect — it belongs to the `googlefonts/intel-one-mono` mirror, not the canonical repo. The correct commit from `intel/intel-one-mono` that corresponds to version 1.004 needs to be identified. The override `config.yaml` in google/fonts correctly references the designspace sources.

Action needed: Find the commit hash in `intel/intel-one-mono` that corresponds to version 1.004 (the version that was onboarded via the googlefonts mirror at `cec102c3`) and update the `commit` field in METADATA.pb.


### Source-metadata correction (2026-06-02, superseded 2026-10-15) — ⚠ REFRESH REQUIRED

**Model**: Claude Opus 4.8

fontc_crater reported a `missing source` failure for this family because the pinned commit was not usable: it is either absent from the repository (a phantom/deleted hash) or predates the declared source, so the source could not be found.

Corrected the METADATA.pb source block:
- commit: `cec102c3890991d35e3766424923fa4afc099a1d` → `99e2d6ca170744c62bfb5f52547435f23720abe1` (2024-07-26)  (repository_url unchanged: `https://github.com/intel/intel-one-mono`)

The declared source is confirmed present at the new commit.

**⚠ REFRESH REQUIRED — this does NOT reproduce the shipped binary.** The shipped binary's exact build commit is not recoverable from the current upstream, so the source now resolves and the family becomes buildable, but a rebuild produces an **updated** font, not the originally-shipped artifact. Before shipping any rebuild, a human must QA the output for reflow / vertical-metric / glyph-coverage / version differences. The original build provenance (the exact source + commit that produced the shipped binary) is not recoverable from the current upstream.
