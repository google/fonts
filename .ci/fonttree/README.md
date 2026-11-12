# Font Tree

Drop a font on `index.html` and browse every table as a tree, in the style of a
diffenator2 report. The decompiler is [fontations](https://github.com/googlefonts/fontations)
(read-fonts, skrifa) plus the `ttj` crate from diffenator3, compiled to WebAssembly.
Nothing leaves the browser.

The daily report workflow (`.github/workflows/report.yaml`) builds it and serves
it at <https://google.github.io/fonts/fonttree.html>.

## Build

    ./build.sh

Needs a Rust toolchain with the `wasm32-unknown-unknown` target and `wasm-pack`.
The script compiles `src/lib.rs`, then inlines the wasm into `www/index.html` to
produce a single self-contained `index.html` that works from `file://`.

## Layout

- `src/lib.rs`   the engine: container decoding (WOFF/WOFF2 via wuff), summaries, table serialisers
- `www/index.html`  the page template; `build.sh` fills in the wasm
- `index.html`   the built page (about 1.3 MB)
