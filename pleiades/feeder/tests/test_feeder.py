# Copyright 2015 New York University.
# Python 3 code written by and for the Institute for the Study
# of the Ancient World: http://isaw.nyu.edu

"""Test the base class for Pleidades feed creators and manipulators."""

from nose.tools import *

from pleiades.feeder import Feeder


class test_feeder():

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
