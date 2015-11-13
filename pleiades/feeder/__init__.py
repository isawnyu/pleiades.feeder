# Copyright 2015 New York University.
# Python 3 code written by and for the Institute for the Study of the
# Ancient World: http://isaw.nyu.edu

"""Create and manipulate feeds of Pleiades content."""

from rdflib import RDF
from rdflib.namespace import FOAF
from pleiades.feeder.readers import TTLReader
from pleiades.feeder.vocabs import PLEIADES, PLEIADES_URLS, VIAF


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


class AuthorFeeder(Feeder, TTLReader):
    """Read and manipulate Pleiades author feeds."""

    def __init__(self, src: str=PLEIADES_URLS['authors']['turtle']):
        Feeder.__init__(self, src)
        TTLReader.__init__(self)

    def names(self):
        """Get a list of author's names."""
        try:
            return list(self._names)
        except AttributeError:
            self._make_lists()
        return list(self._names)

    def _make_lists(self):
        """Create useful lists from the data we've read."""

        try:
            data = self.data
        except AttributeError:
            self._extract()
            data = self.data

        self._names = [v['names'][0]
                       for k, v in data.items() if len(v['names']) > 0]

    def _extract(self):
        """Extract information from the graph to a data attribute."""

        people = {}
        g = self.graph
        for person in g.subjects(RDF.type, FOAF.Person):
            uri = person.n3()[1:-1]
            d = {}
            if PLEIADES.author in uri:
                d['pa_id'] = uri[len(PLEIADES.author):]
            elif VIAF in uri:
                d['uri'] = [uri, ]
            names = [name.n3()[1:-1] for name in g.objects(person, FOAF.name)]
            if len(names) > 0:
                d['names'] = names
            people[uri] = d
        self.data = people
