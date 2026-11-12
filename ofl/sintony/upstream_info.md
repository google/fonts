**Model**: Claude Opus 4.6

# Sintony — Upstream Source Investigation

## Summary

Sintony is a modern sans-serif typeface designed by Eduardo Rodríguez Tunni (edu@tipo.net.ar / tipo.net.ar) and released in 2013. It was added to Google Fonts on 2013-02-27.

## Designer

Eduardo Rodríguez Tunni — tipo.net.ar

## Repository Search

A search for canonical upstream repositories was conducted on GitHub. The following repository was found:

- **etunni/sintony** (https://github.com/etunni/sintony) — repository owned by Eduardo Rodríguez Tunni (GitHub user `etunni`, confirmed as Eduardo Rodríguez Tunni via profile name and email edu@tipo.net.ar). The repository contained:
  - `sources/Sintony-GF-plus.glyphs` — Glyphs source file
  - `fonts/` — compiled TTF files

The repository was confirmed as non-archived with an active `master` branch.

## Commit

Latest commit: `be9cf7be562d566504ef1c8e52d41ce48535ced8` — "Update README.md"

This commit was verified via the GitHub API.

## Status

Source block was added pointing to `etunni/sintony` at commit `be9cf7be562d566504ef1c8e52d41ce48535ced8` on the `master` branch.

## Confidence

High — The repository is owned and maintained by the font designer, contains Glyphs source files, and matches the font metadata.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sintony/` referencing the upstream gftools-builder-compatible source at the pinned commit `be9cf7b` (`sources/Sintony-GF-plus.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.
