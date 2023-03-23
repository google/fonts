# Google Fonts Axis Registry

This repository is the official **upstream** Google Fonts **Axis Registry.**

This data-set is synced into the central [github.com/google/fonts](https://github.com/google/fonts) git repo, through which all Google Fonts assets are onboarded.

The **actual** Axis Registry lives within the actual live Google Fonts product, surfaced at [fonts.google.com/variablefonts#axis-definitions](https://fonts.google.com/variablefonts#axis-definitions) – so axis definitions are only final when they appear on that page, and this repository will from time to time contain fresh data not in the live system, and subject to change. 

## The AxisRegistry Python Module

This repo is structured as a Python package/module, providing easy access to the registry data-set from Python programs.

The Python package contains a collection of metadata source files that collectively form the Google Fonts Axis Registry.

This module is the central place for dataset updates.
After updates are made here on the `main` branch, the maintainers of the central repo will update subtree located at `google/fonts/axisregistry` and then work to push those changes through to the live Google Fonts API via sandbox servers, according to the typical push process.
For more detailed information, please see the [Axis Registry](https://googlefonts.github.io/gf-guide/googlefonts.html#axis-registry) section of the _`google/fonts` repository explained_ article in the GF Guide.

<!--
## Registering New Axes

Font projects that need to introduce a new axis to Google Fonts must follow the [Axis Registry Protocol](https://googlefonts.github.io/gf-guide/axis-registry.html) article in the GF Guide.
-->

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
*   `fallback`
    *   Instance positions along the axis, such as wght 100,200,300,400,500,600,700,800,900.
    *   A cross-product of fallback positions along all supported axes is created to support legacy browsers that lack variable font support.
        For axes with CSS3 properties (such as [font-weight](https://drafts.csswg.org/css-fonts-3/#font-weight-prop)), the positions accessible
        to CSS3 should be specified. For axes lacking CSS3 properties a legacy browser is limited to a single position and that position must
        be at a fallback.
        <br>In case an axis doesn't include predefined positions, it is mandatory to define at least one fallback position. It should be called `Default` and its value should correspond to the `default_value` position of the axis.
*   `fallback_only`
    *   Describes whether to only use fallback values when presenting to users in the UI. Currently, default to `true`, for continuous range axes should be set to `false.`
*   `description`
    *   A description of the axis.

## Why does Google Fonts have its own Axis Registry?

We support a superset of the [OpenType axis registry](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg) axis set, and use additional metadata for each axis.
Axes present in a font file but not in this registry will not function via our API.
No variable font is expected to support all of the axes here.

Any font foundry or distributor library that offers variable fonts has a implicit, latent, de-facto axis registry, which can be extracted by scanning the library for axes' tags, labels, and min/def/max values.
While in 2016 Microsoft originally offered to include more axes in the OpenType 1.8 specification ([github.com/microsoft/OpenTypeDesignVariationAxisTags](https://github.com/microsoft/OpenTypeDesignVariationAxisTags)), by August 2020 this effort had stalled.
We hope more foundries and distributors will publish documents like this that make their axes explicit, to encourage of adoption of variable fonts throughout the industry, and provide source material for a future update to the OpenType specification's axis registry.
