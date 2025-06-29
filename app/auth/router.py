from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth import controller
from app.auth.schemas import (
    LoginRequest,
    LoginResponse,
    RefreshRequest,
    UserInfoOut,
)


router = APIRouter(prefix="/auth", tags=["authentication"])
security = HTTPBearer()


@router.post("/login", response_model=LoginResponse)
async def login(login_request: LoginRequest):
    try:
        return await controller.login(login_request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/refresh")
async def post_refresh(refresh_request: RefreshRequest) -> LoginResponse:
    try:
        return controller.refresh(refresh_request)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/logout")
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        return await controller.logout(credentials.credentials)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/me")
async def get_current_user() -> UserInfoOut:
    return controller.get_current_user()
