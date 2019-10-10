from uuid import UUID
from decimal import Decimal
from typing import TypeVar, Union
from datetime import date, time, datetime, timedelta
from dataclasses import MISSING, Field as _Field
from ipaddress import IPv4Network, IPv6Network, IPv4Address, IPv6Address

from asyncpg import (
    BitString, Box, Circle, Line, LineSegment, Path, Point, Polygon)

T = TypeVar('T')  # Just a generic type variable

'''
TODO:
anyarray | list
anyenum  | str
anyrange | asyncpg.Range
record   | asyncpg.Record, tuple, Mapping
name     | str
tid      | tuple
=========================================
tsquery
tsvector
txid_snapshot
pg_lsn
'''


class Field(_Field):
    '''A custom field definition.'''

    py_type: T = str
    pg_type: str = 'TEXT'

    def __init__(
            self, default=MISSING, default_factory=MISSING, init=True,
            repr=True, hash=None, compare=True):
        # init=True because of the warning:
        # It is expected that init=False fields will be rarely and judiciously used  # noqa
        # https://docs.python.org/3/library/dataclasses.html#dataclasses.replace  # noqa

        # It is an error to specify both default and default_factory.
        # https://github.com/python/cpython/blob/2d88e63bfcf7bccba925ab80b3f47ccf8b7aefa8/Lib/dataclasses.py#L331  # noqa
        if default is not MISSING and default_factory is not MISSING:
            raise ValueError('cannot specify both default and default_factory')
        if default is MISSING and default_factory is MISSING:
            default = self.py_type()
        metadata = {'py_type': self.py_type, 'pg_type': self.pg_type}
        super(Field, self).__init__(
            default, default_factory, init, repr, hash, compare, metadata)

    @property
    def sql_def(self) -> str:
        '''Get an SQL definition of a Field.'''
        return f'"{self.name}" {self.pg_type}'


class TextField(Field):
    pass


class CharField(TextField):
    pg_type: str = 'CHAR'


class XMLField(TextField):
    pg_type: str = 'XML'


class UUIDField(Field):
    py_type: T = UUID
    pg_type: str = 'UUID'


class VarCharField(CharField):
    # varchar  # [ (n) ]
    pg_type: str = 'VARCHAR'


class SmallIntField(Field):
    py_type: T = int
    pg_type: str = 'SMALLINT'


class IntField(SmallIntField):
    py_type: T = int
    pg_type: str = 'INT'


class BigIntField(IntField):
    pg_type: str = 'BIGINT'


class SmallSerial(IntField):
    pg_type: str = 'SMALLSERIAL'


class SerialField(SmallSerial):
    pg_type: str = 'SERIAL'


class BigSerial(SerialField):
    pg_type: str = 'BIGSERIAL'


class BitField(Field):
    # bit  # [ (n) ]
    py_type: T = BitString
    pg_type: str = 'BIT'


class VarBitField(BitField):
    # varbit  # [ (n) ]
    pg_type: str = 'VARBIT'


class BoolField(Field):
    py_type: T = bool
    pg_type: str = 'BOOL'


class BooleanField(BoolField):
    pg_type: str = 'BOOLEAN'


class BoxField(Field):
    py_type: T = Box
    pg_type: str = 'BOX'


class ByteaField(Field):
    py_type: T = bytes
    pg_type: str = 'BYTEA'


class CIDRField(Field):
    py_type: T = Union[IPv4Network, IPv6Network]
    pg_type: str = 'CIDR'


class CircleField(Field):
    py_type: T = Circle
    pg_type: str = 'CIRCLE'


class DateField(Field):
    py_type: T = date
    pg_type: str = 'DATE'


class RealField(Field):
    py_type: T = float
    pg_type: str = 'REAL'


class FloatField(RealField):
    pg_type: str = 'FLOAT'


class DoubleField(FloatField):
    pg_type: str = 'DOUBLE'


class INETField(Field):
    py_type: T = Union[IPv4Network, IPv6Network, IPv4Address, IPv6Address]
    pg_type: str = 'INET'


class IntervalField(Field):
    # interval  # [ fields ] [ (p) ]
    py_type: T = timedelta
    pg_type: str = 'INTERVAL'


class JSONField(Field):
    pg_type: str = 'JSON'


class JSONBField(Field):
    pg_type: str = 'JSONB'


class LineField(Field):
    py_type: T = Line
    pg_type: str = 'LINE'


class LSegField(Field):
    py_type: T = LineSegment
    pg_type: str = 'LSEG'


class MACAddrField(Field):
    pg_type: str = 'MACADDR'


class MACAddr8Field(MACAddrField):
    pg_type: str = 'MACADDR8'


class MoneyField(Field):
    pg_type: str = 'MONEY'


class NumericField(Field):
    # numeric  # [ (p, s) ] 	decimal [ (p, s) ]
    py_type: T = Decimal
    pg_type: str = 'NUMERIC'


class DecimalField(NumericField):
    pg_type: str = 'DECIMAL'


class PathField(Field):
    py_type: T = Path
    pg_type: str = 'PATH'


class PointField(Field):
    py_type: T = Point
    pg_type: str = 'POINT'


class PolygonField(Field):
    py_type: T = Polygon
    pg_type: str = 'POLYGON'


class TimeField(Field):
    # offset-naïve datetime.time
    py_type: T = time
    pg_type: str = 'TIME'


class TimeTZField(TimeField):
    # offset-aware datetime.time
    pg_type: str = 'TIMETZ'


class TimeStampField(Field):
    # offset-naïve datetime.datetime
    py_type: T = datetime
    pg_type: str = 'TIMESTAMP'


class TimeStampTZField(TimeStampField):
    # offset-aware datetime.datetime
    pg_type: str = 'TIMESTAMPTZ'
