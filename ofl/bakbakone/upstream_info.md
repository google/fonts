# Bakbak One

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Designer**: Saumya Kishore, Sanchit Sawaria

## Source Data

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| repository_url   | https://github.com/googlefonts/bakbak                    |
| commit           | b53b9c31c16f0021b7c206a57a8f04a4d382bc67                 |
| config_yaml      | sources/builder.yaml                                     |
| branch           | master                                                   |
| primary_script   | Deva                                                     |

## Investigation

### Repository URL

The METADATA.pb already contained `repository_url: "https://github.com/googlefonts/bakbak"`. The cached upstream repo at `upstream_repos/fontc_crater_cache/googlefonts/bakbak` confirmed the remote matches this URL. The repo was clean with no local modifications.

### Commit Hash

The upstream repository has only one commit visible in the shallow clone: `b53b9c3` ("Added fractions", 2021-12-16, by Yanone). This is the HEAD of the `master` branch and the only commit on it.

**Onboarding history in google/fonts:**

1. **PR #3810** (merged 2021-09-24, by aaronbell): Initial onboarding of Bakbak One Version 1.002. The gftools-packager message referenced upstream commit `eee2dc2a6da7fe3d5e636180be4f30a814866ac2`, which is no longer available in the shallow clone. This was the first time the binary appeared in google/fonts.

2. **PR #4176** (merged 2022-01-11, by Yanone): Updated to Bakbak Version 1.003. The PR body stated "Added fractions, Renamed remaining instances of BakBak to Bakbak, Added devanagari to METADATA.pb." This PR directly used the binary from the upstream repo.

The METADATA.pb references commit `b53b9c31c16f0021b7c206a57a8f04a4d382bc67`, which corresponds to the "Added fractions" commit dated 2021-12-16. This commit predates the PR #4176 merge date (2022-01-11), making it a plausible source for the Version 1.003 update.

**Binary verification**: The SHA-256 hash of `BakbakOne-Regular.ttf` in google/fonts (`238dd2cf...`) matched exactly with the file at the referenced commit in the upstream repo. This confirmed the commit hash is correct.

### Config (builder.yaml)

The upstream repo contained `sources/builder.yaml` at the referenced commit with the following content:

```yaml
sources:
  - Bakbak.glyphs
familyName: "Bakbak One"
buildTTF: true
buildOTF: false
buildWebfont: false
buildVariable: false
```

The METADATA.pb correctly referenced this as `config_yaml: "sources/builder.yaml"`. The source file `Bakbak.glyphs` was confirmed present at the referenced commit. No override config.yaml was needed since the upstream repo already had a valid build configuration.

### Source Files at Referenced Commit

The `files` block in METADATA.pb mapped:
- `fonts/ttf/BakbakOne-Regular.ttf` -> `BakbakOne-Regular.ttf`
- `OFL.txt` -> `OFL.txt`

Both files were confirmed present at the referenced commit.

## Conclusion

The source block in METADATA.pb was already complete and correct. The repository URL, commit hash, branch, config_yaml path, and file mappings were all verified. The binary file hash matched exactly between google/fonts and the upstream repo at the referenced commit. No changes were needed.

**Confidence**: HIGH
