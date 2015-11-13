# Copyright 2015 New York University.
# Python 3 code written by and for the Institute for the Study
# of the Ancient World: http://isaw.nyu.edu

"""Test Pleidades feed creators and manipulators."""

from nose.tools import *
import os

from pleiades.feeder import Feeder, AuthorFeeder
from pleiades.feeder.tests import TESTDATAPATH


class test_feeder():
    """Test base mixin Feeder class."""

    def __init__(self):
        pass

    def test_create(self):
        """Test creation of the feeder."""

        # absence of required "src" argument
        assert_raises(TypeError, Feeder)

        # wrong type passed as "src"
        foo = 1
        try:
            f = Feeder(foo)
        except TypeError as inst:
            assert_equals(
                inst.__str__(),
                (
                    '"src" argument to Feeder.init() was of type '
                    '"<class \'int\'>"; a Python3 Unicode "str" was '
                    'expected.')
            )

        # src stored as attribute on object
        foo = 'bar'
        f = Feeder(foo)
        assert_equals(f.src, foo)


class test_author_feeder():
    """Test AuthorFeeder class."""

    def __init__(self):
        pass

    def test_create(self):
        """Test creation of the feeder."""

        # use local file instead of web
        foo = os.path.join(os.getcwd(), *TESTDATAPATH, 'authors.ttl')
        f = AuthorFeeder(foo)
        assert_equals(foo, f.src)

    def test_lists(self):
        """Test getting list versions of the authors."""

        # use local file instead of web
        foo = os.path.join(os.getcwd(), *TESTDATAPATH, 'authors.ttl')
        f = AuthorFeeder(foo)
        f.read()
        l = f.names()
        assert_equals(len(l), 334)
