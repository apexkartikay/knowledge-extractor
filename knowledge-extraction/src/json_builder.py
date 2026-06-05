import json

def build_json(text, tables):

    result = {
        "text": text,
        "tables": tables
    }

    return json.dumps(
        result,
        indent=4
    )