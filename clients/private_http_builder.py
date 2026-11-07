"""Создание HTTP-клиента с Bearer-токеном, полученным по email и паролю."""

from httpx import Client

from clients.authentication.authentication import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from pydantic import BaseModel

class AuthenticationUserSchema(BaseModel):
    """Хранит email и пароль для входа; создание модели само по себе не авторизует."""

    email: str
    password: str

def get_private_http_client(user: AuthenticationUserSchema):
    """Выполняет вход по модели учётных данных и создаёт HTTP-клиент с Bearer-токеном."""
    authentication_client = get_authentication_client()

    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)


    return Client(
        timeout=100,
        base_url="http://127.0.0.1:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token }"},
    )
