import json
from jsonschema import validate

# Definizione dello schema JSON
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["name", "age"]
}

# Oggetto JSON da validare
json_data = '''
{
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}
'''
# Parsing dell'oggetto JSON
data = json.loads(json_data)

# Validazione dell'oggetto JSON rispetto allo schema
try:
    validate(data, schema)
    print("Validazione riuscita!")
except Exception as e:
    print("Validazione fallita:", e)

