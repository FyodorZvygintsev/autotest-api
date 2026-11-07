"""Структуры курса, параметров поиска и данных создания или изменения."""
from pydantic import BaseModel, ConfigDict, Field
from clients.files.files_schema import FileSchema
from clients.users.user_schema import UserSchema

class GetCoursesQwerySchema(BaseModel):
    """Параметры фильтрации списка курсов по идентификатору пользователя."""

    userid: str


class CourseSchema(BaseModel):
    """Данные курса с вложенными моделями файла обложки и пользователя-автора."""
    model_config = ConfigDict(populate_by_name=True)


    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseResponseSchema(BaseModel):
    """Ответ создания курса: поле course содержит CourseSchema, включая ID."""

    course: CourseSchema


class CreateCourseRequestSchema(BaseModel):
    """Данные нового курса, включая ID автора и заранее загруженной обложки."""

    title: str
    description: str
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateCourseRequestSchema(BaseModel):
    """Поля изменения курса с допустимым None; отсутствие defaults не делает их необязательными."""

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")