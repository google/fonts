function RenderFamily(family) {
    let match = family.match(/^([^\/]+)\/([^\/]+)\/(\S+)\?([a-f0-9]+) \((\S+)\) (\S+)/);
    if (!match) {
        return <span>{family}</span>;
    }
    let [_, owner, repo, path, sha, config, mode] = match;
        return (
            <span>
                <a href={
                    `https://github.com/${owner}/${repo}`
                }>
                    {owner}/{repo}
                </a> / <a href={
                    `https://github.com/${owner}/${repo}/blob/${sha}/${path}`
                }>
                    {path
                }</a> @ <a href={
                        `https://github.com/${owner}/${repo}/commit/${sha}`
                }>
                    {sha.substring(0, 7)}
                </a> (<a href={
                    `https://github.com/${owner}/${repo}/blob/${sha}/sources/${config}`
                    }>{config}</a>) {mode}
            </span>
        );
}

function RenderCompileFailed(failure) {
    return ["fontmake", "fontc"].map(compiler => {
        if (failure[compiler]) {
            return (
                <div key={compiler}>
                    <h3>{compiler} failed</h3>
                    <pre>% {failure[compiler].command}</pre>
                    <pre class="pre-wrap">{failure[compiler].stderr}</pre>
                </div>
            );
        }
        return <div/>;
    });
}

export function RenderFailures({failures} = {}) {
    return <div>
        {
            Object.entries(failures).map(([family, problems]) => (
                <details key={family}>
                    <summary>{RenderFamily(family)}</summary>
                    {problems.compile_failed && RenderCompileFailed(problems.compile_failed)}

                </details>
            ))
        }
    </div>
}

function RenderDiffs(diffs) {
    return <div>
        <h3>Diffs</h3>
        <ul>
            {Object.entries(diffs).map(([area, diff]) => (
                <li key={area}>{ area} : { diff }</li>
            ))}
        </ul>
        </div>
}

let pct = (problems) => problems.diffs ? (problems.diffs.total * 100.0) : 100; 

export function RenderSuccesses({successes} = {}) {
    return <div>
        {
            Object.entries(successes).filter( ([family, problems]) => {
                return problems.diffs && problems.diffs.total > 0;
            }).sort( ([familyA, problemsA], [familyB, problemsB]) => {
                return pct(problemsB) - pct(problemsA);
            }).map(([family, problems]) => (
                <details key={family}>
                    <summary>{RenderFamily(family)} ({pct(problems).toFixed(2)}%)</summary>
                    {problems.diffs && RenderDiffs(problems.diffs)}

                </details>
            ))
        }
    </div>
}