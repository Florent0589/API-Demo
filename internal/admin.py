from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)


@router.get("/admin")
async def dashboard():
    return {'Message': 'Welcome to the FASTAPI'}
