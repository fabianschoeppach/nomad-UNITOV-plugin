import logging

from nomad.datamodel import EntryArchive

from nomad_unitov_plugin.parsers.parser import NewParser


def test_parse_file():
    parser = NewParser()
    archive = EntryArchive()
    parser.parse('tests/data/example.out', archive, logging.getLogger())

    assert archive.workflow2.name == 'test'

def test_parse_JV():
    pass;