# Google Sans

**Model**: Claude Opus 5.5
**Date**: 2026-10-06

## Initial state

METADATA.pb had no source block. The upstream repository,
https://github.com/googlefonts/googlesans, was private when fontc_crater first listed it, by
hand and with an access token; it is public now.

## Actions taken

- The source commit was identified from the shipped fonts: both carry
  `Version 14.000;[08f2ac800]` in name ID 5. GitHub still serves commit `08f2ac800`
  (https://github.com/googlefonts/googlesans/commit/08f2ac8009f08ef6d5e302ebbee3bdae48977d4b),
  but no branch contains it: it is from the history the repository had before it was
  published. The public history holds it as `5c8f512c5` (same author, date and message,
  "Merge pull request #731 from googlefonts/remove-factions"; the trees differ only by one
  internal PDF removed from `docs/`). `5c8f512c5` is on `main` and is the `v14.000` release
  tag, the version google/fonts#10960 onboarded.
- Both shipped files were found byte-identical to `build/GoogleSans/variable/` in the
  `v14.000` release archive.
- A source block was added: repository, commit `5c8f512c5`, the `v14.000` release archive
  with the two font files, `sources/config.yaml`, branch `main`. `OFL.txt` is not mapped:
  the release archive does not contain it.

## Final state

The source block points at `5c8f512c5` (tag `v14.000`) and at the release archive whose
two variable fonts are the shipped files, byte for byte. google-fonts-sources can now find
the repository, so fontc_crater no longer needs to list it by hand.
