import { DuckDBInstance } from "@duckdb/node-api";

const instance = await DuckDBInstance.create("../../fontspector.db");
const db = await instance.connect();

const reader = await db.runAndReadAll(
  "SELECT distinct run FROM results ORDER BY run DESC"
);
const rows = reader.getRows();
let allRuns = rows.map((c) => Number(c[0].micros) / 1000);
let latestRun = allRuns[0];

let headline = await db.runAndReadAll(`
select status, count(status) as count
  FROM (SELECT * FROM fontspector.results WHERE epoch_ms(run) == ${latestRun})
  where status == 'WARN' or status == 'FAIL'
  group by status`);
const headlineRows = headline.getRows();

let fails_by_run = (
  await db.runAndReadAll(`
select run, status, count(status) as count from fontspector.results
where status == 'WARN' or status == 'FAIL'
group by status, run
order by run, status;
`)
).getRows();
fails_by_run = fails_by_run.map((c) => {
  return {
    run: Number(c[0].micros) / 1000,
    status: c[1],
    count: Number(c[2]),
  };
});

let most_failing_checks = (
  await db.runAndReadAll(`
select run, check_id, status, count(status) as count
  FROM fontspector.results
  where status == 'FAIL' or status == 'ERROR' or status == 'WARN'
  group by run, check_id, status order by count desc;
`)
).getRows();
let mfc = {};
for (var row of most_failing_checks) {
  let key = Number(row[0].micros) / 1000;
  if (!mfc[key]) {
    mfc[key] = [];
  }
  if (mfc[key].length < 10) {
    mfc[key].push({
      check_id: row[1],
      status: row[2],
      count: Number(row[3]),
    });
  }
}

/*

```sql id=most_failing_families
select directory as family, status, count(status) as count
  FROM (SELECT * FROM fontspector.results WHERE epoch_ms(run) == ${allRuns[runSlider]})
  where (status == 'FAIL' or status == 'ERROR' or status == 'WARN')
  AND family in (SELECT directory as family FROM fontspector.results WHERE status == 'FAIL' or status == 'ERROR' or status == 'WARN' group by family order by count(status) desc limit 20)
  group by directory, status;
```
*/


let mff = {};
for (var run of allRuns) {
  let most_failing_families = (
    await db.runAndReadAll(`
select directory as family, status, count(status) as count
  FROM (SELECT * FROM fontspector.results WHERE epoch_ms(run) == ${run})
  where (status == 'FAIL' or status == 'ERROR' or status == 'WARN')
  AND family in (SELECT directory as family FROM fontspector.results WHERE status == 'FAIL' or status == 'ERROR' or status == 'WARN' group by family order by count(status) desc limit 20)
  group by directory, status;
  `)
  ).getRows();
  mff[run] = [];
  for (var row of most_failing_families) {
    mff[run].push({
      family: row[0],
      status: row[1],
      count: Number(row[2]),
    });
  }
}
const results = {
  headline: {
    [headlineRows[0][0]]: Number(headlineRows[0][1]),
    [headlineRows[1][0]]: Number(headlineRows[1][1]),
  },
  allRuns,
  fails_by_run,
  most_failing_checks: mfc,
  most_failing_families: mff,
};

process.stdout.write(JSON.stringify(results));
