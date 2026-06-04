---
toc: true
title: Push status
---

```js
const data = await FileAttachment("./data/gf_repo_data.json").json();
```

## Pushes

```js
import { interval, rangeInput } from "./util/range-slider.js";
import { utcQuarter } from "./util/moretime.js";

const thresholds = view(
  Inputs.radio(
    new Map([
      ["Weekly", d3.utcDay],
      ["Monthly", d3.utcMonth],
      ["Quarterly", utcQuarter],
      ["Yearly", d3.utcYear],
    ]),
    { label: "Period", value: d3.utcMonth }
  )
);
let maxEpoch = new Date(data.commits[0].date).getTime(),
  minEpoch = new Date(data.commits[data.commits.length - 1].date).getTime();

const dateRange = view(
  interval([minEpoch, maxEpoch], {
    format: ([start, end]) =>
      `${d3.utcFormat("%Y-%m-%d")(new Date(start))} - ${d3.utcFormat(
        "%Y-%m-%d"
      )(new Date(end))}`,
  })
);
```

```js
display(
  Plot.plot({
    color: { legend: true },
    marks: [
      Plot.lineY(
        data.commits,
        Plot.binX(
          { y: "count" },
          {
            x: "date",
            stroke: (d) => (d.kind == "family" ? d.status + " family" : d.kind),
            filter: (d) =>
              new Date(d.date) >= new Date(dateRange[0]) &&
              new Date(d.date) <= new Date(dateRange[1]),
            thresholds,
          }
        )
      ),
    ],
    width,
  })
);
```

<div class="grid grid-cols-2">
  <div class="card"><h1>Total commits by kind</h1>
  
```js
display(
  Plot.plot({
    y: { percent: true },
    color: { legend: true },
    marks: [
      Plot.waffleY(
        data.commits,
        Plot.groupX(
          { y: "count" },
          {
            x: 0,
            fill: (d) => (d.kind == "family" ? d.status + " family" : d.kind),
            offset: "normalize",
            filter: (d) =>
              new Date(d.date) >= new Date(dateRange[0]) &&
              new Date(d.date) <= new Date(dateRange[1]),
          }
        )
      ),
    ],
    width: 500,
    height: 400,
  })
);
```

  </div>
  <div class="card"><h1>Total commits by contributor</h1>

```js
let contributors = d3.rollup(
  data.commits.filter(
    (d) =>
      new Date(d.date) >= new Date(dateRange[0]) &&
      new Date(d.date) <= new Date(dateRange[1])
  ),
  (v) => v.length,
  (d) => d.author
);
let top_ten_authors = Array.from(contributors)
  .sort((a, b) => b[1] - a[1])
  .slice(0, 9) // "top 10" but we will add "Other"
  .map(([author, count]) => author);
let authorgroup = (x) =>
  top_ten_authors.includes(x.author) ? x.author : "Other";
display(
  Plot.plot({
    y: { percent: true },
    color: { legend: true, domain: top_ten_authors.concat(["Other"]) },
    marks: [
      Plot.waffleY(
        data.commits,
        Plot.groupX(
          { y: "count" },
          {
            x: 0,
            fill: authorgroup,
            order: top_ten_authors,
            offset: "normalize",
            filter: (d) =>
              new Date(d.date) >= new Date(dateRange[0]) &&
              new Date(d.date) <= new Date(dateRange[1]),
          }
        )
      ),
    ],
    width: 500,
    height: 400,
  })
);
```

  </div>
</div>

```js
display(Inputs.table(data.commits));
```

## Server pushes

### Going to sandbox server

```js
display(Inputs.table(data.pushes.sandbox));
```

### Going to production server

```js
display(Inputs.table(data.pushes.production));
```

```

```
