# Investigation: Decovar Alpha

## Summary

| Field | Value |
|-------|-------|
| Family Name | Decovar Alpha |
| Slug | decovar-alpha |
| License Dir | ofl |
| Repository URL | https://github.com/TypeNetwork/fb-Decovar |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_commit |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

(No METADATA.pb exists for this family. It is an Early Access font.)

## Investigation

The family directory is at `ofl/decovaralpha/` and contains:
- `DecovarAlpha-VF.ttf`
- `DESCRIPTION.en_us.html`
- `EARLY_ACCESS.category` (value: "Sans Serif")
- `OFL.txt`

**No METADATA.pb exists.** This is an Early Access font that predates the modern METADATA.pb onboarding process.

### Git History

```
bc4d03ae3  2017-08-30  decovaralpha/Decovar-VF.ttf -> DecovarAlpha-VF.ttf
3231ca2f6  2017-08-30  decovar -> decovaralpha + update to latest version (#1183)
fda8d1f9c  2017-08-14  Add Decovar to Early Access (#656)
```

- **PR #656** (commit `fda8d1f9c`, 2017-08-14, Dave Crossland): Initial onboarding as "decovar" — added `Decovar-VF.ttf`, `DESCRIPTION.en_us.html`, `EARLY_ACCESS.category`, and `OFL.txt` to `ofl/decovar/`.
- **PR #1183** (commit `3231ca2f6`, 2017-08-30, Dave Crossland): Renamed directory from `ofl/decovar/` to `ofl/decovaralpha/` and updated the TTF to a newer version (295,396 bytes → 295,460 bytes). The PR title is "decovar -> decovaralpha + update to latest version".
- **commit `bc4d03ae3`** (2017-08-30, Dave Crossland): Renamed the font file from `Decovar-VF.ttf` to `DecovarAlpha-VF.ttf`.

### Upstream Repository

The `DESCRIPTION.en_us.html` links directly to the upstream repository:
> "To learn more about this project, visit [github.com/TypeNetwork/fb-Decovar](https://github.com/TypeNetwork/fb-Decovar)"

The `OFL.txt` copyright line reads:
> "Copyright 2016 The Decovar Project Authors (info@fontbureau.com)"

The upstream is **https://github.com/TypeNetwork/fb-Decovar** (originally a Font Bureau project by David Berlow, now maintained under TypeNetwork).

### Upstream Repo Not in Cache

The repository `TypeNetwork/fb-Decovar` is **not** cloned in `upstream_repos/fontc_crater_cache/TypeNetwork/` (only `Arimo` and `Assistant` are cached there).

### No config.yaml Known

Without access to the upstream repo, the config.yaml status cannot be confirmed. Given the early nature of this project (2017) and that it is a variable font with likely `.glyphs` or `.designspace` sources, a config.yaml may or may not exist.

### Exact Commit Unknown

The PR #1183 commit message does not include an upstream commit hash. The exact commit in `TypeNetwork/fb-Decovar` that corresponds to the August 2017 update is unknown without inspecting the upstream repository.

## Conclusion

This Early Access font has a clearly identified upstream repository at `https://github.com/TypeNetwork/fb-Decovar`. A METADATA.pb with a source block needs to be created, referencing this upstream. The exact commit hash used for the August 2017 update needs to be determined by inspecting the upstream repository history around that date. Once the upstream repo is cloned and the correct commit identified, a config.yaml path (or override) can be determined.

**Action needed**: Clone `TypeNetwork/fb-Decovar` to the fontc_crater_cache (when disk space allows), identify the commit from around 2017-08-30, check for config.yaml, and create a METADATA.pb with source block.
