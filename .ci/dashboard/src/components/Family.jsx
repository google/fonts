export function RenderFamily({family, directory, allResults, metadata, servers, updates, pullRequests} = {}) {
  let result = allResults.latestResult[directory];
  let fbStuff = <div/>;
  let history = [];
  let pullsForThisDirectory = pullRequests?.filter(pr => pr.directories.includes(directory)) || [];
  if (updates[family]) {
    for (let [server, moves] of Object.entries(updates[family])) {
      for (let {version, date} of moves) {
        if (date != "1970-01-01T00:00:00") {
          history.push({server, version, date});
        }
      }
    }
  }
  history = history.sort((a, b) => new Date(b.date) - new Date(a.date));
  if (result) {
    for (let section of Object.keys(result)) {
      // If no check has status: WARN or status: FAIL, skip the section
      let checks = result[section];
      if (checks.filter(check => check.status === 'WARN' || check.status === 'FAIL').length == 0) {
        delete result[section];
      }
    }
   fbStuff = Object.entries(result).map(
    ([section, checks]) => {
      return <div key={section}>
        <h3>{section}</h3>
        <ul>
          {checks.filter(check => check.status == "WARN" || check.status == "FAIL" || check.status == "ERROR").map(check => {
            let unique_codes = check.codes ? check.codes.split(' ').map(code => code.trim()).filter((v, i, a) => a.indexOf(v) === i) : [];
            check.codes = unique_codes.join(', ');
            return <li key={check.name}>
              <strong><a href={"https://fonttools.github.io/fontspector/#"+check.check_id}>{check.check_id}</a></strong>: <span  className={check.status.toLowerCase()}>{check.status}
              {check.codes ? <span> - {check.codes}</span> : ''}
              </span>
            </li>;
          })}
        </ul>
      </div>;
    }
  );
  }
  let repo_metadata = metadata[directory];
  let sandbox_metadata = servers?.sandbox?.metadata[family] || {};
  let production_metadata = servers?.production?.metadata[family] || {};

  let lastUpdated = (history?.[0]) ? new Date(history[0].date).toLocaleDateString() : 'Unknown';
  return <div>
    <h2>{family}</h2>
      <table>
        <tr><th>Directory</th> <td>{directory}</td></tr>
        <tr><th>Date added</th> <td>{new Date(repo_metadata.dateAdded).toLocaleDateString()}</td></tr>
        <tr><th>Last updated</th> <td>{lastUpdated}</td></tr>
        <tr><th>Repo version</th> <td>{repo_metadata.version}</td></tr>
        <tr><th>Sandbox version</th> <td class="sandbox">{servers?.sandbox.families[family]?.version || "None"}</td></tr>
        <tr ><th>Production version</th> <td class="production">{servers?.production.families[family]?.version || "None"}</td></tr>
        { pullsForThisDirectory.length > 0 ?
        <tr><th>Pull requests</th>
          <td>
            <ul>
            {pullsForThisDirectory.map(pr => {
              return <li key={pr.number}>
                <a href={pr.html_url}>#{pr.number}</a> {pr.title}
              </li>;
            })}
            </ul>
          </td>
        </tr> : ''}
      </table>

      {CompareMetadata({
        repo: repo_metadata,
        sandbox: sandbox_metadata,
        production: production_metadata,
      })}

      <details>
        <summary>Version history</summary>
        <ul>
        {history.map(({server, version, date}) => {
          return <li key={`${server}-${version}`}>
            {new Date(date).toLocaleDateString()}: -&gt; <span className={server}>{server}: {version}</span>
          </li>;
        })}
        </ul>
      </details>

      <details>
        <summary>Upstream repository</summary>
        <a href={repo_metadata?.source?.repositoryUrl}>{repo_metadata?.source?.repositoryUrl}</a>
      </details>

      <details>
        <summary>Fontspector results</summary>
        {fbStuff}
      </details>
        <hr/>
  </div>;
}

function CompareMetadata({repo, sandbox, production}) {
  let allKeys = new Set([
    ...Object.keys(repo),
    ...Object.keys(sandbox),
    ...Object.keys(production),
  ]);
  // Skip "version", we did that
  allKeys.delete("version");
  allKeys.delete("dateAdded");
  allKeys.delete("isNoto");
  let s = (key, txt) => {
    if (key == "designer") {
      // May be a string or a list. Convert list to comma-separated string
      if (Array.isArray(txt)) {
        return txt.join(', ');
      }
      return txt;
    }
    return txt
  }
  let truthy = (value) => {
    return value !== undefined && value !== null && value !== '';
  };
  let allEmpty = (key) => {
    return !truthy(repo[key]) && !truthy(sandbox[key]) && !truthy(production[key]);
  };
  let servers = { "repo": repo, "sandbox": sandbox, "production": production };
  let furthest = (serverlist) => {
    if (serverlist.includes("production")) {
      return "production";
    }
    if (serverlist.includes("sandbox")) {
      return "sandbox";
    }
    return "repo";
  }

  let rows = Array.from(allKeys).filter((key) => !allEmpty(key) && (!repo[key] || !(repo[key] instanceof Object))).map(key => {
    let clusters = {};
    for (let [server, data] of Object.entries(servers)) {
      let entry = s(key, data[key]);
      if (!clusters[entry]) {
        clusters[entry] = [];
      }
      clusters[entry].push(server);
    }
    return <tr key={key}>
      <th>{key}</th>
      <td>{
        Object.keys(clusters).length == 1 ? Object.keys(clusters)[0] :
        <ul>
          {Object.entries(clusters).map(([value, servers]) => {
            return <li key={value} class={furthest(servers)}>
              {value} <strong>[{servers.join(', ')}]</strong>
            </li>;
          })}
        </ul>
      }</td>
    </tr>;
  })
  return <table>
    <tbody>
      {rows}
    </tbody>
  </table>;
}

export function hasVersionDifference(family, metadata, servers) {
    let repoVersion = metadata[family]?.version?.split(";")[0];
    let sandboxVersion = servers?.sandbox?.families[family]?.version.split(";")[0];
    let productionVersion = servers?.production?.families[family]?.version.split(";")[0];
    return (repoVersion && repoVersion !== sandboxVersion) ||
           (productionVersion && productionVersion !== sandboxVersion);
}
