import uvicorn as uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from dependencies import users_dictionary

from internal import admin
from models import User
from routers import users

app = FastAPI()

app.include_router(users.router)
app.include_router(
    admin.router,
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = users_dictionary.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User.UserInDB(**user_dict)
    hashed_password = form_data.password
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7702)
