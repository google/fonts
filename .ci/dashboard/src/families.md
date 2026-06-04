---
toc: true
title: Family status
---

```js
import { RenderFamily, hasVersionDifference } from "./components/Family.js";

const updates = await FileAttachment("./data/versionhistory.json").json();
const allResults = await FileAttachment("./data/fontspector.json").json();
const metadata = await FileAttachment("./data/metadata.json").json();
const servers = await FileAttachment("./data/servers.json").json();
const github = await FileAttachment("./data/github.json").json();

const family_to_directory = Object.fromEntries(
  Object.entries(metadata).map(([k, v]) => [v.name, k])
);
const directory_to_family = Object.fromEntries(
  Object.entries(metadata).map(([k, v]) => [k, v.name])
);
let filters = view(
  Inputs.checkbox(["Version differences", "Open pull requests"], false)
);
```

```js
let families = Object.keys(family_to_directory);
if (filters.includes("Open pull requests")) {
  families = Object.entries(metadata)
    .filter(([directory, md]) =>
      github.pullRequests.some((pr) => pr.directories.includes(directory))
    )
    .map(([directory, md]) => md.name);
}
if (filters.includes("Version differences")) {
  families = families.filter((family) =>
    hasVersionDifference(family, metadata, servers)
  );
}
families = families.sort();
const searchBar = Inputs.search(families, {
  placeholder: "Search families...",
});
const search = view(searchBar);
```

```jsx
let render = (x) => (
  <RenderFamily
    servers={servers}
    family={x}
    directory={family_to_directory[x]}
    allResults={allResults}
    metadata={metadata}
    updates={updates}
    pullRequests={github.pullRequests}
  />
);

if (search.length < 100) {
  let rows = search.map(render);
  display(<div>{rows}</div>);
} else {
  display(<div />);
}
```
