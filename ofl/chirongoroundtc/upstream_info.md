# Chiron GoRound TC - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Chiron GoRound TC |
| Designer | Tamcy |
| License | OFL |
| Date Added | 2025-06-21 |
| Repository URL | https://github.com/chiron-fonts/chiron-go-round-tc |
| Commit | `803fb2f0423d5ce9683859cdaa19942896abaf74` |
| Branch | source |
| Config YAML | `scripts/config.yaml` (in upstream on source branch) |
| Status | complete |

## How URL Found

The repository URL `https://github.com/chiron-fonts/chiron-go-round-tc` is documented in the METADATA.pb source block on google/fonts main, set during the initial onboarding commit `b6f9abe68` (2025-06-21).

## How Commit Determined

The font was onboarded on 2025-06-21 and then updated on 2025-06-24 (commit `879c0b0d5` in google/fonts: "Updating to v 1.002"). The update changed the font binary from 50,967,852 bytes to 51,170,304 bytes.

On the upstream `source` branch, the commit history shows:
- `cb58a24` (2025-06-23) - "v1.002 sources"
- `803fb2f` (2025-06-24) - "Fixed a couple things for FB" by Aaron Bell
- `d51d782` (2025-06-22) - "Updating build script"
- `916245e` (2025-06-27) - Merge pull request #5 from aaronbell/source

The font binary at commit `803fb2f` is 51,170,304 bytes, matching exactly the size of the font in google/fonts after the v1.002 update. This confirms `803fb2f` as the commit from which the font was built.

**Note**: PR #9596 in google/fonts proposed a different commit `e7501a7156fb55387f45348cc89b91aeb38dd61b`, but this commit (2025-06-24, "update workflow") only changed a GitHub Actions workflow file and did not affect font sources. The commit `803fb2f` is more accurate as it is the actual commit that produced the font binary.

## Config YAML Status

**config.yaml exists in upstream** at `scripts/config.yaml` on the `source` branch. Verified at commit `803fb2f`:

```yaml
sources:
  - ChironGoRoundTC.designspace
axisOrder:
  - wght
familyName: Chiron GoRound TC
outputDir: ./
stat:
  ChironGoRoundTC[wght].ttf:
    - name: Weight
      tag: wght
      values:
        - name: ExtraLight
          value: 200
        - name: Light
          value: 300
        - name: Regular
          value: 400
          linkedValue: 700
          flags: 2
        - name: Medium
          value: 500
        - name: SemiBold
          value: 600
        - name: Bold
          value: 700
        - name: ExtraBold
          value: 800
        - name: Black
          value: 900
autohintTTF: False
buildStatic: False
```

No override config.yaml exists in the google/fonts family directory.

## Verification

- Repository URL verified: accessible at https://github.com/chiron-fonts/chiron-go-round-tc
- Commit `803fb2f` verified via GitHub API: exists on source branch, authored 2025-06-24 by Aaron Bell
- Font binary size matches: 51,170,304 bytes at commit `803fb2f` matches google/fonts after v1.002 update
- config.yaml verified at `scripts/config.yaml` on source branch
- Current METADATA.pb on main only has repository_url and branch; commit and config_yaml are in pending PR branches

## Confidence Level

**HIGH** - The commit hash is verified by matching font binary size. The config.yaml path is confirmed to exist at the referenced commit on the source branch. The font engineer (Aaron Bell) authored both the upstream commit and the google/fonts update.

## Open Questions

- The METADATA.pb on google/fonts main currently lacks the `commit` and `config_yaml` fields. Two different pending changes propose different commits:
  - Batch update `4fd9e239` proposes `803fb2f` + `scripts/config.yaml` (correct)
  - PR #9596 commit `0c8d6246` proposes `e7501a7` (workflow-only commit, less accurate)
- These pending changes need to be merged to complete the METADATA.pb source block.
