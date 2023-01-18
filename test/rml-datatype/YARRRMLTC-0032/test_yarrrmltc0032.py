__author__ = "Marino Gonzalez Garcia"
__credits__ = ["Marino Gonzalez Garcia"]

__license__ = "Apache-2.0"
__maintainer__ = "David Chaves Fraga"
__email__ = "david.chaves@upm.es"


import os
from ruamel.yaml import YAML
import yarrrml_translator
from rdflib.graph import Graph
from rdflib import compare


def test_yarrrmltc0032():
    expected_mapping = Graph()
    expected_mapping.parse(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mapping.ttl'), format="ttl")

    translated_mapping = Graph()
    yaml = YAML(typ='safe', pure=True)
    mapping_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mapping.yml')
    translated_mapping.parse(data=yarrrml_translator.translate(yaml.load(open(mapping_path))), format="ttl")

    assert compare.isomorphic(expected_mapping, translated_mapping)