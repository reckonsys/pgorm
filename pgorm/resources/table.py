#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Table related utilities.'''

from dataclasses import dataclass

from pgorm.resources.constants import TABLE
from pgorm.resources.resource import Resource


@dataclass
class Table(Resource):

    @staticmethod
    def pg_repr() -> str:
        return TABLE

    @classmethod
    def sql_create(cls) -> str:
        return f'"{cls.name()}" ({cls.sql_fields()});'
