import { DuckDBInstance } from "@duckdb/node-api";

const instance = await DuckDBInstance.create("fontspector.db");
const db = await instance.connect();

const reader = await db.runAndReadAll(
  "SELECT distinct run FROM run_summary ORDER BY run DESC"
);
const rows = reader.getRows();
let allRuns = rows.map((c) => Number(c[0].micros) / 1000);
let latestRun = allRuns[0];

let headline = await db.runAndReadAll(`
select status, status_count as count FROM run_summary WHERE run = (select max(run) from run_summary) AND (status == 'FAIL' or status == 'WARN')
`);
const headlineRows = headline.getRows();

let fails_by_run = (
  await db.runAndReadAll(`
select run, status, status_count as count from run_summary
where status == 'WARN' or status == 'FAIL'
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
select run, check_id, status, status_count as count
  FROM fontspector.statuses_by_check
  order by count desc;
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

let mff = {};
for (var run of allRuns) {
  let most_failing_families = (
    await db.runAndReadAll(`
select family, status, status_count
  FROM fontspector.statuses_by_family WHERE epoch_ms(run) == ${run}
  AND family IN (
    select family from fontspector.statuses_by_family
    WHERE epoch_ms(run) == ${run}
    group by family
    order by sum(status_count) desc
    limit 10
    )
  order by status_count
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
let latestResultSQL = (
  await db.runAndReadAll(
    `select directory, file, section, check_id, status, codes
  FROM fontspector.results
    WHERE status NOT IN ('PASS', 'SKIP')
  `
  )
).getRows();
let latestResult = {};
for (var row of latestResultSQL) {
  let [directory, file, section, check_id, status, codes] = row;
  if (!latestResult[directory]) {
    latestResult[directory] = [];
  }
  latestResult[directory].push({
    file,
    section,
    check_id,
    status,
    codes,
  });
}

// Organise latestResult by section and file
for (const dir in latestResult) {
  const files = latestResult[dir];
  const organisedFiles = {};
  for (const file of files) {
    if (!organisedFiles[file.section]) {
      organisedFiles[file.section] = [];
    }
    organisedFiles[file.section].push(file);
  }
  latestResult[dir] = organisedFiles;
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
  latestResult,
};

process.stdout.write(JSON.stringify(results));
