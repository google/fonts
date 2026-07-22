import { jsx, jsxs } from "../../_npm/react@19.2.8/jsx-runtime.f9a472e9.js";
function RenderFamily(family) {
  let match = family.match(/^([^\/]+)\/([^\/]+)\/(\S+)\?([a-f0-9]+) \((\S+)\) (\S+)/);
  if (!match) {
    return /* @__PURE__ */ jsx("span", { children: family });
  }
  let [_, owner, repo, path, sha, config, mode] = match;
  return /* @__PURE__ */ jsxs("span", { children: [
    /* @__PURE__ */ jsxs("a", { href: `https://github.com/${owner}/${repo}`, children: [
      owner,
      "/",
      repo
    ] }),
    " / ",
    /* @__PURE__ */ jsx("a", { href: `https://github.com/${owner}/${repo}/blob/${sha}/${path}`, children: path }),
    " @ ",
    /* @__PURE__ */ jsx("a", { href: `https://github.com/${owner}/${repo}/commit/${sha}`, children: sha.substring(0, 7) }),
    " (",
    /* @__PURE__ */ jsx("a", { href: `https://github.com/${owner}/${repo}/blob/${sha}/sources/${config}`, children: config }),
    ") ",
    mode
  ] });
}
function RenderCompileFailed(failure) {
  return ["fontmake", "fontc"].map((compiler) => {
    if (failure[compiler]) {
      return /* @__PURE__ */ jsxs("div", { children: [
        /* @__PURE__ */ jsxs("h3", { children: [
          compiler,
          " failed"
        ] }),
        /* @__PURE__ */ jsxs("pre", { children: [
          "% ",
          failure[compiler].command
        ] }),
        /* @__PURE__ */ jsx("pre", { class: "pre-wrap", children: failure[compiler].stderr })
      ] }, compiler);
    }
    return /* @__PURE__ */ jsx("div", {});
  });
}
export function RenderFailures({ failures } = {}) {
  return /* @__PURE__ */ jsx("div", { children: Object.entries(failures).map(([family, problems]) => /* @__PURE__ */ jsxs("details", { children: [
    /* @__PURE__ */ jsx("summary", { children: RenderFamily(family) }),
    problems.compile_failed && RenderCompileFailed(problems.compile_failed)
  ] }, family)) });
}
function RenderDiffs(diffs) {
  return /* @__PURE__ */ jsxs("div", { children: [
    /* @__PURE__ */ jsx("h3", { children: "Diffs" }),
    /* @__PURE__ */ jsx("ul", { children: Object.entries(diffs).map(([area, diff]) => /* @__PURE__ */ jsxs("li", { children: [
      area,
      " : ",
      diff
    ] }, area)) })
  ] });
}
let pct = (problems) => problems.diffs ? problems.diffs.total * 100 : 100;
export function RenderSuccesses({ successes } = {}) {
  return /* @__PURE__ */ jsx("div", { children: Object.entries(successes).filter(([family, problems]) => {
    return problems.diffs && problems.diffs.total > 0;
  }).sort(([familyA, problemsA], [familyB, problemsB]) => {
    return pct(problemsB) - pct(problemsA);
  }).map(([family, problems]) => /* @__PURE__ */ jsxs("details", { children: [
    /* @__PURE__ */ jsxs("summary", { children: [
      RenderFamily(family),
      " (",
      pct(problems).toFixed(2),
      "%)"
    ] }),
    problems.diffs && RenderDiffs(problems.diffs)
  ] }, family)) });
}
