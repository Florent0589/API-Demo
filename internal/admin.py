from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_current_active_user, users_dictionary
from models import User

router = APIRouter(
    tags=["admin"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/admin/me")
async def dashboard(current_user: User.User = Depends(get_current_active_user)):
    return {'Message': 'Welcome to the FASTAPI', 'Admin': await get_current_active_user(current_user)}


@router.get("/admin/us")
async def get_all_users():
    return users_dictionary
