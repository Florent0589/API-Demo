from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from models import User
from dependencies import  get_current_active_user, users_dictionary

router = APIRouter(
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_dictionary.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User.UserInDB(**user_dict)
    hashed_password = form_data.password
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/me")
async def user_profile(current_user: User.User = Depends(get_current_active_user)):
    return await get_current_active_user(current_user)


@router.get("/users/items")
async def get_user_items(current_user: User.User = Depends(get_current_active_user)):
    return {'items': fake_items_db, 'Profile': await get_current_active_user(current_user)}
