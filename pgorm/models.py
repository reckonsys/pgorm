#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''A model related utilities.'''

from dataclasses import dataclass, fields

from inflection import pluralize


@dataclass
class BaseModel:

    @classmethod
    def _table_name(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    def _table_name_plural(cls) -> str:
        return pluralize(cls._table_name)

    @classmethod
    def sql_create(cls) -> str:
        fields_defn = ', '.join([f.sql_def for f in fields(cls)])
        return f'CREATE TABLE "{cls._table_name()}" ({fields_defn});'

    @classmethod
    def sql_common(cls) -> str:
        fields_defn = ', '.join([f.sql_def for f in fields(cls)])

