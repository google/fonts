#!/usr/bin/env bash
# Build the fontations engine to wasm and inline it into a single index.html.
set -euo pipefail
cd "$(dirname "$0")"
wasm-pack build --target no-modules --release --no-typescript
python3 -I - <<'PY'
import base64, pathlib
tpl = pathlib.Path('www/index.html').read_text()
js = pathlib.Path('pkg/fonttree.js').read_text()
b64 = base64.b64encode(pathlib.Path('pkg/fonttree_bg.wasm').read_bytes()).decode()
assert '/*__WASM_JS__*/' in tpl and '__WASM_B64__' in tpl
out = tpl.replace('/*__WASM_JS__*/', js).replace('__WASM_B64__', b64)
pathlib.Path('index.html').write_text(out)
print(f'index.html written: {len(out)/1e6:.1f} MB (wasm {len(b64)*3//4/1e6:.2f} MB)')
PY
