# Investigation: League Script

## Summary

| Field | Value |
|-------|-------|
| Family Name | League Script |
| Slug | league-script |
| License Dir | ofl |
| Repository URL | https://github.com/theleagueof/league-script-number-one |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/theleagueof/league-script-number-one"
}
```

## Investigation

The METADATA.pb has a `repository_url` pointing to `https://github.com/theleagueof/league-script-number-one` but no commit hash.

The google/fonts git history for `ofl/leaguescript/LeagueScript-Regular.ttf` shows:
- `17eecaf5f` — "ofl/leaguescript: v1.001 added. Fixed name table OS X validation failure."
- `90abd17b4` — "Initial commit" (earliest onboarding)

The upstream repo at `upstream_repos/fontc_crater_cache/theleagueof/league-script-number-one/` contains:
- `LeagueScriptNumberOne.otf` — prebuilt OTF
- `source/LeagueScriptNumberOne.ufo` — UFO source
- `source/LeagueScriptNumberOne.vfb` — FontLab VFB source
- `source/LeagueScriptNumberOne.bak`

The repo has a single commit: `225add0` ("Initial commit with readme and licenses"). There is no `config.yaml` for gftools-builder.

Since the repo has only one commit, that commit is the most likely candidate for the onboarding reference, though no explicit reference was found in the google/fonts commit messages.

## Conclusion

The repository URL is present but the commit hash is missing. The upstream repo has only one commit (`225add0`), which is likely the reference commit. The sources include UFO format which could support an override `config.yaml`, but the VFB file is the primary design source (FontLab format).

## Commit Added (MEDIUM confidence)

Commit `225add0b37cf8268759ba4572e02630d9fb54ecf` was determined by **date_correlation**. Found the latest upstream commit before the binary modification date in google/fonts (2019-07-09). This assumes the upstream HEAD at onboarding time was the commit used.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Upstream has both compatible sources (.ufo) and legacy `.sfd`/`.vfb` archives at the pinned commit `225add0` (upstream legacy: .vfb in source/). Added an override `config.yaml` in `ofl/leaguescript/` that references the compatible sources only (`source/LeagueScriptNumberOne.ufo`). The legacy archives are retained upstream for historical reference but are not consumed by gftools-builder. `google-fonts-sources` auto-detects the override on the next regeneration of crater's `targets.json`.
