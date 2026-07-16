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
from typing import Optional, Dict, Any, List


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
        candidate_ttf_fonts: Optional[List[Any]] = None,
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
            subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "checkout", "-B", branch_name], check=True)

            # 4. Write updated METADATA.pb on the new feature branch
            meta_path.write_text(updated_pb_content, encoding="utf-8")

            # 4b. Copy candidate TTF font binaries into family directory ONLY if they correspond to existing fonts in Google Fonts
            if candidate_ttf_fonts:
                from .diffenator_runner import load_font_mappings

                family_dir = meta_path.parent
                existing_ttf_names = {p.name for p in family_dir.glob("*.ttf")}
                mappings = load_font_mappings(family_slug)

                for cand_item in candidate_ttf_fonts:
                    cand_path = Path(cand_item[0]) if isinstance(cand_item, (list, tuple)) else Path(cand_item)
                    cand_name = cand_path.name

                    target_name = None
                    if cand_name in mappings:
                        target_name = mappings[cand_name]
                    elif cand_name in existing_ttf_names:
                        target_name = cand_name

                    if target_name and target_name in existing_ttf_names:
                        if cand_path.exists() and cand_path.parent.resolve() != family_dir.resolve():
                            dest_path = family_dir / target_name
                            dest_path.write_bytes(cand_path.read_bytes())


            # 5. Add and commit METADATA.pb and updated font binaries
            subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "add", str(meta_path.parent)], check=True)
            commit_msg = f"Update {family_name} font binaries and METADATA.pb to upstream {upstream_version or upstream_commit}"
            subprocess.run([
                "git", "-c", "core.hooksPath=/dev/null",
                "-c", "user.name=github-actions[bot]",
                "-c", "user.email=github-actions[bot]@users.noreply.github.com",
                "commit", "-m", commit_msg
            ], check=True)

            # 6. Push branch to origin
            subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "push", "origin", branch_name, "--force"], check=True)

            # 7. Create PR via GitHub REST API
            pr_url = None
            api_error = None
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
                        "Authorization": f"Bearer {self.token}",
                        "Accept": "application/vnd.github+json",
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
                    err_text = e.read().decode("utf-8") if e.fp else str(e)
                    api_error = f"GitHub REST API HTTP {e.code}: {err_text}"
                    print(f"⚠️ PR Creation API Error: {api_error}")
                except Exception as e:
                    api_error = str(e)
                    print(f"⚠️ PR Creation Network Error: {api_error}")

            if not pr_url:
                # Fallback to gh CLI
                env = os.environ.copy()
                if self.token:
                    env["GITHUB_TOKEN"] = self.token
                    env["GH_TOKEN"] = self.token

                gh_res = subprocess.run(
                    [
                        "gh", "pr", "create",
                        "--repo", self.repo_slug,
                        "--base", base_branch,
                        "--head", branch_name,
                        "--title", pr_title,
                        "--body", pr_body,
                    ],
                    capture_output=True, text=True, env=env
                )
                if gh_res.returncode == 0:
                    pr_url = gh_res.stdout.strip()
                else:
                    gh_err = gh_res.stderr.strip() or gh_res.stdout.strip()
                    print(f"⚠️ gh CLI PR Creation Error: {gh_err}")
                    if not api_error:
                        api_error = f"gh CLI Error: {gh_err}"

            # Return to original branch
            subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "checkout", original_branch], check=False)

            if pr_url:
                return {
                    "created": True,
                    "branch_name": branch_name,
                    "pr_url": pr_url,
                    "status": "PR_CREATED",
                }
            else:
                return {
                    "created": False,
                    "branch_name": branch_name,
                    "error": api_error or "Failed to open PR via API or gh CLI",
                    "status": "PR_CREATION_FAILED",
                }

        except Exception as e:
            # Revert any uncommitted/unstaged changes and restore original branch
            subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "checkout", "--", "."], check=False)
            subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "checkout", original_branch], check=False)
            return {
                "created": False,
                "error": str(e),
                "status": "PR_CREATION_FAILED",
            }

