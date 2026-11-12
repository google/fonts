---
title: Fontc crater
---

```js
const fontc = await FileAttachment("./data/fontc.json").json();
import { RenderFailures, RenderSuccesses } from "./components/Fontc.js";
```

```js
const semiFlattened = fontc.summary.map((cur) => {
  // Move the `stats` object to the top level
  return {
    date: new Date(cur.began),
    rev: cur.fontc_rev,
    targets: cur.stats.total_targets,
    fontc_failed: cur.stats.fontc_failed,
    fontmake_failed: cur.stats.fontmake_failed,
    both_failed: cur.stats.both_failed,
    other: cur.stats.other_failure,
    identical: cur.stats.identical,
    similarity: cur.stats.diff_perc_including_failures,
  };
});

let prev_identical = undefined;
let updown = (v) => {
  if (v > 0) return html`<span class="up">↑${v}</span>`;
  if (v < 0) return html`<span class="down">↓${-v}</span>`;
  return "";
};

semiFlattened.forEach((cur) => {
  let identical_value = cur.identical;
  if (prev_identical) {
    let identical_change = cur.identical - prev_identical;
    if (identical_change) {
      cur.identical = html`${cur.identical} ${updown(identical_change)}`;
    } else {
      cur.identical = html`${cur.identical}`;
    }
  } else {
    cur.identical = html`${cur.identical}`;
  }
  prev_identical = identical_value;
});
const flattened = fontc.summary.flatMap((cur) =>
  Object.entries(cur.stats)
    .filter(([status, count]) =>
      ["both_failed", "fontmake_failed", "identical", "produced_diff"].includes(
        status
      )
    )
    .map(([status, count]) => {
      return {
        began: cur.began,
        status,
        count,
      };
    })
);
display(
  Inputs.table(semiFlattened, {
    format: {
      identical: (v) => v,
      date: (v) => v.toLocaleDateString(),
      similarity: (v) => `${v.toFixed(2)}%`,
    },
    reverse: true,
    width: {
      date: 90,
    },
  })
);
```

```js
const y2 = d3.scaleLinear(
  [0, 100],
  [0, d3.max(fontc.summary, (d) => d.stats.total_targets)]
);

display(
  Plot.plot({
    color: { legend: true },
    y: { axis: "left", label: "targets" },

    marks: [
      Plot.ruleY([0]),
      Plot.axisY(y2.ticks(), {
        anchor: "right",
        label: "%",
        color: "lightgreen",
        y: y2,
        tickFormat: y2.tickFormat(),
      }),

      Plot.areaY(flattened, {
        y: "count",
        x: (d) => new Date(d.began),
        fill: "status",
      }),
      Plot.lineY(
        fontc.summary,
        Plot.mapY((D) => D.map(y2), {
          x: (d) => new Date(d.began),
          y: (d) => d.stats.diff_perc_including_failures,
          stroke: "green",
          strokeWidth: 2,
        })
      ),
      Plot.lineY(
        fontc.summary,
        Plot.mapY((D) => D.map(y2), {
          x: (d) => new Date(d.began),
          y: (d) => d.stats.diff_perc_excluding_failures,
          stroke: "green",
          strokeOpacity: 0.2,
        })
      ),
    ],
    width,
  })
);
```

## Successes

```jsx
display(<RenderSuccesses successes={fontc.lastRun.success} />);
```

## Failures

```jsx
display(<RenderFailures failures={fontc.lastRun.failure} />);
```
