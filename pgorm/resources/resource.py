from dataclasses import dataclass, fields
from abc import ABCMeta, abstractstaticmethod

from inflection import pluralize
from pgorm.resources.constants import RESOURCE


@dataclass
class Resource(metaclass=ABCMeta):

    @abstractstaticmethod
    def _pg_repr() -> str:
        return RESOURCE

    @classmethod
    def _name(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    def _name_plural(cls) -> str:
        return pluralize(cls._name())

    @classmethod
    def _sql_fields(cls) -> str:
        return ', '.join([f.sql_def for f in fields(cls)])

    @classmethod
    def _sql_create(cls) -> str:
        return f'CREATE {cls._pg_repr()} "{cls._name()}" ({cls._sql_fields()});'  # noqa

    class Meta:
        pass
