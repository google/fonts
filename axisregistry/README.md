# GF Axis Registry

This package contains a collection of metadata files that collectivefly form
the GF Axis Registry.

## Why does Fonts have its own Axis Registry?

Any font foundry or distributor library that offers variable fonts has a
latent/de-facto axis registry, which can be extracted by scanning the library
for axes' tags, labels, and min/def/max values and publishing a document that
makes this info explicit. We are doing the same in order to help our users adopt
variable fonts.

While in 2016 Microsoft originally offered to include more axes in the OpenType
1.8 specification (https://github.com/microsoft/OpenTypeDesignVariationAxisTags)
as of 2020-05 they have abandoned that effort. We hope that in publishing
explicit "Google Fonts Axis Registry" docs, we will reinvigorate Microsoft's
effort to update the OpenType specification's axis registry.
