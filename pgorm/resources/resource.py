from dataclasses import dataclass, fields
from abc import ABCMeta, abstractstaticmethod

from inflection import pluralize
from pgorm.resources.constants import RESOURCE


@dataclass
class Resource(metaclass=ABCMeta):

    @abstractstaticmethod
    def pg_repr() -> str:
        return RESOURCE

    @classmethod
    def name(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    def name_plural(cls) -> str:
        return pluralize(cls.name())

    @classmethod
    def sql_fields(cls) -> str:
        return ', '.join([f.sql_def for f in fields(cls)])

    class Meta:
        pass
