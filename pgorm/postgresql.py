from dataclasses import dataclass, is_dataclass

from asyncpg.connection import Connection

# Implement all commands from:
# https://www.postgresql.org/docs/current/sql-commands.html


@dataclass
class PostgreSQL:
    """A PostgreSQL DB wrapper"""
    connection: Connection

    async def create_extension(
            self, extention_name: str, if_not_exists: bool = True):
        condition = 'IF NOT EXISTS' if if_not_exists else ''
        stmt = f'CREATE EXTENSION {condition} "{extention_name}";'
        return await self.connection.fetchrow(stmt)

    async def create_extension_uuid_ossp(self):
        return await self.create_extension('uuid-ossp')

    def register_model(self, model):
        # This is where we register our model
        # Create helper functions
        pass

    def register_models(self, models):
        return [self.register_model(model) for model in models]

    async def create_table(self, model) -> str:
        if not is_dataclass(model):
            raise TypeError('Dataclass is required')
        return await self.connection.execute(model.sql_create())
