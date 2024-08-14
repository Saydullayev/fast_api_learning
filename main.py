from fastapi import FastAPI
import uvicorn
from tortoise import Tortoise, run_async
from models import *
from algorithms import *
from tortoise.contrib.fastapi import register_tortoise
from user_api.route import router as user_router

async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


app = FastAPI()
app.include_router(
    user_router,
    prefix="/user",
    tags=["User"],
)
register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)



if __name__ == '__main__':
    run_async(init())
    uvicorn.run("main:app", reload=True)
