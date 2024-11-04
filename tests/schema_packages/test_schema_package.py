import os.path

from nomad.client import normalize_all, parse

import yaml;

def test_schema_package():
    test_file = os.path.join(os.path.dirname(__file__),'..', 'data', 'test.archive.yaml')

    archive_data = yaml.load(open(test_file), Loader=yaml.FullLoader)

    print(archive_data);

    obj_type = type(archive_data);

    print(obj_type);

    for key, value in dict(archive_data).items():
        print(key,value);

    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.name == 'Markus'

test_schema_package();