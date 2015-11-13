# Copyright 2015 New York University.
# Python 3 code written by and for the Institute for the Study of the
# Ancient World: http://isaw.nyu.edu

from rdflib.namespace import Namespace

PLEIADES = Namespace('http://pleiades.stoa.org/')

PD = 'http://atlantides.org/downloads/pleiades/'

PLEIADES_URLS = {
	'authors': {
		'turtle': PD + 'rdf/authors.ttl'
	},
	'place-types': {
		'turtle': PD + 'rdf/place-types.ttl'
	}
}
VIAF = Namespace('http://viaf.org/viaf/')
