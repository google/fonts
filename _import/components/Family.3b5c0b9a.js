import { jsx, jsxs } from "../../_npm/react@19.2.7/jsx-runtime.c6c547ca.js";
export function RenderFamily({ family, directory, allResults, metadata, servers, updates, pullRequests } = {}) {
  let result = allResults.latestResult[directory];
  let fbStuff = /* @__PURE__ */ jsx("div", {});
  let history = [];
  let pullsForThisDirectory = pullRequests?.filter((pr) => pr.directories.includes(directory)) || [];
  if (updates[family]) {
    for (let [server, moves] of Object.entries(updates[family])) {
      for (let { version, date } of moves) {
        if (date != "1970-01-01T00:00:00") {
          history.push({ server, version, date });
        }
      }
    }
  }
  history = history.sort((a, b) => new Date(b.date) - new Date(a.date));
  if (result) {
    for (let section of Object.keys(result)) {
      let checks = result[section];
      if (checks.filter((check) => check.status === "WARN" || check.status === "FAIL").length == 0) {
        delete result[section];
      }
    }
    fbStuff = Object.entries(result).map(
      ([section, checks]) => {
        return /* @__PURE__ */ jsxs("div", { children: [
          /* @__PURE__ */ jsx("h3", { children: section }),
          /* @__PURE__ */ jsx("ul", { children: checks.filter((check) => check.status == "WARN" || check.status == "FAIL" || check.status == "ERROR").map((check) => {
            let unique_codes = check.codes ? check.codes.split(" ").map((code) => code.trim()).filter((v, i, a) => a.indexOf(v) === i) : [];
            check.codes = unique_codes.join(", ");
            return /* @__PURE__ */ jsxs("li", { children: [
              /* @__PURE__ */ jsx("strong", { children: /* @__PURE__ */ jsx("a", { href: "https://fonttools.github.io/fontspector/#" + check.check_id, children: check.check_id }) }),
              ": ",
              /* @__PURE__ */ jsxs("span", { className: check.status.toLowerCase(), children: [
                check.status,
                check.codes ? /* @__PURE__ */ jsxs("span", { children: [
                  " - ",
                  check.codes
                ] }) : ""
              ] })
            ] }, check.name);
          }) })
        ] }, section);
      }
    );
  }
  let repo_metadata = metadata[directory];
  let sandbox_metadata = servers?.sandbox?.metadata[family] || {};
  let production_metadata = servers?.production?.metadata[family] || {};
  let lastUpdated = history?.[0] ? new Date(history[0].date).toLocaleDateString() : "Unknown";
  return /* @__PURE__ */ jsxs("div", { children: [
    /* @__PURE__ */ jsx("h2", { children: family }),
    /* @__PURE__ */ jsxs("table", { children: [
      /* @__PURE__ */ jsxs("tr", { children: [
        /* @__PURE__ */ jsx("th", { children: "Directory" }),
        " ",
        /* @__PURE__ */ jsx("td", { children: directory })
      ] }),
      /* @__PURE__ */ jsxs("tr", { children: [
        /* @__PURE__ */ jsx("th", { children: "Date added" }),
        " ",
        /* @__PURE__ */ jsx("td", { children: new Date(repo_metadata.dateAdded).toLocaleDateString() })
      ] }),
      /* @__PURE__ */ jsxs("tr", { children: [
        /* @__PURE__ */ jsx("th", { children: "Last updated" }),
        " ",
        /* @__PURE__ */ jsx("td", { children: lastUpdated })
      ] }),
      /* @__PURE__ */ jsxs("tr", { children: [
        /* @__PURE__ */ jsx("th", { children: "Repo version" }),
        " ",
        /* @__PURE__ */ jsx("td", { children: repo_metadata.version })
      ] }),
      /* @__PURE__ */ jsxs("tr", { children: [
        /* @__PURE__ */ jsx("th", { children: "Sandbox version" }),
        " ",
        /* @__PURE__ */ jsx("td", { class: "sandbox", children: servers?.sandbox.families[family]?.version || "None" })
      ] }),
      /* @__PURE__ */ jsxs("tr", { children: [
        /* @__PURE__ */ jsx("th", { children: "Production version" }),
        " ",
        /* @__PURE__ */ jsx("td", { class: "production", children: servers?.production.families[family]?.version || "None" })
      ] }),
      pullsForThisDirectory.length > 0 ? /* @__PURE__ */ jsxs("tr", { children: [
        /* @__PURE__ */ jsx("th", { children: "Pull requests" }),
        /* @__PURE__ */ jsx("td", { children: /* @__PURE__ */ jsx("ul", { children: pullsForThisDirectory.map((pr) => {
          return /* @__PURE__ */ jsxs("li", { children: [
            /* @__PURE__ */ jsxs("a", { href: pr.html_url, children: [
              "#",
              pr.number
            ] }),
            " ",
            pr.title
          ] }, pr.number);
        }) }) })
      ] }) : ""
    ] }),
    CompareMetadata({
      repo: repo_metadata,
      sandbox: sandbox_metadata,
      production: production_metadata
    }),
    /* @__PURE__ */ jsxs("details", { children: [
      /* @__PURE__ */ jsx("summary", { children: "Version history" }),
      /* @__PURE__ */ jsx("ul", { children: history.map(({ server, version, date }) => {
        return /* @__PURE__ */ jsxs("li", { children: [
          new Date(date).toLocaleDateString(),
          ": -> ",
          /* @__PURE__ */ jsxs("span", { className: server, children: [
            server,
            ": ",
            version
          ] })
        ] }, `${server}-${version}`);
      }) })
    ] }),
    /* @__PURE__ */ jsxs("details", { children: [
      /* @__PURE__ */ jsx("summary", { children: "Upstream repository" }),
      /* @__PURE__ */ jsx("a", { href: repo_metadata?.source?.repositoryUrl, children: repo_metadata?.source?.repositoryUrl })
    ] }),
    /* @__PURE__ */ jsxs("details", { children: [
      /* @__PURE__ */ jsx("summary", { children: "Fontspector results" }),
      fbStuff
    ] }),
    /* @__PURE__ */ jsx("hr", {})
  ] });
}
function CompareMetadata({ repo, sandbox, production }) {
  let allKeys = /* @__PURE__ */ new Set([
    ...Object.keys(repo),
    ...Object.keys(sandbox),
    ...Object.keys(production)
  ]);
  allKeys.delete("version");
  allKeys.delete("dateAdded");
  allKeys.delete("isNoto");
  let s = (key, txt) => {
    if (key == "designer") {
      if (Array.isArray(txt)) {
        return txt.join(", ");
      }
      return txt;
    }
    return txt;
  };
  let truthy = (value) => {
    return value !== void 0 && value !== null && value !== "";
  };
  let allEmpty = (key) => {
    return !truthy(repo[key]) && !truthy(sandbox[key]) && !truthy(production[key]);
  };
  let servers = { "repo": repo, "sandbox": sandbox, "production": production };
  let furthest = (serverlist) => {
    if (serverlist.includes("production")) {
      return "production";
    }
    if (serverlist.includes("sandbox")) {
      return "sandbox";
    }
    return "repo";
  };
  let rows = Array.from(allKeys).filter((key) => !allEmpty(key) && (!repo[key] || !(repo[key] instanceof Object))).map((key) => {
    let clusters = {};
    for (let [server, data] of Object.entries(servers)) {
      let entry = s(key, data[key]);
      if (!clusters[entry]) {
        clusters[entry] = [];
      }
      clusters[entry].push(server);
    }
    return /* @__PURE__ */ jsxs("tr", { children: [
      /* @__PURE__ */ jsx("th", { children: key }),
      /* @__PURE__ */ jsx("td", { children: Object.keys(clusters).length == 1 ? Object.keys(clusters)[0] : /* @__PURE__ */ jsx("ul", { children: Object.entries(clusters).map(([value, servers2]) => {
        return /* @__PURE__ */ jsxs("li", { class: furthest(servers2), children: [
          value,
          " ",
          /* @__PURE__ */ jsxs("strong", { children: [
            "[",
            servers2.join(", "),
            "]"
          ] })
        ] }, value);
      }) }) })
    ] }, key);
  });
  return /* @__PURE__ */ jsx("table", { children: /* @__PURE__ */ jsx("tbody", { children: rows }) });
}
export function hasVersionDifference(family, metadata, servers) {
  let repoVersion = metadata[family]?.version?.split(";")[0];
  let sandboxVersion = servers?.sandbox?.families[family]?.version.split(";")[0];
  let productionVersion = servers?.production?.families[family]?.version.split(";")[0];
  return repoVersion && repoVersion !== sandboxVersion || productionVersion && productionVersion !== sandboxVersion;
}
