"""Единая точка проверки данных по JSON Schema, включая указанные в схеме форматы."""
from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict) -> None:
    """Проверяет данные по JSON Schema с проверкой форматов.

    :param instance: Разобранные JSON-данные, обычно результат Response.json().
    :param schema: Словарь правил, например результат model_json_schema().
    :raises jsonschema.exceptions.ValidationError: Если данные нарушают правила.
    :return: None при успешной проверке.
    """
    validate(
            instance=instance,
            schema=schema,
            format_checker=Draft202012Validator.FORMAT_CHECKER
        )