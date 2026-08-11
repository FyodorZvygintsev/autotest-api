import httpx
from tools.fakers import  get_random_email

# Данные для создания нового пользователя.
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}


# POST-запрос на создание пользователя.
create_user_response = httpx.post(
    "http://localhost:8000/api/v1/users",
    json=create_user_payload)

# JSON-ответ сервера о созданном пользователе.
create_user_response_data = create_user_response.json()

print("пользователь создан")
print("create user data", create_user_response_data)


# Данные созданного пользователя для входа.
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

# POST-запрос на авторизацию пользователя.
login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login",
    json=login_payload
)

# JSON-ответ сервера после авторизации.
login_response_data = login_response.json()

print("выполнен логин и получен accessToken")
print("login data", login_response_data)


delete_user_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}
delete_user_response = httpx.delete(
    f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
    headers=delete_user_headers,
)

delete_user_response_data = delete_user_response.json()
print("delete user data", delete_user_response_data)