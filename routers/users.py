from fastapi import APIRouter, Depends, HTTPException

from models import User
from dependencies import  get_current_active_user

router = APIRouter(
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/me")
async def user_profile(current_user: User.User = Depends(get_current_active_user)):
    return await get_current_active_user(current_user)


@router.get("/users")
async def dashboard():
    return fake_items_db
