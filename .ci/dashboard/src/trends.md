---
title: Fontspector QA trends
toc: false
---

```js
const allResults = await FileAttachment("./data/fontspector.json").json();
const metadata = await FileAttachment("./data/metadata.json").json();

const categoricals = {
  type: "categorical",
  domain: ["INFO", "WARN", "FAIL", "ERROR"],
  range: ["#2182bf", "#bdae4f", "#cf4f2b", "#ff0000"],
  legend: true,
};
```

<div class="hero">
  <h1> Google Fonts QA </h1>
  <h2> WARNs last run: <span class="huge warn">${ allResults.headline.WARN }</h2>
  <h2> FAILs last run: <span class="huge fail">${ allResults.headline.FAIL }</h2>
</div>

<div class="card">

## Overall failures

```js
display(
  Plot.plot({
    marks: [
      Plot.ruleY([0]),
      Plot.line(
        allResults.fails_by_run,
        Plot.stackY2({
          y: "count",
          x: (d) => new Date(d.run),
          stroke: "status",
        })
      ),
      Plot.dot(
        allResults.fails_by_run,
        Plot.stackY2({ y: "count", x: "run", fill: "status", tip: true })
      ),
    ],
    color: categoricals,
    width,
  })
);
```

</div>

<div>

<hr>

<div class="runslider">
<p>Select run:</p>

```js
const runSlider = view(
  html`<input
    type="range"
    step="1"
    min="0"
    max=${allResults.allRuns.length - 1}
    value=${allResults.allRuns.length - 1}
  />`
);
```

```js
const selectedRun =
  allResults.allRuns[allResults.allRuns.length - (1 + runSlider)];
```

<span class="when">${(new Date(selectedRun)).toISOString().replace("T", " ").replace(/\.\d+Z$/, "") }</span>

</div>

<div class="grid grid-cols-2">
  <div class="card">
    <h2>Most failing checks</h2>

```js
display(
  Plot.plot({
    marginBottom: 90,
    marginLeft: 90,
    x: {
      tickRotate: -30,
      label: null,
    },
    color: categoricals,
    marks: [
      Plot.ruleY([0]),
      Plot.rectY(
        allResults.most_failing_checks[selectedRun],

        {
          y: "count",
          x: "check_id",
          sort: { x: "y", reverse: "true" },
          tip: true,
          fill: "status",
        }
      ),
    ],
  })
);
```

  </div>

  <div class="card">

## Most failing families

```js
const family_to_directory = Object.fromEntries(
  Object.entries(metadata).map(([k, v]) => [v.name, k])
);
const directory_to_family = Object.fromEntries(
  Object.entries(metadata).map(([k, v]) => [k, v.name])
);

display(
  Plot.plot({
    x: {
      tickRotate: -30,
      label: null,
    },
    color: categoricals,
    marks: [
      Plot.ruleY([0]),
      Plot.barY(allResults.most_failing_families[selectedRun], {
        y: "count",
        x: (d) => directory_to_family[d.family],
        tip: true,
        fill: "status",
        order: "status",
        sort: { x: "y", reverse: true },
      }),
    ],
  })
);
```

  </div>
</div>
</div>
