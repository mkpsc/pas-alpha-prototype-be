from app.fields import BaseCamelModel


class LoginRequest(BaseCamelModel):
    username: str
    password: str


class LoginResponse(BaseCamelModel):
    access_token: str
    token_type: str = "Bearer"
    expires_in: int


class RefreshRequest(BaseCamelModel):
    refresh_token: str


class LogoutRequest(BaseCamelModel):
    refresh_token: str


class UserInfoOut(BaseCamelModel):
    sub: str
    name: str
    email: str
    roles: list[str]
    provider_ids: list[str]
