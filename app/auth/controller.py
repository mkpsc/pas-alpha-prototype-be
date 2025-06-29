from app.auth.schemas import LoginRequest, LoginResponse, UserInfoOut
from app.auth import db
import uuid


async def login(login_request: LoginRequest) -> LoginResponse:
    if login_request.username and login_request.password:
        access_token = f"mock_token_{uuid.uuid4()}"
        return LoginResponse(access_token=access_token, expires_in=3600)
    raise ValueError("Invalid credentials")


async def logout(token: str) -> dict:
    token_data = {
        "id": str(uuid.uuid4()),
        "token": token,
    }
    await db.insert_invalidated_token(token_data)
    return {"message": "Successfully logged out"}


async def get_current_user() -> UserInfoOut:
    return UserInfoOut(
        sub="mock_user_123",
        name="John Doe",
        email="john.doe@nhs.net",
        roles=["clinician", "admin"],
        provider_ids=["provider_1", "provider_2"],
    )
