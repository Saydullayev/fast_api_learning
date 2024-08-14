from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import *
from algorithms import *
from user_api.scheme import *


router = APIRouter()


@router.post("/reg/")
async def user_reg(data: UserRegistration):
    if await User.filter(username=data.username).exists():
        return JSONResponse(status_code=409, content={"message": "username already exists"})
    if await User.filter(email=data.email).exists():
        return JSONResponse(status_code=409, content={"message": "email already exists"})
    user = await User.create(fio=data.fio, username=data.username, email=data.email, viloyat=data.viloyat, password=data.password, email_verified=False, status = 'student')
    user.save()
    token = await AuthToken.create(user=user, token=generate_token())
    token.save()
    return {"message": "user created", "data": token.token}

@router.post("/login/")
async def user_login(username: str, password: str):
    user = await User.filter(username=username, password=password).first()
    if not user.exists():
        return JSONResponse(status_code=403, content={"message": "Foydalanuvchi topilmadi"})
    token = await AuthToken.create(user=user, token=generate_token())
    token.save()
    return {"message": "session createad", "data": token.token}
