import sqlite3
from pathlib import Path
from typing import Any


DB_PATH = Path(__file__).parent / "birthday.db"


def _connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    return connection


def initialize(default_wish: dict[str, Any]) -> None:
    with _connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS wishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL,
                vibe TEXT NOT NULL,
                media_name TEXT,
                media_type TEXT,
                media_bytes BLOB
            )
            """
        )
        if connection.execute("SELECT 1 FROM wishes LIMIT 1").fetchone() is None:
            connection.execute(
                """
                INSERT INTO wishes
                    (name, location, message, created_at, vibe)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    default_wish["name"],
                    default_wish["location"],
                    default_wish["message"],
                    default_wish["created_at"],
                    default_wish["vibe"],
                ),
            )


def list_wishes() -> list[dict[str, Any]]:
    with _connect() as connection:
        rows = connection.execute(
            """
            SELECT name, location, message, created_at, vibe,
                   media_name, media_type, media_bytes
            FROM wishes
            ORDER BY id DESC
            """
        ).fetchall()
    wishes = []
    for row in rows:
        media = None
        if row["media_bytes"] is not None:
            media = {
                "name": row["media_name"],
                "type": row["media_type"],
                "bytes": row["media_bytes"],
            }
        wishes.append(
            {
                "name": row["name"],
                "location": row["location"],
                "message": row["message"],
                "created_at": row["created_at"],
                "vibe": row["vibe"],
                "media": media,
            }
        )
    return wishes


def add_wish(wish: dict[str, Any]) -> None:
    media = wish.get("media") or {}
    with _connect() as connection:
        connection.execute(
            """
            INSERT INTO wishes
                (name, location, message, created_at, vibe,
                 media_name, media_type, media_bytes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                wish["name"],
                wish["location"],
                wish["message"],
                wish["created_at"],
                wish["vibe"],
                media.get("name"),
                media.get("type"),
                media.get("bytes"),
            ),
        )