"""Получение пользователя через клиент: регистрация, вход и разбор ответа в модель."""

from clients.users.private_user_client import get_private_user_client
from clients.users.public_users_client import get_public_users_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.user_schema import CreateUserRequestSchema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email= fake,
    password= "string",
    last_name= "string",
    first_name= "string",
    middle_name= "string"
)

create_user_response = public_users_client.create_user(create_user_request)

print(create_user_response)
print()
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_users_client = get_private_user_client(authentication_user)

get_user_response = private_users_client.get_user(create_user_response.user.id)

print(get_user_response)
