import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file:
        parsed = json.load(file)
    return parsed


def pretty_print_json(data):
    print(json.dumps(data, indent=5, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    data = load_data("example.json")
    pretty_print_json(data)
