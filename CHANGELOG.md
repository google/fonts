Below are the most important changes from each release.

## 0.1.0 (2022-Mar-04)
### Release notes
  - Initial release of the `axisregistry` python module.
  - Most of the code & data was migrated from the [`fontbakery`](https://github.com/googlefonts/fontbakery/) and [`google/fonts`](https://github.com/google/fonts/) git repositories so that the GF Axis Registry data can be easily available to all our tools. The most immediate user of this module is `Font Bakery` itself, as well as `GFTools`.
  - Axis Registry definitions are still being gradualy updated on the `google/fonts` repo, on its **axisregistry/** directory (https://github.com/google/fonts/tree/main/axisregistry) and this `axisregistry` python module will try to be kept in sync.
  - There's an ongoing plan to make this module the main place to update these definitions, avoiding data duplication and guaranteeing uniformity across tools.
