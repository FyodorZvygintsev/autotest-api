import httpx

# Данные созданного пользователя для входа.
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

# POST-запрос на авторизацию пользователя.
login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login",
    json=login_payload
)
login_response_data = login_response.json()


client = httpx.Client(
    base_url="http://127.0.0.1:8000",
    timeout=100,
    headers=
    {
        "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
    }
)

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()


print(get_user_me_response_data)