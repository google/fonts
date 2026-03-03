# Investigation: Intel One Mono

## Summary

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

## Source Data (METADATA.pb)

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

## Investigation

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

## Conclusion

The `repository_url` was corrected to point to the canonical `intel/intel-one-mono` repo, but the `commit` hash `cec102c3` was not updated and is now incorrect — it belongs to the `googlefonts/intel-one-mono` mirror, not the canonical repo. The correct commit from `intel/intel-one-mono` that corresponds to version 1.004 needs to be identified. The override `config.yaml` in google/fonts correctly references the designspace sources.

Action needed: Find the commit hash in `intel/intel-one-mono` that corresponds to version 1.004 (the version that was onboarded via the googlefonts mirror at `cec102c3`) and update the `commit` field in METADATA.pb.
