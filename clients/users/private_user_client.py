"""Авторизованные запросы пользователей: текущий пользователь, поиск по ID и изменения."""
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

from httpx import Response
from typing import TypedDict

from clients.users.user_schema import UpdateUserRequestSchema, GetUserResponseSchema





class PrivateUsersClient(APIClient):
    """Выполняет операции пользователей через переданный авторизованный HTTP-клиент."""

    def get_user_me_api(self) -> Response:
        """Запрашивает /users/me: сервер определяет пользователя по токену клиента."""
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """Подставляет user_id в путь GET-запроса и возвращает исходный Response."""
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """Отправляет данные изменения пользователя по его ID; возвращает HTTP-ответ."""
        return self.patch(f"/api/v1/users/{user_id}", json=request)


    def delete_user_api(self, user_id: str) -> Response:
        """Удаляет пользователя по ID и возвращает ответ, тело которого может быть пустым."""
        return self.delete(f"/api/v1/users/{user_id}")




    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """Получает пользователя через get_user_api и проверяет JSON по GetUserResponseSchema."""
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_user_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """Выполняет вход по учётным данным и создаёт готовый PrivateUsersClient."""
    return PrivateUsersClient(client=get_private_http_client(user))
