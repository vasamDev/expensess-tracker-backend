from fastapi import FastAPI
from routers.users import router as user_router
from routers.authentication import router as auth_router
from routers.expenses import router as expenses_router
app = FastAPI()


@app.get("/")
def home_page():
    return {"msg" : "welcome to the home page"}

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(expenses_router)
