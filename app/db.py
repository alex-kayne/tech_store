from pathlib import Path
from sqlite3 import Row
from typing import Iterable

import aiosqlite

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "app.db"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"
VIEWS_PATH = BASE_DIR / "sql" / "views.sql"


async def run_sql_file(conn: aiosqlite.Connection, path: Path) -> None:
    sql = path.read_text(encoding="utf-8")
    await conn.executescript(sql)


async def init_db() -> None:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        await run_sql_file(db, SCHEMA_PATH)
        await run_sql_file(db, VIEWS_PATH)
        await db.commit()


async def returning_insert(raw_sql_template: str, values: tuple) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        async with db.execute(raw_sql_template, values) as cursor:
            new_id = await cursor.fetchone()
            await db.commit()
            return new_id[0]


async def insert(raw_sql_template: str, values: tuple) -> None:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        await db.execute(raw_sql_template, values)
        await db.commit()


async def select(raw_sql_template: str) -> Iterable[Row]:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        async with db.execute(raw_sql_template) as cursor:
            return await cursor.fetchall()

async def select_one_row(raw_sql_template: str) -> Row | None:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        async with db.execute(raw_sql_template) as cursor:
            return await cursor.fetchone()
