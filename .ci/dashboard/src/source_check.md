---
title: Fontc crater sources check
toc: false
---

```js
const fontc = await FileAttachment("./data/fontc.json").json();
const metadata = await FileAttachment("./data/metadata.json").json();
const reviewlist = await FileAttachment("./data/fontc_review.json").json();

const family_to_directory = Object.fromEntries(
  Object.entries(metadata).map(([k, v]) => [v.name, k])
);
const directory_to_family = Object.fromEntries(
  Object.entries(metadata).map(([k, v]) => [k, v.name])
);

function fontcKeyToGithubAndSha(key, state) {
  let match = key.match(
    /^([^\/]+)\/([^\/]+)\/.*\?([a-f0-9]+) \((\S+)\)/
  );
  if (match) {
    let [_, owner, repo, sha, mode] = match;
    return { repo: `${owner}/${repo}`, sha, state };
  }
}

let fontcResults = [];
for (let successKey of Object.keys(fontc.lastRun.success)) {
  let githubAndSha = fontcKeyToGithubAndSha(successKey, "success");
  if (githubAndSha) {
    fontcResults.push(githubAndSha);
  }
}
for (let failureKey of Object.keys(fontc.lastRun.failure)) {
  let githubAndSha = fontcKeyToGithubAndSha(failureKey, "failure");
  if (githubAndSha) {
    fontcResults.push(githubAndSha);
  }
}

const summary = Object.keys(metadata).map((directory) => {
  const md = metadata[directory];
  const family = md.name;
  let source_state = "Good";
  if (!md.source) {
    source_state = "No source information";
  } else if (!md.source.repositoryUrl) {
    source_state = "Missing repository URL";
  } else if (!md.source.commit) {
    source_state = "Missing SHA";
  } else if (!md.source.configYaml) {
    source_state = "Missing config.yaml";
  } else if (!md.source.commit.match(/^[0-9a-f]{40}$/)) {
    source_state = "Invalid commit hash";
  }
  let github =
    md.source?.repositoryUrl &&
    md.source.repositoryUrl.match(/github.com\/([^/]+\/[^/]+)/)?.[1];
  let fontcResult = fontcResults.find((r) => r.repo === github);
  let fontcState = "unknown";
  if (fontcResult) {
    fontcState = fontcResult.state;
  }
  if (source_state != "Good" && fontcState == "unknown") {
    fontcState = "insufficient source data: " + source_state;
  }
  return {
    directory,
    family,
    slug:
      source_state == "Good"
        ? github + "/" + md.source?.configYaml + "@" + md.source?.commit
        : "",
    github,
    sha: md.source?.commit,
    source_state,
    fontc_state: fontcState,
    reviewed: reviewlist[directory],
  };
});

let successes = summary.filter((s) => s.fontc_state == "success");
let failures = summary.filter((s) => s.fontc_state == "failure");
let insufficient = summary.filter((s) =>
  s.fontc_state.startsWith("insufficient source data")
);
let unknown = summary.filter((s) => s.fontc_state == "unknown");
let reviewed = summary.filter((s) => s.reviewed == "yes");
```

<div class="hero">
  <h2> Total families: <span class="huge ">${ summary.length }</h2>
    <h2> Ran: <span class="pass">${ successes.length }</span> + <span class="fail">${ failures.length}</span> = <span class="huge">${ successes.length + failures.length }</span></h2>
    <h2> Insufficient source data: <span class="">${ insufficient.length }<br/>
    Unaccounted: <span class="">${ unknown.length }</h2>
    <h2>Reviewed: <span class="">${ reviewed.length } (${ Math.floor(reviewed.length / summary.length * 100) }%)</span></h2>
</div>

```js
const domain = ["success", "failure", "insufficient source data", "unknown"];
display(
  Plot.plot({
    y: { percent: true },
    color: { legend: true },
    marks: [
      Plot.waffleY(
        summary,
        Plot.groupX(
          { y: "count" },
          {
            x: 0,
            fill: (d) =>
              d.fontc_state.replace(
                /insufficient source data: (.+)/,
                "insufficient source data"
              ),
            offset: "normalize",
            order: domain,
          }
        )
      ),
    ],
    width: 500,
    height: 400,
    color: {
      domain,
      range: ["#1a821aff", "#8d2929ff", "#4ee5f9ff", "#aaaaaa"],
      legend: true,
    },
  })
);
```

## Details

```js
display(
  Inputs.table(summary, {
    rows: 200,
    columns: ["directory", "family", "slug", "fontc_state", "reviewed"],
    sort: "fontc_state",
    reverse: true,
    header: {
      directory: "Directory",
      family: "Family name",
      slug: "Source",
      fontc_state: "Fontc state",
      reviewed: "Reviewed",
    },
    format: {
      fontc_state: (d) => {
        if (d == "success") {
          return html`<span class="pass">${d}</span>`;
        } else if (d == "failure") {
          return html`<span class="fail">${d}</span>`;
        } else if (d.startsWith("insufficient source data")) {
          return html`<span class="insufficient"
            >${d.replace("insufficient source data:", "")}</span
          >`;
        } else {
          return html`<b>${d}</b>`;
        }
      },
    },
  })
);
```
