"""Базовая обёртка HTTPX: общие HTTP-методы возвращают исходный Response."""
from httpx import Client, URL, Response, QueryParams
from typing import Any

from httpx._types import RequestData, RequestFiles

class APIClient:
    """Хранит настроенный httpx.Client и предоставляет общие методы отправки запросов."""
    def __init__(self, client: Client):
        """Сохраняет переданный HTTP-клиент; запросы при создании объекта не отправляются."""
        self.client = client


    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """Отправляет GET с параметрами URL и возвращает HTTP-ответ со статусом и телом."""
        return self.client.get(url, params=params)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """Отправляет POST с JSON, полями формы или файлами и возвращает Response."""
        return self.client.post(url, json=json, data=data, files=files)


    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """Передаёт JSON в PATCH-запрос для частичного изменения ресурса."""
        return self.client.patch(url, json=json)

    def delete(self, url: URL | str) -> Response:
        """Отправляет DELETE по указанному пути и возвращает исходный ответ сервера."""
        return self.client.delete(url)