import json
import sys
import os


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf8') as file:
            try:
                parsed_json = json.load(file)
            except:
                print('Incorrect json file: \'{}\'!'.format(filepath))
                sys.exit()
    else:
        print('File \'{}\' does not exist!'.format(filepath))
        sys.exit()
    return parsed_json


def pretty_print_json(raw_json):
    print(json.dumps(raw_json, indent=5, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        raw_json = load_data(sys.argv[1])
        pretty_print_json(raw_json)
    else:
        print('Path to json file expected!')
