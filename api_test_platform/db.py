# ============ 数据库层 ============

import sqlite3
from pathlib import Path
from models import TestCase

DB_FILE = "test_platform.db"


class Database:
    def __init__(self, db_file=DB_FILE):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self._init_tables()

    def _init_tables(self):
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS test_case (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            method TEXT DEFAULT 'GET',
            url TEXT NOT NULL,
            headers TEXT DEFAULT '{}',
            body TEXT,
            expected_status INTEGER DEFAULT 200,
            expected_field TEXT,
            expected_value TEXT
        );
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id INTEGER,
            case_name TEXT,
            passed INTEGER,
            status_code INTEGER,
            response_time REAL,
            error_msg TEXT,
            timestamp TEXT
        );
        """)
        self.conn.commit()

    def add_case(self, case: TestCase):
        ok, msg = case.validate()
        if not ok:
            return None, msg
        cur = self.conn.execute("""
            INSERT INTO test_case(name, method, url, headers, body, expected_status, expected_field, expected_value)
            VALUES (?,?,?,?,?,?,?,?)
        """, (case.name, case.method, case.url, str(case.headers),
              str(case.body) if case.body else None,
              case.expected_status, case.expected_field, case.expected_value))
        self.conn.commit()
        case.id = cur.lastrowid
        return case.id, "OK"

    def get_all_cases(self):
        cur = self.conn.execute("SELECT * FROM test_case ORDER BY id")
        rows = cur.fetchall()
        return [TestCase(
            id=r["id"], name=r["name"], method=r["method"], url=r["url"],
            headers=eval(r["headers"]) if r["headers"] else {},
            body=eval(r["body"]) if r["body"] else None,
            expected_status=r["expected_status"],
            expected_field=r["expected_field"],
            expected_value=r["expected_value"]
        ) for r in rows]

    def save_result(self, result):
        self.conn.execute("""
            INSERT INTO test_results(case_id, case_name, passed, status_code, response_time, error_msg, timestamp)
            VALUES (?,?,?,?,?,?,?)
        """, (result.case_id, result.case_name, result.passed, result.status_code,
              result.response_time, result.error_msg, result.timestamp))
        self.conn.commit()

    def close(self):
        self.conn.close()

