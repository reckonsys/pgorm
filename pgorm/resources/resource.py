from abc import ABCMeta, abstractclassmethod
from dataclasses import dataclass, fields

from inflection import pluralize


@dataclass
class Resource(metaclass=ABCMeta):

    @abstractclassmethod
    def pg_repr(cls) -> str:
        return 'RESOURCE'

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
