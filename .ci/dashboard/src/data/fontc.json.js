const resultUrl =
  "https://raw.githubusercontent.com/googlefonts/fontc_crater/refs/heads/main/results/";
const summary_request = await fetch(resultUrl + "summary.json");
const summary = await summary_request.json();
let lastRunFile = summary[summary.length - 1].results_file;
let details_request = await fetch(resultUrl + lastRunFile);
let lastRun = await details_request.json();
console.log(
  JSON.stringify(
    {
      summary,
      lastRun,
    },
    null,
    2
  )
);
