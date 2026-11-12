# Investigation: Bitcount Single Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bitcount Single Ink |
| Slug | bitcount-single-ink |
| License Dir | ofl |
| Repository URL | https://github.com/petrvanblokland/TYPETR-Bitcount |
| Commit Hash | 89e7994f73b7f5ced80e7cf493d40be9e66ff82f |
| Config YAML | sources/config.yaml (upstream, but inadequate — needs correction) |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/petrvanblokland/TYPETR-Bitcount"
  commit: "89e7994f73b7f5ced80e7cf493d40be9e66ff82f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/variable/BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
    dest_file: "BitcountSingleInk[CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL, commit hash, and `config_yaml: "sources/config.yaml"`.

The history shows the initial addition at commit `9cc1c52fc`, then a batch update by commit `19cdcec59` (March 31, 2025, fontc_crater batch) which added `config_yaml: "sources/config.yaml"` and changed the commit hash to `653fc48a72cf3b6a293f6fc207a770f537921889`. Commit `cdcbeee55` ("Bitcount Single Ink: Version 1.001 added") then updated the commit hash to `89e7994f73b7f5ced80e7cf493d40be9e66ff82f`, confirmed by its body: "Taken from the upstream repo https://github.com/petrvanblokland/TYPETR-Bitcount at commit https://github.com/petrvanblokland/TYPETR-Bitcount/commit/89e7994f73b7f5ced80e7cf493d40be9e66ff82f."

The commit `89e7994f73b7f5ced80e7cf493d40be9e66ff82f` is confirmed valid (September 5, 2025).

**Problem**: The `config_yaml: "sources/config.yaml"` refers to the upstream `sources/config.yaml`, which only contains `familyName: Bitcount` — an incomplete gftools-builder configuration. Unlike the other Bitcount Ink families (Grid Double Ink, Grid Single Ink, Ink, Prop Double Ink), there is no local override `config.yaml` in the `ofl/bitcountsingleink/` directory within google/fonts.

This is the same issue as Bitcount Prop Single Ink. Both families are inconsistent with the other Bitcount Ink families which have proper override `config.yaml` files in google/fonts and no `config_yaml` set in METADATA.pb.

The fix would be to:
1. Remove `config_yaml` from METADATA.pb, and
2. Add a proper override `config.yaml` to the `ofl/bitcountsingleink/` directory in google/fonts

(Consistent with the pattern used by all other Bitcount Ink families.)

## Conclusion

The commit hash is correct. However, `config_yaml: "sources/config.yaml"` points to an inadequate upstream config that only sets `familyName: Bitcount`. This family needs correction: a proper override `config.yaml` should be added to the google/fonts directory, and the `config_yaml` field should be removed from METADATA.pb, matching the pattern used by the other Bitcount Ink families.

### Earlier (2025-09-11)

- **2025-09-11** — Emma Marichal, commit [`711bcf6c1`](https://github.com/google/fonts/commit/711bcf6c1) ("bump version"): same-day binary update following the v1.001 onboarding (binary-only, file size unchanged at 430912 bytes — internal version-string bump).

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
METADATA.pb pointed `config_yaml` at the upstream `sources/config.yaml`. The shared upstream repo's fontc_crater build failed with the error `missing field \`sources\``.

### Investigation
The upstream `sources/config.yaml` contains only `familyName: Bitcount`, with no `sources:` field — it is not a gftools-builder config. Bitcount is built by a custom Python/COLRv1 pipeline (`Makefile` → `scripts/build.py`) that cannot be expressed as a gftools-builder `config.yaml`. The recorded commit `89e7994f` is correct (v1.001).

### Actions taken
The misleading `config_yaml: "sources/config.yaml"` field was removed from the METADATA.pb `source` block, addressing the inconsistency identified above. No override `config.yaml` was created: the family's build is a bespoke pipeline that gftools-builder cannot reproduce, so it is recorded as not reproducible rather than given a placeholder config.

### Final state
METADATA.pb retains the correct repository URL and commit; the misleading `config_yaml` reference is gone.
