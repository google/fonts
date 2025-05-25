/**
 * Bundled by jsDelivr using Rollup v2.79.2 and Terser v5.39.0.
 * Original file: /npm/binary-search-bounds@2.0.5/search-bounds.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
function r(r,n,t,o,e){for(var u=e+1;o<=e;){var i=o+e>>>1,f=r[i];(void 0!==t?t(f,n):f-n)>=0?(u=i,e=i-1):o=i+1}return u}function n(r,n,t,o,e){for(var u=e+1;o<=e;){var i=o+e>>>1,f=r[i];(void 0!==t?t(f,n):f-n)>0?(u=i,e=i-1):o=i+1}return u}function t(r,n,t,o,e){for(var u=o-1;o<=e;){var i=o+e>>>1,f=r[i];(void 0!==t?t(f,n):f-n)<0?(u=i,o=i+1):e=i-1}return u}function o(r,n,t,o,e){for(var u=o-1;o<=e;){var i=o+e>>>1,f=r[i];(void 0!==t?t(f,n):f-n)<=0?(u=i,o=i+1):e=i-1}return u}function e(r,n,t,o,e){for(;o<=e;){var u=o+e>>>1,i=r[u],f=void 0!==t?t(i,n):i-n;if(0===f)return u;f<=0?o=u+1:e=u-1}return-1}function u(r,n,t,o,e,u){return"function"==typeof t?u(r,n,t,void 0===o?0:0|o,void 0===e?r.length-1:0|e):u(r,n,void 0,void 0===t?0:0|t,void 0===o?r.length-1:0|o)}var i={ge:function(n,t,o,e,i){return u(n,t,o,e,i,r)},gt:function(r,t,o,e,i){return u(r,t,o,e,i,n)},lt:function(r,n,o,e,i){return u(r,n,o,e,i,t)},le:function(r,n,t,e,i){return u(r,n,t,e,i,o)},eq:function(r,n,t,o,i){return u(r,n,t,o,i,e)}},f=i.eq,v=i.ge,a=i.gt,c=i.le,d=i.lt;export{i as default,f as eq,v as ge,a as gt,c as le,d as lt};
