
A “flash of invisible text” (FOIT) is the phenomenon in which a web page loads without the [type](/glossary/type) appearing at all, before rendering to the intended [typeface(s)](/glossary/typeface). This delay is caused by the [web fonts](/glossary/web_font) being downloaded to the user’s device. See also: [FOUT](/glossary/fout).

<figure>

![Two abstract representations of a website being viewed on a mobile phone: on the left phone, no content is visible at all; on the right, the content is visible—intended to represent what happens after a delay in loading the fonts.](images/thumbnail.svg)

</figure>

In almost all scenarios, a FOIT is not a great user experience for the end user, since all written content is effectively blocked during the time it takes the fonts to load.

The effect can be prevented using the CSS `font-display` property, which will first render the content using system fonts before swapping to the desired typefaces once the web fonts have downloaded. For more information, please see our article [“Using web fonts.”](/lesson/using_web_fonts)
