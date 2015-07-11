# -*- coding: utf-8 -*-

# Python 3
import six
import sys
if sys.version > '3':
    long = int
    unicode = str

import datetime
import time
#import dateutil.parser
from numbers import Number

class Property(object):
    def __str__(self):
        return str(self.__dict__)

    def __init__(self, default=None, name=None, nullable=True, \
        fget=None, fset=None, ):
        self.fget = fget
        self.fset = fset
        self.name = name
        self.default = default
        self.nullable = nullable


    def validate(self, key, value):
        self._check_null(key, value)
        self._check_datatype(key, value)

    def _check_null(self,key,value):
        # TODO: should this be checking that the value is True to catch empties?
        if self.nullable is False and value is None:
            raise ValueError

    def _check_datatype(self, key, value):
        if value is not None and isinstance(value, self.python_type) is False:
            raise TypeError

    def convert_to_db(self, key, value):
        value = self.to_db(value)
        return value

    def convert_to_python(self, key, value):
        try:
            value = self.to_python(value)
        except Exception as e:
            value = None
        return value

    # def to_db(self, value):
    #     return value

    # def to_python(self, value):
    #     return value

class String(Property): 
    #: Python type
    python_type = str

    def to_db(self, value):
        return value

    def to_python(self, value):
        return value

class Integer(Property):
    #: Python type
    python_type = int

    def to_db(self, value):
        return value

    def to_python(self, value):
        return value

class Long(Property):
    #: Python type
    python_type = long

    def to_db(self, value):
        return value

    def to_python(self, value):
        return value

class Float(Property):
    #: Python type
    python_type = float
    
    def to_db(self, value):
        return value

    def to_python(self, value):
        return value          

class Bool(Property):
    #: Python type
    python_type = bool
    
    def to_db(self, value):
        return value

    def to_python(self, value):
        return value

class Null(Property):
    #: Python type
    python_type = None
    
    pass

class List(Property):
    #: Python type
    python_type = list
    
    pass

class Dictionary(Property):
    #: Python type
    python_type = dict
    
    pass

class Document(Property):
    #: Python type
    python_type = dict
    
    pass


class DateTime(Property):

    python_type = datetime.datetime

    def to_db(self, value):
        return time.mktime(value.timetuple())

    def to_python(self, value):
        return datetime.datetime.fromtimestamp(value)

    def is_valid(self, key, value):
        return isinstance(value, datetime.datetime)

    def _coerce(self, value):
        return value


class Date(Property):
    
    python_type = datetime.date

    def to_db(self, value):
        return time.mktime(value.timetuple())

    def to_python(self, value):
        return datetime.date.fromtimestamp(value)

    def is_valid(self, key, value):
        return isinstance(value, datetime.date)

    def _coerce(self, value):
        return value
    
