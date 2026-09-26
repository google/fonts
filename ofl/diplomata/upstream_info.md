# Diplomata

## Summary

| Field | Value |
|---|---|
| **Family name** | Diplomata |
| **Designer** | Eduardo Tunni |
| **License** | OFL |
| **Date added** | 2012-01-25 |
| **Repository URL** | https://github.com/etunni/diplomata |
| **Commit** | `32dc35e6b420631acc10808e1f92f74e3048e81d` |
| **Branch** | master |
| **Config YAML** | `sources/diplomata.yaml` |
| **Status** | complete |

## Upstream Repository

The upstream repo at `etunni/diplomata` is shared between Diplomata and Diplomata SC. It contains:
- `sources/Diplomata.glyphs` - Glyphs source for Diplomata
- `sources/DiplomataSC.glyphs` - Glyphs source for Diplomata SC
- `sources/diplomata.yaml` - gftools-builder config for Diplomata
- `sources/diplomatasc.yaml` - gftools-builder config for Diplomata SC
- `fonts/diplomata/ttf/Diplomata-Regular.ttf` - Pre-built TTF
- `fonts/diplomatasc/ttf/DiplomataSC-Regular.ttf` - Pre-built TTF

The repo has a single commit (`32dc35e`), which is a merge commit for PR #1 from emmamarichal/master.

## Commit Verification

The commit `32dc35e` ("Merge pull request #1 from emmamarichal/master - Diplomata and DiplomataSC update") was authored by Eduardo Rodriguez Tunni on 2023-02-16. This matches the gftools-packager commit `4ceb8d23f` in google/fonts (by Emma Marichal, same date), which states: "taken from the upstream repo https://github.com/etunni/diplomata at commit https://github.com/etunni/diplomata/commit/32dc35e6b420631acc10808e1f92f74e3048e81d".

This is the only commit in the repo, and is confirmed as the correct onboarding commit.

## Config YAML

The config at `sources/diplomata.yaml` contains:
```yaml
sources:
  - Diplomata.glyphs
outputDir: "../fonts/diplomata"
```

## Source Block Status

The METADATA.pb has a complete source block with:
- repository_url, commit, branch, config_yaml, and files entries
- All data was populated in commits `53995c52a` and `66f91f10f`

## Conclusion

- Repository URL: Verified correct
- Commit hash: Verified correct (`32dc35e` is the sole commit, confirmed by gftools-packager)
- Config YAML: Verified at `sources/diplomata.yaml`
- Status: `complete` - all fields populated and verified
