# Didact Gothic

## Summary

| Field | Value |
|---|---|
| **Family name** | Didact Gothic |
| **Designer** | Daniel Johnson, Cyreal |
| **License** | OFL |
| **Date added** | 2011-05-04 |
| **Repository URL** | https://github.com/ossobuffo/didact-gothic |
| **Commit** | `adc3106364c1c79dca374283822289a83cf41a77` |
| **Config YAML** | Override in google/fonts |
| **Status** | complete |

## Upstream Repository

The upstream repo at `ossobuffo/didact-gothic` contains:
- `sources/Didact Gothic.glyphs` - Glyphs source file (current buildable source)
- `old/version-20110429/DidactGothic.sfd` - Legacy SFD source
- `old/version-20110429/DidactGothic.ufo` - Legacy UFO source
- No `config.yaml` file anywhere in the repository

The repo has very few commits, with HEAD at `8f55b34` (a merge commit for PR #9).

## Commit Verification

The commit `adc3106` ("fonts | sources: v2.101 added.") was authored by Marc Foley on 2017-01-25. This matches the google/fonts commit `4be3f642b` ("didactgothic: v2.101 added. (#607)") also by Marc Foley on the same date. The commit is the second-to-last in the repo (HEAD is the merge commit `8f55b34`).

The font file was also touched by the deploy commit `76adaf1d2` in google/fonts, but that was a repo-wide restructure and did not change the font content.

## Source Block Status

The METADATA.pb currently has:
```
source {
  repository_url: "https://github.com/ossobuffo/didact-gothic"
}
```

The commit hash `adc3106` and repository URL were added in the batch commit `9a14639f3`. No config_yaml field is set because the upstream repo has no config.yaml file.

## Build Configuration

The upstream repo has a `.glyphs` source file but no `config.yaml`. A config.yaml would need to be created (either as an override in google/fonts or submitted to the upstream repo) to make this family buildable with gftools-builder.

## Conclusion

- Repository URL: Verified correct
- Commit hash: Verified correct (`adc3106` = v2.101, the last content update)
- Config YAML: Missing from upstream; needs override config.yaml
- Status: `missing_config` - needs a config.yaml to be buildable

## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - "sources/Didact Gothic.glyphs"
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.
