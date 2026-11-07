"""Модели пользователей с проверкой email и aliases полей имени для JSON API."""
from pydantic import BaseModel, Field, ConfigDict, EmailStr


class UserSchema(BaseModel):
    """Данные пользователя из ответа: ID, проверяемый email и поля имени с JSON-aliases."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Данные регистрации с паролем; принимает Python-имена полей и aliases API."""

    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """Ответ регистрации: поле user содержит модель созданного пользователя."""

    user: UserSchema


class UpdateUserRequestSchema(BaseModel):

    """Поля изменения пользователя; None допустим, но без defaults поля остаются обязательными."""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")


class GetUserResponseSchema(BaseModel):
    """Ответ получения пользователя: вложенная модель user определяет ожидаемую структуру."""

    user: UserSchema
