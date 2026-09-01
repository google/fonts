# Diplomata SC

## Summary

| Field | Value |
|---|---|
| **Family name** | Diplomata SC |
| **Designer** | Eduardo Tunni |
| **License** | OFL |
| **Date added** | 2012-01-25 |
| **Repository URL** | https://github.com/etunni/diplomata |
| **Commit** | `32dc35e6b420631acc10808e1f92f74e3048e81d` |
| **Branch** | master |
| **Config YAML** | `sources/diplomatasc.yaml` |
| **Status** | complete |

## Upstream Repository

The upstream repo at `etunni/diplomata` is shared with the Diplomata family. It contains:
- `sources/DiplomataSC.glyphs` - Glyphs source for Diplomata SC
- `sources/diplomatasc.yaml` - gftools-builder config for Diplomata SC
- `fonts/diplomatasc/ttf/DiplomataSC-Regular.ttf` - Pre-built TTF

See the [Diplomata investigation](diplomata.md) for full repo details.

## Commit Verification

The commit `32dc35e` is the same as used for Diplomata (both families share the same upstream repo and commit). This was confirmed by the gftools-packager commit `6a8620423` in google/fonts (by Emma Marichal, 2023-02-16), which states: "taken from the upstream repo https://github.com/etunni/diplomata at commit https://github.com/etunni/diplomata/commit/32dc35e6b420631acc10808e1f92f74e3048e81d".

## Config YAML

The config at `sources/diplomatasc.yaml` contains:
```yaml
sources:
  - DiplomataSC.glyphs
outputDir: "../fonts/diplomatasc"
```

## Source Block Status

The METADATA.pb has a complete source block with:
- repository_url, commit, branch, config_yaml, and files entries
- All data was populated in the same commits as Diplomata

## Conclusion

- Repository URL: Verified correct (shared repo with Diplomata)
- Commit hash: Verified correct (`32dc35e` is the sole commit, confirmed by gftools-packager)
- Config YAML: Verified at `sources/diplomatasc.yaml`
- Status: `complete` - all fields populated and verified
