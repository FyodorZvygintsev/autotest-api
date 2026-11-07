"""Метаданные файла, локальный путь загрузки и структура ответа сервера."""
from pydantic import BaseModel, HttpUrl



class FileSchema(BaseModel):
    """Метаданные загруженного файла: ID, имя, каталог и проверяемый URL."""

    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreateFileRequestSchema(BaseModel):
    """Имя, каталог и локальный путь upload_file; путь нужен клиенту для чтения файла."""

    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """Ответ загрузки с вложенной моделью file; ID доступен через result.file.id."""

    file: FileSchema