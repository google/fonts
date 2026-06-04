from gftools.push.trafficjam import PushItems
from datetime import datetime
import pygit2
import os
import json

def get_commits(repo):
    commits = list(repo.walk(repo.head.target))
    res = []
    for idx in range(1, len(commits)):
        current_commit = commits[idx - 1]
        prev_commit = commits[idx]

        # Basic meta
        author = current_commit.author.name
        title = current_commit.message.split("\n")[0]
        date = datetime.fromtimestamp(int(current_commit.commit_time))

        if "Merge branch" in current_commit.message:
            continue
        diff = prev_commit.tree.diff_to_tree(current_commit.tree)
        # Commit has all new files
        if all(d.status == 1 for d in diff.deltas):
            status = "new"
        # Contains modifications
        elif any(d.status == 3 for d in diff.deltas):
            status = "modified"
        else:
            status = "modified"

        # Type of commit
        if any(d.new_file.path.endswith(("ttf", "otf")) for d in diff.deltas):
            kind = "family"
        elif any(
            d.new_file.path.endswith(("metadata.pb", "DESCRIPTION.en_us.html"))
            for d in diff.deltas
        ):
            kind = "metadata"
        elif any(d.new_file.path.endswith("info.pb") for d in diff.deltas):
            kind = "designer"
        else:
            kind = "infrastructure"

        res.append(
            {
                "date": date.isoformat(),
                "title": title,
                "author": author,
                "status": status,
                "kind": kind,
                "id": str(current_commit.id),
            }
        )
    return res

repo_path = os.environ["GF_REPO_PATH"]
repo = pygit2.Repository(repo_path)
commits = get_commits(repo)

sb_path = os.path.join(repo_path, "to_sandbox.txt")
sb_families = PushItems.from_server_file(sb_path)
prod_path = os.path.join(repo_path, "to_production.txt")
prod_families = PushItems.from_server_file(prod_path)

commit_data = {
    "last_run": datetime.now().strftime("%Y-%m-%d"),
    "commits": commits,
    "pushes": {
        "sandbox": [i.to_json() for i in sb_families],
        "production": [i.to_json() for i in prod_families],
    },
}

print(json.dumps(commit_data))