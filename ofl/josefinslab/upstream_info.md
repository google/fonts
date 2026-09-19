# Investigation: Josefin Slab

## Summary

| Field | Value |
|-------|-------|
| Family Name | Josefin Slab |
| Slug | josefin-slab |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/josefinslab |
| Commit Hash | 61773366f714341802e5f131bd7181073094898f |
| Config YAML | sources/config.yaml |
| Status | needs_correction |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/josefinslab"
  commit: "61773366f714341802e5f131bd7181073094898f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/JosefinSlab-Italic[wght].ttf"
    dest_file: "JosefinSlab-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/variable/JosefinSlab[wght].ttf"
    dest_file: "JosefinSlab[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The fonts were last updated in google/fonts on 2024-11-15 via two consecutive commits:
- `2f085fa92` (16:30, "Josefin Slab: Version 2.100 added"): Referenced upstream commit `d14756349e966c3f4f6bec371e877da960a8470b` (subject: "Merge pull request #44 from emmamarichal/master", dated 2024-11-15 16:10).
- `321d1360e` (16:35, "update fonts"): Updated the font binaries without changing METADATA.pb.

The commit hash in METADATA.pb was subsequently changed from `d14756349e` to `61773366f714341802e5f131bd7181073094898f` via commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), which imported data from fontc_crater's target.json.

Commit `61773366f7` is dated 2024-12-06 (subject: "Merge pull request #45 from emmamarichal/master") — this is **after** the 2024-11-15 google/fonts addition. The commits between `d14756349e` and `61773366f7` include "remove last QA", "remove old build.sh", and "rebuilt fonts with the STAT", suggesting the upstream continued development after the google/fonts onboarding.

The upstream repository at https://github.com/googlefonts/josefinslab is cached at `upstream_repos/fontc_crater_cache/googlefonts/josefinslab`. The commit `61773366f7` is the current HEAD of the upstream repo.

The upstream `sources/config.yaml` exists and is the gftools-builder configuration for Josefin Slab (referencing `JosefinSlab.designspace` and `JosefinSlab-Italic.designspace`). The METADATA.pb correctly references it at `sources/config.yaml`.

## Conclusion

The repository URL and config_yaml are correct. However, the commit hash `61773366f7` in METADATA.pb was added by the fontc_crater batch and corresponds to a newer upstream commit (Dec 2024) than the actual onboarding commit (Nov 2024). The correct onboarding commit is likely `4e362ce130f2a56b24fe3d2654520f2f7e303bb9` ("rebuilt fonts with the STAT", 2024-11-15 16:26) which closely predates the google/fonts additions. Confidence is MEDIUM because the exact commit used for the "update fonts" push (321d1360e) is not stated in the commit message.
