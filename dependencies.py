from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models import User
from models.User import UserInDB

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users_dictionary = {
    'Ayanda': {
        "username": 'Ayanda',
        "full_name": "Default User",
        "email": "",
        "hashed_password": '123456',
        "disabled": False,
    },
}


def fake_decode_token(token):
    user = get_user(users_dictionary, token)
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: User.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

