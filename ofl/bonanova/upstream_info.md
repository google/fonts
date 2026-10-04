# Investigation: Bona Nova

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bona Nova |
| Slug | bona-nova |
| License Dir | ofl |
| Repository URL | https://github.com/kosmynkab/Bona-Nova |
| Commit Hash | a5cbdfb8741af20ea5bfe252f0128beed6c8beed |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/kosmynkab/Bona-Nova"
  commit: "a5cbdfb8741af20ea5bfe252f0128beed6c8beed"
  files {
    source_file: "fonts/ttf/BonaNova-Regular.ttf"
    dest_file: "BonaNova-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/BonaNova-Bold.ttf"
    dest_file: "BonaNova-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/BonaNova-Italic.ttf"
    dest_file: "BonaNova-Italic.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Bona Nova is a serif typeface by Capitalics (Mateusz Machalski, Andrzej Heidrich), added to Google Fonts on 2021-04-13. It includes Regular, Bold, and Italic static weights with support for Latin, Cyrillic, Greek, Hebrew, and Vietnamese scripts.

### Git History

The font TTF files were last updated by google/fonts commit `728f6da02` (PR #3275, 2021-04-13):

```
Bona Nova: Version 4.001; ttfautohint (v1.8.3) added (#3275)

Bona Nova Version 4.001; ttfautohint (v1.8.3) taken from the upstream repo
https://github.com/kosmynkab/Bona-Nova at commit
https://github.com/kosmynkab/Bona-Nova/commit/a5cbdfb8741af20ea5bfe252f0128beed6c8beed.
```

Note: The PR #3275 body originally referenced a different commit (`fdc7db4c1fcd4d63a922ea8797881a39d3a62caa`), but that commit no longer exists in the upstream repository, likely due to a subsequent force-push that rewrote history.

The commit hash `a5cbdfb8` and `config_yaml: "sources/config.yaml"` were both added to METADATA.pb by commit `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list"), porting data from the fontc_crater targets list.

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/kosmynkab/Bona-Nova/` (shallow clone). Commit `a5cbdfb8` is the HEAD of the main branch (message: "remove fontbakery report", date: 2021-04-13). It is the only visible commit due to the shallow clone.

The `sources/config.yaml` exists at this commit and contains:
```yaml
sources:
  - BonaNova.glyphs
  - BonaNova-Italic.glyphs
familyName: Bona Nova
buildVariable: False
```

This is a valid gftools-builder configuration for building static fonts from Glyphs sources. The referenced TTF files exist at `fonts/ttf/BonaNova-Regular.ttf`, `fonts/ttf/BonaNova-Bold.ttf`, and `fonts/ttf/BonaNova-Italic.ttf` in the repo at this commit.

### Verification

- Repository URL: Confirmed (stated in copyright string, gftools-packager commit, and upstream.yaml)
- Commit hash: The recorded commit `a5cbdfb8` is the current HEAD. The original onboarding commit (`fdc7db4c`) no longer exists in the repo (likely force-pushed away). The fontc_crater targets list adopted `a5cbdfb8` as the reference.
- Config YAML: `sources/config.yaml` exists and is valid at the recorded commit
- Source files: All three TTF files exist at `fonts/ttf/` at the recorded commit

## Conclusion

The METADATA.pb source block is complete and accurate. The repository URL, commit hash, file mappings, branch, and config_yaml path are all set correctly. The only caveat is that the recorded commit `a5cbdfb8` differs from the original onboarding commit (`fdc7db4c`) referenced in PR #3275 — the upstream repository was apparently force-pushed after onboarding. The current HEAD commit is the best available reference, and it has been adopted by fontc_crater. No action needed unless the original onboarding commit needs to be reconstructed.
