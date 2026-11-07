"""Основы Pydantic: вложенные модели, aliases и создание объектов из словаря и JSON.

Пример ожидаемого JSON курса:
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
"""


import uuid
from fileinput import filename

from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    """Учебная модель метаданных файла, используемая как вложенное поле курса."""
    id: str
    filename: str
    directory: str
    url: str


    def get_username(self):
        """Черновик вычисления имени: first_name и last_name не объявлены в этой модели файла."""
        return f"{self.first_name} {self.last_name}"

class UserSchema(BaseModel):
    """Учебная модель пользователя с явными aliases для ключей JSON."""
    id: str
    email: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CourseShema(BaseModel):
    """Объединяет вложенные модели автора и обложки, aliases и значения полей по умолчанию."""
    model_config = ConfigDict(alias_generator=to_camel, populate_default=True)

    id: str = Field(default_factory=lambda:(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=100)
    min_score: int = Field(alias="minScore", default=10)
    description: str = "Playwright course"
    preview_file : FileSchema = Field(alias="previewFile")
    estimatedTime: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseShema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile = FileSchema(
        id = "file-id",
        url = "https://example.com/",
        filename = "file.png",
        directory = "1 week",
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(

        id = "user-id",
        email = "example.com",
        lastName = "Zara",
        firstName = "Bob",
        middleName = "Alice",
    )

)


course_dict = {
    "id" : "course-id",
    "title" : "Playwright",
    "maxScore" : 100,
    "minScore" : 10,
    "description" : "Playwright",
    "previewFile" : {
        "id" : "file-id",
        "url" : "https://example.com/",
        "filename" : "file.png",
        "directory" : "1 week"
    },
    "estimatedTime" : "1 week",
    "createdByUser" : {
        "id" : "user-id",
        "email" : "example.com",
        "lastName" : "Zara",
        "firstName" : "Bob",
        "middleName" : "Alice"
    }
}



course_dict_model = CourseShema(**course_dict)




course_Json = """{
    "id" : "course-id",
    "title" : "Playwright",
    "maxScore" : 100,
    "minScore" : 10,
    "description" : "Playwright",
    "previewFile" : {
        "id" : "file-id",
        "url" : "https://example.com/",
        "filename" : "file.png",
        "directory" : "1 week"
    },
    "estimatedTime" : "1 week",
    "createdByUser" : {
        "id" : "user-id",
        "email" : "example.com",
        "lastName" : "Zara",
        "firstName" : "Bob",
        "middleName" : "Alice"
    }
}
"""

course_json_model = CourseShema.model_validate_json(course_Json)

print(course_json_model.model_damp_json(by_alias=True))
print(course_json_model.model_damp(by_alias=True))
