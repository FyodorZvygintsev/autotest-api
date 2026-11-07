"""Операции с файлами: multipart-загрузка и чтение ответа с метаданными."""
from clients.api_client import APIClient
from httpx import Response
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from typing import TypedDict
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema


class File(TypedDict):
    """Типизированный словарь метаданных файла; сам TypedDict данные во время выполнения не проверяет."""

    id: str
    filename: str
    directory: str
    url: str

class FilesClient(APIClient):
    """Работает с файлами через авторизованные запросы к /files."""

    def get_file_api(self, file_id : str) -> Response:
        """Возвращает HTTP-ответ с метаданными файла по его ID."""
        return self.get(f"/api/v1/files/{file_id}")

    def delite_file_api(self, file_id : str) -> Response:
        """Учебный черновик удаления: обращение к self.delite требует исправления имени метода."""
        return self.delite(f"/api/v1/files/{file_id}")


    def create_file_api(self, request : CreateFileRequestSchema) -> Response:
        """Загружает локальный файл как multipart, отдельно передавая filename и directory."""
        return self.post(
            "/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={"upload_file"}),
            files = {"upload_file": open(request.upload_file, "rb")}
        )

    def create_file(self, request : CreateFileRequestSchema) -> CreateFileResponseSchema:
        """Загружает файл и возвращает модель ответа с данными в поле file."""
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)



def get_file_client(user: AuthenticationUserSchema) -> FilesClient:
    """Выполняет вход пользователя и создаёт клиент загрузки и получения файлов."""
    return FilesClient(client=get_private_http_client(user))
