#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Table related utilities.'''

from dataclasses import dataclass

from pgorm.resources.constants import TABLE
from pgorm.resources.resource import Resource


@dataclass
class Table(Resource):

    @staticmethod
    def _pg_repr() -> str:
        return TABLE
