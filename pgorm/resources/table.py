#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Table related utilities.'''

from pgorm.resources.resource import Resource
from dataclasses import dataclass


@dataclass
class Table(Resource):

    @classmethod
    def pg_repr(cls) -> str:
        return 'TABLE'

    @classmethod
    def sql_create(cls) -> str:
        a = f'CREATE {cls.pg_repr()} "{cls.name()}" ({cls.sql_fields()});'
        print(a)
        return a
