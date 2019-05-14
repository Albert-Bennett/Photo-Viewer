import json

def open_json_file(filepath):
    with open(filepath) as f:
        return json.load(f)
    return {}
