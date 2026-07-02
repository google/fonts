/**
 * Bundled by jsDelivr using Rollup v4.62.2 and esbuild v0.28.1.
 * Original file: /npm/internmap@2.0.3/src/index.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
class h extends Map{constructor(e,r=i){if(super(),Object.defineProperties(this,{_intern:{value:new Map},_key:{value:r}}),e!=null)for(const[s,c]of e)this.set(s,c)}get(e){return super.get(n(this,e))}has(e){return super.has(n(this,e))}set(e,r){return super.set(u(this,e),r)}delete(e){return super.delete(o(this,e))}}class f extends Set{constructor(e,r=i){if(super(),Object.defineProperties(this,{_intern:{value:new Map},_key:{value:r}}),e!=null)for(const s of e)this.add(s)}has(e){return super.has(n(this,e))}add(e){return super.add(u(this,e))}delete(e){return super.delete(o(this,e))}}function n({_intern:t,_key:e},r){const s=e(r);return t.has(s)?t.get(s):r}function u({_intern:t,_key:e},r){const s=e(r);return t.has(s)?t.get(s):(t.set(s,r),r)}function o({_intern:t,_key:e},r){const s=e(r);return t.has(s)&&(r=t.get(s),t.delete(s)),r}function i(t){return t!==null&&typeof t=="object"?t.valueOf():t}export{h as InternMap,f as InternSet};
