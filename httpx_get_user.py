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

get_user_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

# GET-запрос для получения пользователя по его id.
get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",headers=get_user_headers)


get_user_response_data = get_user_response.json()

print("запрос с заголовком Authorization: Bearer ... вернул этого пользователя по id")
print("get user data", get_user_response_data)