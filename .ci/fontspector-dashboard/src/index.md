---
toc: false
---

```js
const allResults = FileAttachment("./results.json").json();

const categoricals = {
    type: "categorical",
    domain: ['INFO', 'WARN', 'FAIL', 'ERROR'],
    range: ["#2182bf", "#bdae4f", "#cf4f2b", "#ff0000"],
    legend: true
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
Plot.plot({
  marks: [
    Plot.ruleY([0]),
    Plot.line(
      allResults.fails_by_run,
      Plot.stackY2({ y: "count", x: (d) => new Date(d.run), stroke: "status" })
    ),
    Plot.dot(
      allResults.fails_by_run,
      Plot.stackY2(
        { y: "count", x: "run", fill: "status", "tip": true }
      )
    )
  ],
  color: categoricals,
  width
})
```

</div>


<div>

<hr>

<div class="runslider">
<p>Select run:</p>

```js
const runSlider = view(html`<input type=range step=1 min=0 max=${allResults.allRuns.length-1} value=${allResults.allRuns.length-1}>`)
```

```js
const selectedRun = allResults.allRuns[allResults.allRuns.length-(1+runSlider)]
```

<span class="when">${(new Date(selectedRun)).toISOString().replace("T", " ").replace(/\.\d+Z$/, "") }</span>
</div>


<div class="grid grid-cols-2">
  <div class="card">
    <h2>Most failing checks</h2>

```js
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
    Plot.rectY(allResults.most_failing_checks[selectedRun],
  
    { y: "count", x: "check_id", sort: {x: "y", reverse: "true"}, tip: true, fill: "status" },
  )
]})
```

  </div>

  <div class="card">

## Most failing families


```js
Plot.plot({
   x: {
    tickRotate: -30,
    label: null,

  },
  color: categoricals,
  marks: [
  
    Plot.ruleY([0]),
    Plot.barY(allResults.most_failing_families[selectedRun],
    { y: "count", x: "family", tip: true, fill: "status", order: "status", sort: {x: "y", reverse: true} },
  ),
],
})
```

  </div>
</div>

</div>



<style>

.card {
  height: 450px;
}

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  text-wrap: balance;
  text-align: center;
}

.runslider {
  height: 50px;
}

.runslider div { display: inline-block}
.runslider div:first-child { display: inline-block; width: 50% ; }
.runslider p { display: inline-block; font-family: sans-serif; }

.hero h1 {
  margin: 1rem 0;
  padding: 1rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero h2 {
  margin: 0;
  max-width: 34em;
  font-size: 40px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--theme-foreground-muted);
  vertical-align: middle; 
  display: inline-block;
}

.hero h2 .huge {
  font-size: 60px;
  font-weight: 700;
  vertical-align: middle; 
}

.warn { color: #bdae4f; }
.fail { color: #cf4f2b; }


@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

</style>
