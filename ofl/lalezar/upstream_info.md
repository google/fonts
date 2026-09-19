# Investigation: Lalezar

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lalezar |
| Slug | lalezar |
| License Dir | ofl |
| Repository URL | https://github.com/BornaIz/Lalezar |
| Commit Hash | 238701c4241f207e92515f845a199be9131c1109 |
| Config YAML | local override (`config.yaml`) |
| Status | complete |
| Confidence | HIGH |

## Initial state

`METADATA.pb` referenced commit `c3e0eae24240424069cd8c1b4350a6101346fb7b` (Aug 22, 2016, "Merge pull request #9"). Building from that revision failed with `missing source 'sources/Lalezar.glyphs'`.

The local override `ofl/lalezar/config.yaml` already pointed to `sources/Lalezar.glyphs`.

## Investigation

The full upstream history at `https://github.com/BornaIz/Lalezar` was reviewed. Key commits:

- `c3e0eae` — Aug 22, 2016 — Merge PR #9 (the previously recorded commit). At this revision the repository contains `Glyphs files/Lalezar_v3.gyphs` (note typo) — there is no `sources/` directory.
- `ded35db` — Jan 23, 2017 — `sources: renamed from Glyphs files`. First commit where the `sources/` directory exists.
- `32b5042` — Jan 23, 2017 — `Lalezar_v3.gyphs: renamed to Lalezar.glyphs.` First commit where `sources/Lalezar.glyphs` exists at the canonical path.
- `8c9d2ad` — Feb 27, 2017 — Merge PR #11 from m4rc1e/gf (Marc Foley's onboarding prep).
- `f3631c6` — Feb 28, 2017 — `fonts | sources: fixed OT features`.
- `238701c` — Feb 28, 2017 — Merge PR #12 from m4rc1e/gf. Last upstream commit prior to the binary modification date in google/fonts (`Lalezar-Regular.ttf` mtime 2017-05-01) and matching `date_added: "2017-02-28"` already recorded in METADATA.pb.

The two 2021 commits (`f7e9f54`, `1a9b729`) postdate the google/fonts binary and are not relevant to the original onboarding.

The previous `c3e0eae` value originated from an automated `tag_match` heuristic that matched a 1.003 version tag whose date was on or before the binary mtime. The heuristic ignored that the source file required by `config.yaml` did not yet exist at that revision.

## Actions taken

- `METADATA.pb` `source.commit` updated from `c3e0eae24240424069cd8c1b4350a6101346fb7b` to `238701c4241f207e92515f845a199be9131c1109`.
- `config.yaml` left unchanged — `sources/Lalezar.glyphs` is present at `238701c` and the existing override is correct.

## Final state

```
source {
  commit: "238701c4241f207e92515f845a199be9131c1109"
  repository_url: "https://github.com/BornaIz/Lalezar"
}
```

`config.yaml` (local override):

```yaml
sources:
  - sources/Lalezar.glyphs
```

**Model**: Claude Opus 4.7
