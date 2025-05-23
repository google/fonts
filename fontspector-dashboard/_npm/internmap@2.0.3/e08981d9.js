/**
 * Bundled by jsDelivr using Rollup v2.79.2 and Terser v5.39.0.
 * Original file: /npm/internmap@2.0.3/src/index.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
class e extends Map{constructor(e,t=u){if(super(),Object.defineProperties(this,{_intern:{value:new Map},_key:{value:t}}),null!=e)for(const[t,r]of e)this.set(t,r)}get(e){return super.get(r(this,e))}has(e){return super.has(r(this,e))}set(e,t){return super.set(n(this,e),t)}delete(e){return super.delete(s(this,e))}}class t extends Set{constructor(e,t=u){if(super(),Object.defineProperties(this,{_intern:{value:new Map},_key:{value:t}}),null!=e)for(const t of e)this.add(t)}has(e){return super.has(r(this,e))}add(e){return super.add(n(this,e))}delete(e){return super.delete(s(this,e))}}function r({_intern:e,_key:t},r){const n=t(r);return e.has(n)?e.get(n):r}function n({_intern:e,_key:t},r){const n=t(r);return e.has(n)?e.get(n):(e.set(n,r),r)}function s({_intern:e,_key:t},r){const n=t(r);return e.has(n)&&(r=e.get(n),e.delete(n)),r}function u(e){return null!==e&&"object"==typeof e?e.valueOf():e}export{e as InternMap,t as InternSet};export default null;
