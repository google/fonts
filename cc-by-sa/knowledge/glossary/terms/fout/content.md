
A “flash of unstyled text” is the phenomenon in which a web page loads with the [type](/glossary/type) set using [system fonts](/glossary/system_font_web_safe_font) before switching to the intended [typeface(s)](/glossary/typeface). This delay is caused by the [web fonts](/glossary/web_font) being downloaded to the user’s device.

<figure>

![Two abstract representations of FOUT on a mobile phone: On the left, the content is rendered in system fonts. On the right, the content is rendered in web fonts.](images/thumbnail.svg)

</figure>

The effect can be prevented using the CSS `font-display` property but is not recommended because it hides the content, resulting in [FOIT](/glossary/foit).
