"""Регистрация пользователя с выбором исходного Response или Pydantic-модели ответа."""
from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.user_schema import UserSchema, CreateUserRequestSchema, CreateUserResponseSchema



class PublicUsersClient(APIClient):
    """Предоставляет регистрацию пользователя без предварительного токена."""

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """Сериализует модель запроса с aliases и возвращает HTTP-ответ создания пользователя."""
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))


    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """Создаёт пользователя и возвращает CreateUserResponseSchema с вложенным user."""
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """Оборачивает публичный HTTP-клиент в PublicUsersClient без отправки запросов."""
    return PublicUsersClient(client=get_public_http_client())
