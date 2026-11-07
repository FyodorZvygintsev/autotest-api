"""Самостоятельные Pydantic-модели запроса создания пользователя и ответа API."""




from pydantic import BaseModel, Field,  EmailStr, HttpUrl


class UserSchema(BaseModel):
    """Проверяет поля пользователя и сопоставляет JSON-ключи имени с Python-атрибутами."""
    id : str
    email : EmailStr
    last_name : str = Field(alias="lastName")
    first_name : str = Field(alias="firstName")
    middle_name : str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Описывает данные регистрации: email, пароль и части имени."""
    email : EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """Оборачивает модель пользователя в поле user ответа создания."""
    user : UserSchema
