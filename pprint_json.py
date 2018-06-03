import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        parsed = json.load(file)
    return parsed


def pretty_print_json(input_json):
    print(json.dumps(input_json, indent=5, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    input_json = load_data("example.json")
    pretty_print_json(input_json)
