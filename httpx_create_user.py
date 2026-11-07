"""Создание пользователя прямым POST-запросом с email из генератора Faker."""
import httpx

from tools.fakers import fake

payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}

response = httpx.post(
    "http://127.0.0.1:8000/api/v1/users",
    json=payload,
)


print(response.json())
print(response.status_code)
