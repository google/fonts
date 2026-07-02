# Liu Jian Mao Cao — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/liujianmaocao"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LiuJianMaoCao-Regular.ttf"
    dest_file: "LiuJianMaoCao-Regular.ttf"
  }
  branch: "master"
}
```

The source block has a repository_url and branch, but is missing a commit hash. There is no `config_yaml` field, which is correct because an override `config.yaml` exists in the google/fonts family directory.

## Repository Analysis

- **Repository**: https://github.com/googlefonts/liujianmaocao
- **Branch**: `master`
- **Total commits**: 14 (from initial commit on 2019-02-13 to latest on 2021-10-07)
- **Latest commit (HEAD)**: `e589ccd1fe37fa9d2076a52096a3e3992489ad2c` — "legacy ci travis files deleted2" (2021-10-07)
- **Repository status**: Clean, up-to-date with remote

The repository was originally at `m4rc1e/liujianmaocao` (Marc Foley's account) and was later transferred to the `googlefonts` organization. The initial onboarding (v1.000) and v1.001 update both referenced the original `m4rc1e/liujianmaocao` URL.

### Source Files

- `sources/LiuJianMaoCao.glyphs` — primary Glyphs source file (48 MB)
- `sources/build.sh` — legacy build script (uses gftools fix-dsig and fix-nonhinting)
- `fonts/ttf/LiuJianMaoCao-Regular.ttf` — pre-compiled binary (4,951,804 bytes)

The source file (`LiuJianMaoCao.glyphs`) was last modified at commit `fc46ef0` (2021-10-07, "designers info fixed"). The pre-compiled TTF in the upstream repo matches the one in google/fonts exactly (MD5: `0e729b8fc3692f9140d56f7df70f612c`).

### No config.yaml in Upstream

The upstream repository does not contain a `config.yaml` file. It only has a legacy `sources/build.sh` script. An override `config.yaml` was created in the google/fonts family directory as part of the config_yaml enrichment effort (commit `5ddf312e6`, 2026-02-20).

## Onboarding History

### v1.000 — Initial onboarding (2019-02-13)

- **google/fonts commit**: `22fdf57e1`
- **Upstream commit referenced**: `8a2fbcb9656a5547775f422da34f3c7c2027c307` (Initial commit at `m4rc1e/liujianmaocao`)
- Font was initially added with a binary TTF from the upstream repo.

### v1.001 — Update (2019-05-08)

- **google/fonts commit**: `64e390bfa`
- **Upstream commit referenced**: `f922204750b6a84e62fddb4da33494df39beb27c` ("umcamelcase name" at `m4rc1e/liujianmaocao`)
- Updated the binary TTF.

### v1.003 — Latest update (2021-10-14)

- **google/fonts commit**: `0bf38a8a3` via PR #3927
- **Upstream commit referenced**: `e589ccd1fe37fa9d2076a52096a3e3992489ad2c` (HEAD of `googlefonts/liujianmaocao`)
- **Onboarded by**: Viviana Monsalve (with Marc Foley as co-author)
- **Tool used**: gftools-packager
- The PR body explicitly stated: "Liu Jian Mao Cao Version 1.003 taken from the upstream repo https://github.com/googlefonts/liujianmaocao at commit e589ccd1fe37fa9d2076a52096a3e3992489ad2c."
- The binary TTF in google/fonts matches the one at this commit exactly (identical checksums).
- This commit (`e589ccd`) is the HEAD of the master branch — no further upstream changes exist after the onboarding.

### Source block added (2024-04-03)

- **google/fonts commit**: `66f91f10f` — "Merge upstream.yaml into METADATA.pb"
- The source block with repository_url and file mappings was added, but without a commit hash.

### Override config.yaml added (2026-02-20)

- **google/fonts commit**: `5ddf312e6` — "Add config_yaml enrichment for 82 font families"
- An override `config.yaml` was created pointing to `sources/LiuJianMaoCao.glyphs`.

## Build Configuration

- **Upstream config.yaml**: None (only a legacy `build.sh` script)
- **Override config.yaml in google/fonts**: Yes, created during enrichment work

Override config.yaml content:
```yaml
sources:
  - sources/LiuJianMaoCao.glyphs
```

This is correct. The source file `sources/LiuJianMaoCao.glyphs` exists in the upstream repo at the referenced commit. Since the override config exists locally, the `config_yaml` field is correctly omitted from METADATA.pb.

## Findings

1. **Commit hash is missing from METADATA.pb**: The source block lacks a `commit` field. The correct commit hash is `e589ccd1fe37fa9d2076a52096a3e3992489ad2c`, which was the commit used for the v1.003 onboarding (PR #3927, merged 2021-10-14). This was verified by:
   - The gftools-packager message in the PR body explicitly referencing this commit
   - Identical binary file checksums between upstream (at this commit) and google/fonts
   - This commit being HEAD of master with no subsequent changes

2. **Repository URL is correct**: The repository was transferred from `m4rc1e/liujianmaocao` to `googlefonts/liujianmaocao`. The current METADATA.pb correctly uses the `googlefonts` URL.

3. **Override config.yaml is in place**: The google/fonts directory already contains a working override `config.yaml` pointing to the correct source file. No `config_yaml` field is needed in METADATA.pb.

4. **Pre-compiled binary**: The upstream repo ships a pre-compiled TTF at `fonts/ttf/LiuJianMaoCao-Regular.ttf`, which is the same file used in google/fonts. With gftools-builder and the override config, the font could be rebuilt from the `.glyphs` source.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/googlefonts/liujianmaocao"
  commit: "e589ccd1fe37fa9d2076a52096a3e3992489ad2c"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LiuJianMaoCao-Regular.ttf"
    dest_file: "LiuJianMaoCao-Regular.ttf"
  }
  branch: "master"
}
```

The only change needed is adding the `commit` field. The `config_yaml` field should remain absent since the override config.yaml in the google/fonts directory is auto-detected by google-fonts-sources.
