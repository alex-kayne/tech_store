import app.db as sqlite_db
from app.schemas.clients.api import ClientCreate


class ClientsRepository:
    async def create_client(self, data: ClientCreate) -> int | None:
        sql_text = "INSERT INTO clients (name, address) VALUES (?, ?) RETURNING id"
        return await sqlite_db.returning_insert(sql_text, (data.name, data.address,))
