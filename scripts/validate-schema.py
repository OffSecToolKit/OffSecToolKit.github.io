#!/usr/bin/env python3
import jsonschema
import os
import sys
import yaml

def parse_yaml(path):
    with open(path) as fs:
        text = fs.read()
        return yaml.load_all(text, Loader=yaml.SafeLoader)

def build_schema():
    service_names = list(next(parse_yaml('_data/services.yml')).keys())
    item_names = list(next(parse_yaml('_data/items.yml')).keys())
    OS_names = list(next(parse_yaml('_data/OS.yml')).keys())
    phase_names = list(next(parse_yaml('_data/phases.yml')).keys())
    return {
        'type': 'object',
        'properties': {
            'description': {'type': 'string'},
            'command': {'type': 'string'},
            'items': {
                'type': 'array',
                'items': {'enum': item_names},
            },
            'services': {
                'type': 'array',
                'items': {'enum': service_names},
            },
            'OS': {
                'type': 'array',
                'items': {'enum': OS_names},
            },
            'phases': {
                'type': 'array',
                'items': {'enum': phase_names},
            },
            'references': {
                'type': 'array',
                'items': {'type': 'string'},
            }
        },
        'required': ['description', 'command', 'items', 'OS', 'phases', 'references'],
        'additionalProperties': False
    }

def validate_directory(root):
    schema = build_schema()
    root, _, files = next(os.walk(root))
    failed = False
    for name in sorted(files):
        if not name.endswith('.md'):
            continue
        path = os.path.join(root, name)
        data = parse_yaml(path)
        try:
            jsonschema.validate(next(data), schema)
        except jsonschema.exceptions.ValidationError as err:
            print('{}: {}'.format(name, err))
            failed = True
    if failed:
        sys.exit(1)

if __name__ == '__main__':
   validate_directory("_OffSecToolKit/")
