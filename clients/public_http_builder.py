"""Общие настройки HTTP-клиента для эндпоинтов без авторизации."""
from httpx import Client


def get_public_http_client() -> Client:
    """Создаёт новый httpx.Client с адресом локального API и таймаутом 100 секунд."""
    return Client(
        timeout=100,
        base_url="http://127.0.0.1:8000"
    )
