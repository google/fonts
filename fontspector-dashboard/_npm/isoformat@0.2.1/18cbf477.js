/**
 * Bundled by jsDelivr using Rollup v2.79.2 and Terser v5.39.0.
 * Original file: /npm/isoformat@0.2.1/src/index.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
function t(t,n){if(t instanceof Date||(t=new Date(+t)),isNaN(t))return"function"==typeof n?n(t):n;const o=t.getUTCHours(),d=t.getUTCMinutes(),r=t.getUTCSeconds(),u=t.getUTCMilliseconds();return`${$=t.getUTCFullYear(),$<0?`-${e(-$,6)}`:$>9999?`+${e($,6)}`:e($,4)}-${e(t.getUTCMonth()+1,2)}-${e(t.getUTCDate(),2)}${o||d||r||u?`T${e(o,2)}:${e(d,2)}${r||u?`:${e(r,2)}${u?`.${e(u,3)}`:""}`:""}Z`:""}`;var $}function e(t,e){return`${t}`.padStart(e,"0")}const n=/^(?:[-+]\d{2})?\d{4}(?:-\d{2}(?:-\d{2})?)?(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d{3})?)?(?:Z|[-+]\d{2}:?\d{2})?)?$/;function o(t,e){return n.test(t+="")?new Date(t):"function"==typeof e?e(t):e}export{t as format,o as parse};export default null;
