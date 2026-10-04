/**
 * Bundled by jsDelivr using Rollup v4.62.2 and esbuild v0.28.1.
 * Original file: /npm/isoformat@0.2.1/src/index.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
function i(n,t){if(n instanceof Date||(n=new Date(+n)),isNaN(n))return typeof t=="function"?t(n):t;const u=n.getUTCHours(),r=n.getUTCMinutes(),s=n.getUTCSeconds(),e=n.getUTCMilliseconds();return`${$(n.getUTCFullYear())}-${o(n.getUTCMonth()+1,2)}-${o(n.getUTCDate(),2)}${u||r||s||e?`T${o(u,2)}:${o(r,2)}${s||e?`:${o(s,2)}${e?`.${o(e,3)}`:""}`:""}Z`:""}`}function $(n){return n<0?`-${o(-n,6)}`:n>9999?`+${o(n,6)}`:o(n,4)}function o(n,t){return`${n}`.padStart(t,"0")}const c=/^(?:[-+]\d{2})?\d{4}(?:-\d{2}(?:-\d{2})?)?(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d{3})?)?(?:Z|[-+]\d{2}:?\d{2})?)?$/;function f(n,t){return c.test(n+="")?new Date(n):typeof t=="function"?t(n):t}export{i as format,f as parse};
