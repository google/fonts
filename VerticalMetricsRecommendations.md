# Vertical metrics recommendations

**Please see [this googlefonts-discuss thread](https://groups.google.com/forum/#!topic/googlefonts-discuss/W4PHxnLk3JY) for the 2016 vertical metrics recommendations from Khaled and Kalapi**

_Recommendations for setting vertical metrics for consistent layout and avoiding clipping._

Last Updated Jan 21, 2011 by @raphlinus

## Goals

It’s important to be clear on the goals. Web font usage is a little different than the traditional print usage, although having the fonts still be suitable for print is also a reasonable goal. Scope is also important. It’s much easier to produce decent vertical metrics for a font which will be Latin-1 only, and harder when it’s important to accommodate Vietnamese (stacked accents) or other scripts with difficult vertical metrics needs. Also, fonts with very long extenders (such as Zapfino) are a bit more challenging.

Some of the goals conflict. It is not possible to create a font with plenty of room for Vietnamese, which doesn’t clip on Windows, is consistent across all platforms, and which provides a reasonable default for “line-height: normal”. So, we have to pick and choose what we can get.

### Important goals

Incorrectly set vertical metrics can cause many different problems. The worst are clipping (primarily on Windows) and inconsistency from browser to browser. These should be avoided. Further, if Vietnamese glyphs (which have stacked accents) are ever to be added to a font, it should be reasonably easy to accommodate those without changing existing pages.

### Less important goals

One of the recommendations below for using web fonts is to always set a line-height numeric CSS property. Some people, of course, will use web fonts without doing that. For these users, we want to provide a reasonable default line spacing. We also want to make sure that there isn’t too much reformatting of the page when the web font replaces the default font underneath (the so-called “flash of unstyled text.”)

### Tentative recommendations

For using fonts: **always** specify an explicit line-height CSS property (for example, 1.2), rather than relying on “line-height: normal”. The latter cannot be made to be completely consistent across all browsers, and is also likely to change as the vertical space budget is increased to extend fonts into more international scripts. (more tentative:) specify ClearType collection font (eg Calibri, Cambria) as the next fallback in the CSS stack.

For creating fonts: **definitely** make sure usWinAscent and usWinDescent values include the bounding box of all glyphs in the font, as anything falling outside will be clipped. **Do** make sure that usWinAscent values matches hhea Ascender and sTypoAscender (same for Descent). **Do** use zero values for hhea LineGap and sTypoLineGap (in general, we’ll want any excess budget to be reserved for additional accents, and also it’s quite difficult to make line gaps consistent).

#### Expanding character set coverage (for example, for Vietnamese)

Vietnamese (and a few other extended-Latin languages) require doubly stacked glyphs. The font designer has three choices, all of which are valid. The best one depends on context and judgment:

  * Add to the vertical space budget. Note that the ascent and descent values will almost always need to increase, otherwise there will be clipping. In this case, do add equally to ascent and descent. This way, baseline positioning won’t be affected in the case that line-height is set.
  * Squish the accent marks to fit in the existing space budget. This is what is done in Courier Bold shipping with Windows fonts. (see [typophile thread](http://www.typophile.com/node/72954) on vietnamese accents)
  * Squish the entire glyph, decreasing the cap-height to make more room for the accents. This is how Jos Buivenga handled “Vietnamese for Dell”.


### Browser tests

The Google Font team tested a number of browsers on a test case comprising a base font plus various modifications.

The test case, along with a collection of screenshots, is posted at http://levien.com/webfonts/vmtx/ . The main test case is test.html. Additional test cases (covering behaviour of system fonts with large bounding boxes) are in test2.html. The screenshots are at screenshots.html. I welcome more screenshots or observations that shed more light on the actual behavior of browsers.

#### Detailed analysis of browser testing

What follows is our best attempt of determining how browsers interpret vertical metrics. The formulas account for the tests, but may not be precise in all cases - so any more insight is definitely appreciated.

For determination of line height (ie when line-height: normal is set):

Chrome/Linux, Chrome/Mac, Safari/Mac, and Firefox/Mac tend to use the HHEA metrics.

Firefox/Linux appears to use the maximum of typo and HHEA metrics.

IE6 uses the usWin metrics. IE7 and IE8 use usWin metrics unless "really use typo" metrics bit is set, in which case they use typo metrics. IE9 uses max of usWin and HHEA metrics, except that "really use typo" metrics overrides those.

Firefox/Windows uses max of usWin and HHEA metrics, but adds a line gap when spacing would otherwise be very tight (don't have exact formula for this).

Chrome/Windows uses max of usWin and HHEA metrics.

When line-height is set explicitly, the main remaining significant parameter is distance from the top of the text box to the baseline.

Firefox/Mac and Chrome mac use HHEA ascent + 1/2 (line-height - (HHEA ascent + HHEA descent)).

Firefox/Windows and Chrome/Windows use usAscent + 1/2 (line-height - (HHEA ascent + HHEA descent)).

IE8 is the same as Firefox/Windows unless the "really use typo" bit is set. In that case, it is typo ascent + 1/2 (line-height - (typo ascent + typo descent)).

Firefox/Linux uses max(usAscent, typoAscent) + 1/2 (line-height - (max(usAscent, typoAscent) + max(usDescent, typoDescent))).

So, as can be seen, even with line-height set explicitly, any discrepancies between the three sets of vertical metrics can cause irregularities in baseline positioning.

All tested Windows browsers (except for IE9) clip to usWin. In particular, default rendering of Arial on Windows does clip very tall glyphs such as u+01fa (Aringacute). IE9, even in compatibility modes, does _not_ clip, even though in all other respects matches the vertical metrics handling of the browser it's set to emulate.

#### Testing of font matching Arial metrics


I created version of Inconsolata with Aringacute added and matching all of Arial’s metrics for testing. Strangely, this font does _not_ especially well match Arial. In particular, Safari and Chrome/Mac add to the line-height (normal) of Arial when tall characters are used, but not to the web font. Note also that Chrome clips the Aringacute intermittently (it’s probably using hhea, but this isn’t 100% confirmed).

### FontForge issues


Rules for setting “Ascent” and “Descent” in font info are very quirky. Apparently, default is .8 **em, but if typo ascent and typo descent sum to em, value is taken from them.**

“Really use Typo Metrics” doesn’t seem to actually save to ttf file. This seems to be an outright bug. The reason why is quite opaque to me just from reading the code, and probably requires deep debugging.

Opening a file, editing (for example, by deleting characters), and saving is likely to change the vertical metrics. See this thread for more discussion. The subset.py script goes to somewhat heroic lengths to work around this.

## References

  * http://meyerweb.com/eric/thoughts/2008/05/06/line-height-abnormal/
  * [Vertical Metrics How-To](http://typophile.com/node/13081) by John Hudson
  * [Vietnamese accents: beyond the Bbox.](http://www.typophile.com/node/72954) (typophile)
  * http://www.fontqa.com/documentation/reference/fontQA_Vmetric.html
  * http://www.kltf.de/downloads/FontMetrics-kltf.pdf
  * http://www.kutlux.co.uk/images/type_discrepency/html-inDesign_discrepency_v2.pdf
  * http://lists.w3.org/Archives/Public/www-style/2010Aug/0053.html - John Hudson on fsSelection bit 7

http://blog.typekit.com/2010/09/13/updating-vertical-metrics-for-cross-platform-consistency/

Tim Brown comments:
Happy to share this info, although it’s not super interesting for most people. We’re constantly learning, but here’s what we know right now: Windows browsers use Win metrics, Mac browsers use hhea metrics, and Firefox on Linux uses Typo metrics unless the hhea values are greater. Win and hhea metrics must match, including an hhea linegap of zero. Typo linegap has to be zero too, or lines of text are spaced unpredictably across browsers.
The specific values to which metrics should be changed are unique to each font file. Our internal tools for foundry partners make recommendations based on the conditions I just mentioned, and also based on the maximum ascent/descent of glyphs in the font file.

http://meyerweb.com/eric/thoughts/2006/02/08/unitless-line-heights/ A recommendation to specify line-height as a unitless number, rather than, for example, “1.2em”. tl;dr: if styles with different font size inherit the unitless setting, it’s multiplied by the actual font size of that line. By contrast, values in em units are always fixed in the parent.

* * * 

### Comment by thomas.phinney, Jan 21, 2011

I assert that the Firefox Linux behavior is a bug, and that font developers should not force the Typo metrics to be compatible with the Windows and Mac metrics. The entire reason the Typo metrics were created was to have a set of "typographically correct" metrics that could differ from the Win/Mac metrics, which have to take into account things like clipping and the bounding box of the glyphs.

### Comment by readablerichard, Jan 23, 2011

Raph - in the interest of explaining this problem to the larger community of web authors - some questions:

Firstly: Are these variations between browsers and platforms unique to @font-face web fonts or is it also an issue with the installed 'web safe' system fonts? Are there the same variations using, say, Verdana or Arial? In other words, is this actually a new problem or just one that went unnoticed until fonts were in the spotlight because of @font-face?

Secondly: Do I understand correctly, from reading the "Details Of Browser Testing" section, that, given the same exact font, getting the same to-the-pixel line-height is impossible given the current crop of user agents? Even if the author specifies line-height in pixels?

(Any feedback at all on these questions, greatly appreciated.)

Richard Fink http://readableweb.com

### Comment by dr.khaled.hosny, Jan 24, 2011

About FF, what version are you testing? Here when I open the generated font in FF I see the "Really use Typo metrics" selected, so I assumed if it reads it it must be set. Decompiling OS/2 table with TTX I see `<fsSelection value="00000000 11000000"/>` but I've no idea which of those is the 7th bit.
