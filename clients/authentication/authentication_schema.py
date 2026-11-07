"""Pydantic-контракт входа, обновления и вложенного объекта токенов."""
from pydantic import BaseModel, Field

class TokenSchema(BaseModel):
    """Пара access/refresh-токенов и их тип; aliases соответствуют ключам JSON API."""

    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class LoginResponseSchema(BaseModel):
    """Ответ входа с вложенным полем token типа TokenSchema."""

    token: TokenSchema

class LoginRequestSchema(BaseModel):
    """Email и пароль, отправляемые в запросе входа."""

    email: str
    password: str


class RefreshRequestSchema(BaseModel):
    """Тело запроса обновления токенов с ключом refreshToken."""

    refresh_token: str = Field(alias="refreshToken")