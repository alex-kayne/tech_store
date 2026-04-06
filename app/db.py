from pathlib import Path

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
