"""
GitHub PR Creator module for submitting automated font update pull requests.
Located internally within google/fonts at .ci/autoupdater/pr_creator.py.
"""

import os
import re
import json
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Dict, Any


class PRCreator:
    """Creates git feature branch, commits updated METADATA.pb, and opens a GitHub PR."""

    def __init__(self, github_token: Optional[str] = None, repo_slug: str = "google/fonts"):
        self.token = github_token or os.environ.get("GITHUB_TOKEN")
        self.repo_slug = repo_slug

    def create_pull_request(
        self,
        family_name: str,
        metadata_filepath: str,
        updated_pb_content: str,
        pr_title: str,
        pr_body: str,
        upstream_version: Optional[str] = None,
        upstream_commit: Optional[str] = None,
        base_branch: str = "main",
        dry_run: bool = False,
    ) -> Dict[str, Any]:

        meta_path = Path(metadata_filepath)
        family_slug = re.sub(r'[^a-zA-Z0-9_-]', '', family_name.lower().replace(" ", "-"))
        version_clean = re.sub(r'[^a-zA-Z0-9_.-]', '', upstream_version or "latest")
        commit_short = (upstream_commit[:7] if upstream_commit else "")
        
        branch_name = f"autoupdate/{family_slug}-v{version_clean}"
        if commit_short:
            branch_name += f"-{commit_short}"

        if dry_run:
            return {
                "created": False,
                "dry_run": True,
                "branch_name": branch_name,
                "title": pr_title,
                "message": "Dry-run mode: PR creation skipped.",
            }

        try:

            # 2. Record current branch
            curr_branch_res = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True, text=True, check=True
            )
            original_branch = curr_branch_res.stdout.strip()

            # 3. Create and checkout feature branch
            subprocess.run(["git", "checkout", "-B", branch_name], check=True)

            # 4. Write updated METADATA.pb on the new feature branch
            meta_path.write_text(updated_pb_content, encoding="utf-8")

            # 5. Add and commit METADATA.pb
            subprocess.run(["git", "add", str(meta_path)], check=True)
            commit_msg = f"Update {family_name} METADATA.pb to upstream {upstream_version or upstream_commit}"
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)


            # 5. Push branch to origin
            subprocess.run(["git", "push", "origin", branch_name, "--force"], check=True)

            # 6. Create PR via GitHub REST API
            pr_url = None
            if self.token:
                url = f"https://api.github.com/repos/{self.repo_slug}/pulls"
                payload = {
                    "title": pr_title,
                    "body": pr_body,
                    "head": branch_name,
                    "base": base_branch,
                }
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode("utf-8"),
                    headers={
                        "Authorization": f"token {self.token}",
                        "Accept": "application/vnd.github.v3+json",
                        "User-Agent": "GoogleFonts-AutoUpdater/1.0.0",
                        "Content-Type": "application/json",
                    },
                    method="POST",
                )
                try:
                    with urllib.request.urlopen(req, timeout=15) as resp:
                        res_data = json.loads(resp.read().decode("utf-8"))
                        pr_url = res_data.get("html_url")
                except urllib.error.HTTPError as e:
                    pass

            if not pr_url:
                # Fallback to gh CLI
                gh_res = subprocess.run(
                    [
                        "gh", "pr", "create",
                        "--repo", self.repo_slug,
                        "--base", base_branch,
                        "--head", branch_name,
                        "--title", pr_title,
                        "--body", pr_body,
                    ],
                    capture_output=True, text=True
                )
                if gh_res.returncode == 0:
                    pr_url = gh_res.stdout.strip()

            # Return to original branch
            subprocess.run(["git", "checkout", original_branch], check=False)

            return {
                "created": True,
                "branch_name": branch_name,
                "pr_url": pr_url or f"https://github.com/{self.repo_slug}/pulls",
                "status": "PR_CREATED",
            }
        except Exception as e:
            # Return to original branch on failure
            subprocess.run(["git", "checkout", original_branch], check=False)
            return {
                "created": False,
                "error": str(e),
                "status": "PR_CREATION_FAILED",
            }
