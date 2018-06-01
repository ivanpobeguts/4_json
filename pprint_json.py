import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        parsed = json.load(file)
    return parsed


def pretty_print_json(data):
    print(json.dumps(data, indent=5, sort_keys=False))


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    pretty_print_json(data)
