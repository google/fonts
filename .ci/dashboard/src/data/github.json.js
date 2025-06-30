import { Octokit } from "octokit";

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

let pulls = await octokit.rest.pulls.list({
  owner: "google",
  repo: "fonts",
});
for (let pull of pulls.data) {
  let files = await octokit.rest.pulls.listFiles({
    owner: "google",
    repo: "fonts",
    pull_number: pull.number,
  });
  let directories = files.data.map((file) => file.filename.split("/")[1]);
  pull.directories = [...new Set(directories)]; // Remove duplicates
}
console.log(
  JSON.stringify({
    pullRequests: pulls.data,
  })
);
