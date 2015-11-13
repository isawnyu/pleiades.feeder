# Copyright 2015 New York University.
# Python 3 code written by and for the Institute for the Study of the
# Ancient World: http://isaw.nyu.edu

"""Create and manipulate feeds of Pleiades content."""


class Feeder():
    """Base class for Pleiades feed creators and manipulators."""

    def __init__(self, src: str):
        if not isinstance(src, str):
            raise TypeError(
                (
                    '"src" argument to Feeder.init() was of type "{0}"; '
                    'a Python3 Unicode "str" was expected.'.format(
                        type(src))
                )
            )
        self.src = src
