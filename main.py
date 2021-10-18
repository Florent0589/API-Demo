import uvicorn as uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from dependencies import users_dictionary

from internal import admin
from models import User
from routers import  users


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



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7702)