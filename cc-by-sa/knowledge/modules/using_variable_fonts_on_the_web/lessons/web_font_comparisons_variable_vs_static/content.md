How efficient are variable web fonts when compared to static fonts? As with most questions related to typography, the answer—for better or worse—is “it depends”.

Though exact numbers will vary for every project, examining a few typical scenarios can be useful for general reference. Below are examples of fairly standard typographic palettes along with comparative estimates about the effects on file sizes and loading times.

The test results below are based on a fairly standard sans-serif typeface ([HEX Franklin](https://hex.xyz/HEX_Franklin/)) with about 325 glyphs and fairly basic OpenType features and auto-hinting. The static fonts were CFF-flavored and the variable fonts were TTF-flavored. (CFF-flavored variable fonts provide even smaller file sizes comparatively, but weren’t used for the test because they aren’t as widely supported.) All the test fonts were compressed in the WOFF2 web font format.

Load time estimates are based on a standard of 500 kB per second for transfer times and 0.1 second per file for additional latency. These are ballpark numbers that won’t be as relevant for every project, but can be used as a starting point for other estimates.

## Type Palette #1
Regular, Bold
(2 variants on 1 axis, made from 2 sources)

|  | w/ static fonts | w/ variable fonts | total savings | % savings |
|:--|:--|:--|:--|:--|
| # of font files | 2 | 1 | 1 | 50% |
| Total file size | 27 kB | 17 kB | 10 kB | 37% |
| Transfer time | 0.05 sec | 0.03 sec | 0.02 sec | 37% |
| Additional latency | 0.2 sec | 0.1 sec | 0.1 sec | 50% |
| Total load time | 0.25 sec | 0.13 sec | 0.12 sec | 47% |

## Type Palette #2
Regular, Semibold, Bold
(3 variants on 1 axis, made from 2 sources)

|  | w/ static fonts | w/ variable fonts | total savings | % savings |
|:--|:--|:--|:--|:--|
| # of font files | 3 | 1 | 2 | 67% |
| Total file size | 41 kB | 17 kB | 24 kB | 59% |
| Transfer time | 0.08 sec | 0.03 sec | 0.05 sec | 59% |
| Additional latency | 0.3 sec | 0.1 sec | 0.2 sec | 67% |
| Total load time | 0.38 sec | 0.13 sec | 0.25 sec | 65% |

## Type Palette #3
Regular, Semibold, Bold, Condensed Bold
(4 variants on 2 axes, made from 3 sources)

|  | w/ static fonts | w/ variable fonts | total savings | % savings |
|:--|:--|:--|:--|:--|
| # of font files | 4 | 1 | 3 | 75% |
| Total file size | 55 kB | 17 kB | 38 kB | 69% |
| Transfer time | 0.11 sec | 0.03 sec | 0.08 sec | 69% |
| Additional latency | 0.4 sec | 0.1 sec | 0.3 sec | 75% |
| Total load time | 0.51 sec | 0.13 sec | 0.38 sec | 74% |

## Type Palette #4
Regular, Semibold, Bold, Narrow, Condensed Bold
(5 variants on 2 axes, made from 4 sources)

|  | w/ static fonts | w/ variable fonts | total savings | % savings |
|:--|:--|:--|:--|:--|
| # of font files | 5 | 1 | 4 | 80% |
| Total file size | 71 kB | 32 kB | 39 kB | 55% |
| Transfer time | 0.14 sec | 0.06 sec | 0.08 sec | 55% |
| Additional latency | 0.5 sec | 0.1 sec | 0.4 sec | 80% |
| Total load time | 0.64 sec | 0.16 sec | 0.48 sec | 74% |

## Type Palette #5
Regular, Semibold, Bold, Narrow, Narrow Semibold, Narrow Bold, Condensed Bold
(7 variants on 2 axes, made from 4 sources)

|  | w/ static fonts | w/ variable fonts | total savings | % savings |
|:--|:--|:--|:--|:--|
| # of font files | 7 | 1 | 6 | 86% |
| Total file size | 102 kB | 32 kB | 70 kB | 69% |
| Transfer time | 0.2 sec | 0.06 sec | 0.14 sec | 69% |
| Additional latency | 0.7 sec | 0.1 sec | 0.6 sec | 86% |
| Total load time | 0.9 sec | 0.16 sec | 0.74 sec | 82% |


As you can tell from the numbers above, variable fonts can offer significant improvements in performance compared to using multiple static fonts. So even if a set of static fonts allows you the design flexibility you need, your website can still benefit from delivering the equivalent variants with variable fonts.
