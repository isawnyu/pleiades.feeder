# Copyright 2015 New York University.
# Python 3 code written by and for the Institute for the Study of the
# Ancient World: http://isaw.nyu.edu

"""Read feeds of Pleiades content."""

from rdflib import Graph


class TTLReader():
    """Read Turtle RDF."""

    def __init__(self, src=None):
        if isinstance(src, str):
            self.src = src
        elif src is not None:
            raise TypeError(
                (
                    'optional "src" argument to TTLReader.init() was of '
                    'type "{0}"; '
                    'a Python3 Unicode "str" was expected.'.format(
                        type(src))
                )
            )

    def read(self):
        g = Graph()
        g.parse(self.src, format='turtle')
        return len(g)
