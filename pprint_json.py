import json
import sys
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf8') as file:
            try:
                return json.load(file)
            except ValueError:
                return None


def pretty_print_json(parsed_json):
    print(json.dumps(parsed_json, indent=5, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        parsed_json = load_data(sys.argv[1])
        if parsed_json is not None:
            pretty_print_json(parsed_json)
        else:
            print('ERROR: Check, that file "{}" exists and it is valid json file.'.format(sys.argv[1]))
    else:
        print('Path to json file expected!')
