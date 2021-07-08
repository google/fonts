# Contribute to Google Fonts

## Feedback

If you have any feedback on Google Fonts API, directory, or the fonts themselves, please create an issue at [github.com/google/fonts/issues](http://github.com/google/fonts/issues)

## New Families

If you would like to include a new font family in the Google Fonts collection, we'll be happy to include it if it meets the following criteria:

* The typeface design must be original, or a legitimate revival of a design in the public domain, and of good quality. The Google Design team curates the overall Google Fonts collection and decides if fonts are of good quality. We may reject families if they fail to meet our criteria. You can get general reviews of your project from the wider international type community during development by posting review requests in the [googlefonts-discuss](https://groups.google.com/forum/#!forum/googlefonts-discuss) group, and the [typedrawers](http://typedrawers.com/categories/critiques%E2%80%94type-design) review forum.
* The project must be **wholly** licensed under the [SIL Open Font License v1.1](http://scripts.sil.org/OFL), and there are no proprietary/restricted-license versions of the project available elsewhere (such as additional weights/styles.)
* The Open Font License should not have any Reserved Font Names ([why](https://github.com/simoncozens/silson/issues/1))
* The copyright holders must all have signed the [Google Contributor's License Agreement](https://cla.developers.google.com)
* The font family name should not include any copyright holder full names (but first names are OK), no registered trademarks, and no initials or abbreviations, and no references to languages or writing systems; it should be a simple and unique name. A limited but easy way to test for uniqueness is [namecheck.fontdata.com](https://namecheck.fontdata.com)  
* The project must be developed on Github or similar, with complete corresponding sources, [open to public participation](http://producingoss.com), and actively maintained. Complete corresponding sources means that the fonts are available in your preferred form of modification, the files you actually use to develop the project, along with all the build instructions or scripts needed to  reproduce the process of turning those source files into your released font binaries.  
* All binary font files must be available in TTF format, and should have hinting (such as with [ttfautohint](http://www.freetype.org/ttfautohint/)).
* All font files must be built with a scripted build process, and should use [fontmake](https://github.com/googlefonts/fontmake)
* All font files should support the "Google Fonts 2016 Plus" glyph set. (Learn more about the Google Fonts 2016 glyph sets in the [gftools](https://github.com/googlefonts/gftools/blob/master/Lib/gftools/encodings/GF%20Glyph%20Sets/README.md) project.)
* All font files within the family must have the same Unicode character set (unencoded glyphs can differ) and corresponding upper/lower case pairs  
* All font files should pass the [Font Bakery](https://github.com/googlefonts/fontbakery) checks for the [`googlefonts` profile](https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html).
* A `README.md` file must be included in the root of the source repository, and inside of that file we can read about the project with the kind of information suggested by SIL in their [FONTLOG](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ofl-faq_web#43cecb44) recommendation (but no FONTLOG file itself is needed.)
* A direct `DESCRIPTION.en_us.html` file, a `profile.txt` and a `your-name.jpg` avatar image, should be available to be copied into this repo ([example](https://github.com/google/fonts/blob/master/ofl/poppins/DESCRIPTION.en_us.html)) so that the fonts.google.com catalog can credit your project.  

**More detailed design and production details are listed in our [Project Specification](https://github.com/googlefonts/gf-docs/tree/master/Spec)**

When you are ready to meet these requirements, please [create a new issue](https://github.com/google/fonts/issues) with a link to the project's source repository.
In special circumstances, you can request an exception to these requirements on your issue.

From time to time, Google Fonts provides financial and design assistance for projects. 
If you would like to discuss this, please mention that you would like someone to contact you privately when filing an issue (and have contact details on your Github profile page.)

### Updates

If your font is already on-boarded and you'd like us to update our copy, please file an issue (instead of making a pull request directly.)

We carefully check the technical aspects of updated fonts to prevent unintended changes, so we prefer to collaborate with you on your upstream project to make a release which we update from. 

## Contributor License Agreement

We love to accept all good patches and contributions to this project. 
There is just one thing contributors need to do first...

Contributions to Google projects must be accompanied by a Contributor License Agreement. 
This is not a copyright assignment, it simply gives Google permission to use and redistribute your contributions as part of the project.

<https://cla.developers.google.com>

You generally only need to submit the Google CLA once, so if you've already submitted one for a different project, you probably don't need to do it again.

After your contribution is included, you will be listed in [CONTRIBUTORS](CONTRIBUTORS) and/or [AUTHORS](AUTHORS) files; 
CONTRIBUTORS is the official list of people who can contribute (and typically have contributed) code to this repository, while the AUTHORS file lists the copyright holders.
