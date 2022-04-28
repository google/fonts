
“Parametric Descender Depth” (`YTDE` in CSS) is a [parametric axis](/glossary/TERM), found in some [variable fonts](/glossary/TERM), for specifying and varying the depth of [lowercase](/glossary/TERM) [descenders](/glossary/TERM), scaled as negative height.

The [Google Fonts CSS v2 API ](https://developers.google.com/fonts/docs/css2) defines the axis as:

| Default: | Min: | Max: | Step: |
| --- | --- | --- | --- |
| -250 | -1000 | 0 | 0 |

<figure>

![INSERT_ALT_TEXT](images/thumbnail.svg)

</figure>

Its four-letter abbreviation, YTDE, is a reference to its logical name, “Y-Transparency for Descenders.” It may be used in conjunction with other axes controlling Y-yransparencies (vertical alignment zones), especially the [Parametric Ascender Height axis (YTAS)](/glossary/TERM).

In line with the current CSS spec, the four-character code for this axis should be referenced in UPPERCASE (only the five axes registered in the OpenType format specification should appear in lowercase). Also, when using the Google Fonts API, the uppercase axes have to appear first in the URL.
