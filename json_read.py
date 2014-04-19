import json


def from_json(jsonobj):
    if '__class__' in jsonobj:
        if jsonobj['__class__'] == 'bytes':
            return bytes(jsonobj['__value__'])
    return jsonobj

with open('basic.json', encoding='utf-8') as f:
    entry = json.load(f, object_hook=from_json)
    print(entry)
