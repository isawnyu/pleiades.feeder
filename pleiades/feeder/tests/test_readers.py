# Copyright 2015 New York University.
# Python 3 code written by and for the Institute for the Study
# of the Ancient World: http://isaw.nyu.edu

"""Test feed reader classes."""

from nose.tools import *
import os
from urllib.error import HTTPError, URLError

from pleiades.feeder.readers import TTLReader

TESTDATADIR = ['pleiades', 'feeder', 'tests', 'data']


class TestTTLReader():

    def __init__(self):
        pass

    def test_create(self):
        """Test creation of the reader."""

        # try simple create
        TTLReader()

        # wrong type passed as "src"
        foo = 1
        try:
            TTLReader(foo)
        except TypeError as inst:
            assert_equals(
                inst.__str__(),
                (
                    'optional "src" argument to TTLReader.init() was of '
                    'type '
                    '"<class \'int\'>"; a Python3 Unicode "str" was '
                    'expected.')
            )

        # src stored as attribute on object
        foo = 'bar'
        r = TTLReader(foo)
        assert_equals(r.src, foo)
        del(r)

    def test_read(self):
        """Test the reader's ability to read."""

        # read a local file
        foo = os.path.join(os.getcwd(), *TESTDATADIR, 'authors.ttl')
        r = TTLReader(foo)
        assert_equals(r.read(), 670)
        assert_is_not_none(r.graph)
        del(r)

        # try to read a non-existent local file
        foo = os.path.join(os.getcwd(), *TESTDATADIR, 'bogus.ttl')
        r = TTLReader(foo)
        try:
            r.read()
        except FileNotFoundError as inst:
            assert_equals(
                inst.__str__().split(':')[0],
                '[Errno 2] No such file or directory'
            )

        # read a file on the web
        foo = 'http://atlantides.org/downloads/pleiades/rdf/place-types.ttl'
        r = TTLReader(foo)
        assert_is_not_none(r.read())
        del(r)

        # try to read a bogus file on the web
        foo = 'http://atlantides.org/bogus.ttl'
        r = TTLReader(foo)
        try:
            r.read()
        except HTTPError as inst:
            assert_equals(
                inst.__str__(),
                'HTTP Error 404: Not Found'
            )
        del(r)

        # try to read a bogus file from a bogus site on the web
        foo = 'http://nowhere.org/bogus.ttl'
        r = TTLReader(foo)
        try:
            r.read()
        except URLError as inst:
            assert_equals(
                inst.__str__(),
                (
                    '<urlopen error [Errno 8] nodename nor servname '
                    'provided, or not known>'
                )
            )
        del(r)



