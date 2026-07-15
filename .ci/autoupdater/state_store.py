"""
State and cache store for tracking family update checks and pipeline status.
Located internally within google/fonts at .ci/autoupdater/state_store.py.
"""

import sqlite3
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone


class StateStore:
    def __init__(self, db_path: str = "gf_autoupdater_state.db"):
        self.db_path = db_path
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tracked_families (
                    family_name TEXT PRIMARY KEY,
                    repository_url TEXT,
                    license TEXT,
                    current_commit TEXT,
                    current_version TEXT,
                    last_checked_at TEXT,
                    status TEXT DEFAULT 'ACTIVE'
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS update_checks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    family_name TEXT,
                    checked_at TEXT,
                    has_update INTEGER,
                    update_type TEXT,
                    upstream_version TEXT,
                    upstream_commit TEXT,
                    safety_score REAL,
                    safety_tier TEXT,
                    pr_url TEXT,
                    status TEXT,
                    FOREIGN KEY (family_name) REFERENCES tracked_families (family_name)
                )
                """
            )
            conn.commit()

    def register_family(
        self,
        family_name: str,
        repository_url: Optional[str],
        license_type: str = "OFL",
        current_commit: Optional[str] = None,
        current_version: Optional[str] = None,
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO tracked_families (family_name, repository_url, license, current_commit, current_version, last_checked_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(family_name) DO UPDATE SET
                    repository_url=excluded.repository_url,
                    license=excluded.license,
                    current_commit=COALESCE(excluded.current_commit, tracked_families.current_commit),
                    current_version=COALESCE(excluded.current_version, tracked_families.current_version),
                    last_checked_at=excluded.last_checked_at
                """,
                (family_name, repository_url, license_type, current_commit, current_version, now),
            )
            conn.commit()

    def record_check_result(
        self,
        family_name: str,
        has_update: bool,
        update_type: str,
        upstream_version: Optional[str] = None,
        upstream_commit: Optional[str] = None,
        safety_score: Optional[float] = None,
        safety_tier: Optional[str] = None,
        pr_url: Optional[str] = None,
        status: str = "CHECKED",
    ) -> int:
        now = datetime.now(timezone.utc).isoformat()
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO update_checks
                (family_name, checked_at, has_update, update_type, upstream_version, upstream_commit, safety_score, safety_tier, pr_url, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    family_name,
                    now,
                    1 if has_update else 0,
                    update_type,
                    upstream_version,
                    upstream_commit,
                    safety_score,
                    safety_tier,
                    pr_url,
                    status,
                ),
            )
            check_id = cursor.lastrowid
            cursor.execute(
                "UPDATE tracked_families SET last_checked_at = ? WHERE family_name = ?",
                (now, family_name),
            )
            conn.commit()
            return check_id

    def get_family(self, family_name: str) -> Optional[Dict[str, Any]]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tracked_families WHERE family_name = ?", (family_name,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_recent_checks(self, family_name: str, limit: int = 5) -> List[Dict[str, Any]]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM update_checks WHERE family_name = ? ORDER BY id DESC LIMIT ?",
                (family_name, limit),
            )
            rows = cursor.fetchall()
            return [dict(r) for r in rows]
