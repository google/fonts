---
toc: true
title: Server moves
---

```jsx
const updates = await FileAttachment("./data/versionhistory.json").json();

var movesbydate = {};
for (var [name, entries] of Object.entries(updates)) {
  for (var [server, moves] of Object.entries(entries)) {
    for (var move of moves) {
      var date = move["date"].replace(/T.*/, "");
      if (date == "1970-01-01") {
        continue;
      }
      if (!(date in movesbydate)) {
        movesbydate[date] = [];
      }
      var version = move["version"]
        .replace(/;.*/, "")
        .replace("Version", "version");
      movesbydate[date].push([name, version, server]);
    }
  }
}

display(
  Object.keys(movesbydate)
    .sort()
    .reverse()
    .slice(0, 50)
    .map((date) => (
      <div>
        <h2>{date}</h2>
        <ul>
          {movesbydate[date].sort().map(([name, version, server]) => (
            <li>
              <span class={server}>{name}</span> {version} →{" "}
              <span class={server}>{server}</span>{" "}
            </li>
          ))}
        </ul>
      </div>
    ))
);
```
