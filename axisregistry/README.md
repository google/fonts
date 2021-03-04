# GF Axis Registry

This package contains a collection of metadata source files that collectively form the Google Fonts Axis Registry.

The live Axis Registry is at [fonts.google.com/variablefonts](https://fonts.google.com/variablefonts), and axis definitions are only final when they appear on that page.

When the registry is updated here, a line like `axisregistry/axis_name.textproto` should be added to the `to_sandbox.txt` file.

## Axis Metadata Fields

*   `tag`
    *   Tag for the axis used to specify an axis in `font-variation-settings` and CSS API requests.
*   `display_name`
    *   Readable name for the axis, generally the expanded form of `tag`.
*   `min_value`
    *   Lower bound of the axis. Inclusive.
*   `max_value`
    *   Upper bound of the axis. Inclusive.
*   `default_value`
    *   Default position of the aixs.
*   `precision`
    *   Describes the specificity at which an axis position can be specified.
        For example, `0` means values must be specified as whole numbers while `-1` means values can be as precise as one decimal place.
*   `fallback` (repeated)
    *   Instance positions along the axis, such as wght 100,200,300,400,500,600,700,800,900.
    *   A cross-product of fallback positions along all supported axes is created to support legacy browsers that lack variable font support.
        For axes with CSS3 properties (such as [font-weight](https://drafts.csswg.org/css-fonts-3/#font-weight-prop)), the positions accessible
        to CSS3 should be specified. For axes lacking CSS3 properties a legacy browser is limited to a single position and that position must
        be at a fallback.
*   `description`   
    *   A description of the axis.

## Why does Google Fonts have its own Axis Registry?

We support a superset of the [OpenType axis registry](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg) axis set, and use additional metadata for each axis.
Axes present in a font file but not in this registry will not function via our API.
No variable font is expected to support all of the axes here.

Any font foundry or distributor library that offers variable fonts has a implicit, latent, de-facto axis registry, which can be extracted by scanning the library for axes' tags, labels, and min/def/max values.
While in 2016 Microsoft originally offered to include more axes in the OpenType 1.8 specification ([github.com/microsoft/OpenTypeDesignVariationAxisTags](https://github.com/microsoft/OpenTypeDesignVariationAxisTags)), as of August 2020, this effort has stalled.
We hope more foundries and distributors will publish documents like this that make their axes explicit, to encourage of adoption of variable fonts throughout the industry, and provide source material for a future update to the OpenType specification's axis registry.
