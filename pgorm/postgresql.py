from inspect import isclass
from dataclasses import dataclass, fields

from asyncpg.connection import Connection
from pgorm.resources.resource import Resource

# Implement all commands from:
# https://www.postgresql.org/docs/devel/sql-commands.html


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

    async def create(self, resource: Resource) -> Resource:
        if not isclass(resource) or not issubclass(resource, Resource):
            raise TypeError(f'Should be a subclass of {Resource}')
        return await self.connection.execute(resource._sql_create())

    async def insert(self, resource: Resource) -> Resource:
        _fields = [f.name for f in fields(resource)]
        _vars = ', '.join([f'${num}' for (num, item) in enumerate(_fields, 1)])
        args = [getattr(resource, f) for f in _fields]
        _fields = ', '.join(_fields)
        stmt = f'INSERT INTO "{resource.__class__._name()}" ({_fields}) VALUES ({_vars})'  # noqa
        await self.connection.execute(stmt, *args)
        return resource
