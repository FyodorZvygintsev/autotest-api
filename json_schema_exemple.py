"""Минимальный пример JSON Schema: проверка типов полей и обязательного имени."""
from jsonschema import validate





schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name"]
}




data = {
    "name": "Alice",
    "age": 30
}

validate(instance=data, schema=schema)
