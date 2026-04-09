import datetime
from collections.abc import Iterable
from pathlib import Path

import aiosqlite
from aiosqlite import Row, Connection
from loguru import logger
from mypyc.ir.ops import Sequence

from schemas.orders.api import CreateOrder, ProductQuantity

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


async def returning_insert(raw_sql_template: str, values: Sequence[object]) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        async with db.execute(raw_sql_template, values) as cursor:
            new_id = await cursor.fetchone()
            await db.commit()
            return new_id[0]


async def insert(raw_sql_template: str, values: Sequence[object]) -> None:
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


async def _product_stock_updating(db: Connection, product_quantity_list: Iterable[ProductQuantity]) -> None:
    for product_quantity in product_quantity_list:
        product_id = product_quantity.product_id
        quantity = product_quantity.quantity

        cursor = await db.execute(
            f"""
            UPDATE products
            SET quantity = quantity - {quantity}
            WHERE id = {product_id}
              AND quantity >= {quantity}
            """
        )

        if cursor.rowcount == 0:
            raise ValueError(f"Not enough stock for product {product_id}")


async def _create_order_product_links(db: Connection, new_order_id: int, product_quantity_list: Iterable[ProductQuantity]):
    payload_data = {(new_order_id, product_quantity.product_id, product_quantity.quantity) for product_quantity in product_quantity_list}

    await db.executemany("INSERT INTO orders_products (order_id, product_id, quantity) VALUES (?, ?, ?)", payload_data)


async def create_order(order_data: CreateOrder) -> int | None:
    now = datetime.datetime.now()
    sql_create_order = f"INSERT INTO orders (dt_created, client_id) VALUES (?, ?) RETURNING id"

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        await db.execute("BEGIN IMMEDIATE")
        try:
            await _product_stock_updating(db, order_data.products)
            cursor = await db.execute(
                sql_create_order,
                (now, order_data.client_id),
            )
            new_order_id = (await cursor.fetchone())[0]
            await _create_order_product_links(db, new_order_id, order_data.products)
            await db.commit()
            return new_order_id

        except Exception as e:
            logger.error(e)
            logger.error(f"Failed to create order")
            await db.rollback()
            return None
