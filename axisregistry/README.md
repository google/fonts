# GF Axis Registry

This package contains a collection of metadata files that collectivefly form the
GF Axis Registry.

## Why does Fonts have its own Axis Registry?

We plan to support a superset of the OpenType axis registry and additional
metadata. Individual variable fonts support a subset of our axis registry. Axes
not in our registry will not function via our API.

## Axis Metadata Fields

*   `tag`
    *   Tag for the axis used to specify an axis in `font-variation-settings`
        and CSS API requests.
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
        For example, `0` means values must be specified as whole numbers while
        `-1` means values can be as precise as one decimal place.
*   `fallback` (repeated)
    *   Important positions along the axis. For weight, these are positions like
        Regular, Medium, and Bold.
*   `description`   
    *   A description of the axis.
