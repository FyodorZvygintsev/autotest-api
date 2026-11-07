"""Операции аутентификации: HTTP-ответы и удобный вход с Pydantic-моделью токенов."""
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.authentication.authentication_schema import LoginResponseSchema, RefreshRequestSchema, LoginRequestSchema



class AuthenticationClient(APIClient):
    """Обращается к эндпоинтам входа и обновления токенов."""

    def login_api(self, request: LoginRequestSchema) -> Response:
        """Отправляет email и пароль на /authentication/login и возвращает Response."""
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """Отправляет refresh-токен серверу и возвращает ответ с новой парой токенов."""
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        """Вызывает login_api один раз и разбирает JSON-ответ в LoginResponseSchema."""
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """Создаёт клиент аутентификации с публичными HTTP-настройками; вход ещё не выполняет."""
    return AuthenticationClient(client=get_public_http_client())
