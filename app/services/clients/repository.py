import app.db as sqlite_db
from schemas.clients.api import ClientCreate


class ClientsRepository:
    async def create_client(self, data: ClientCreate) -> int:
        sql_text = "INSERT INTO clients (name, address) VALUES (?, ?) RETURNING id"
        new_id = await sqlite_db.returning_insert(sql_text, (data.name, data.address,))
        return new_id
