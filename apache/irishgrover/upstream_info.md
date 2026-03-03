# Investigation: Irish Grover

## Summary

| Field | Value |
|-------|-------|
| Family Name | Irish Grover |
| Slug | irish-grover |
| License Dir | apache |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The font is stored under `apache/irishgrover/` with an Apache 2.0 license. The METADATA.pb has no `source` block at all.

The font history in google/fonts shows:
- `90abd17b4` — "Initial commit" — the font was present from the very beginning of the google/fonts repository
- `daa6505c6` — "hotfix-irishgrover: v1.001 added (#777)" — a hotfix that renamed the file from `IrishGrover.ttf` to `IrishGrover-Regular.ttf`

The copyright in METADATA.pb states: "Copyright (c) 2010 by Font Diner, Inc DBA Sideshow. All rights reserved."

The DESCRIPTION.en_us.html says:
> "Presenting Irish Grover! No, it's not a coveted new AKC breed. No, it's not a tasty seasonal pilsner. It's a fun, flamboyant, new display font by Squid that's way better than any of those possibilities. Sure and it's free for Pete's sake! And you can't say that about dogs or beer."

The designer is listed as "Sideshow" (Font Diner, Inc DBA Sideshow). Font Diner is a commercial type foundry; this font was donated to Google Fonts under Apache license. No GitHub repository has been identified for the upstream source. The font dates to 2010 and was contributed directly to Google Fonts without a tracked upstream repository.

No cached upstream repository was found in `upstream_repos/fontc_crater_cache/` for this family.

Given the Apache license and the vintage of the font (2010), it is likely that there is no open-source upstream repository. The font was contributed directly to Google Fonts by Font Diner/Sideshow.

## Conclusion

No upstream repository is known for this font. The font was contributed directly to google/fonts under Apache 2.0 license by Font Diner Inc / Sideshow. Investigation into Font Diner's website or archives may reveal source files, but there is likely no publicly accessible upstream repository. This font may be a case where `no_config_possible` applies due to the commercial foundry origin and lack of open source repository.

Action needed: Determine if Font Diner/Sideshow has a public source repository or if this font was contributed as binaries only. If no upstream repo exists, document as `missing_url` with a note that no upstream repository was found.
