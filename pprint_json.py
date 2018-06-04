import json
import sys
import os


def load_data(filepath):
    parsed_json = None
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf8') as file:
            try:
                parsed_json = json.load(file)
            except Exception as ex:
                print('{}: Incorrect json file (\'{}\')!'.format(type(ex).__name__, filepath))
    else:
        print('File \'{}\' does not exist!'.format(filepath))
    return parsed_json


def pretty_print_json(raw_json):
    print(json.dumps(raw_json, indent=5, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        raw_json = load_data(sys.argv[1])
        if raw_json is not None:
            pretty_print_json(raw_json)
    else:
        print('Path to json file expected!')
