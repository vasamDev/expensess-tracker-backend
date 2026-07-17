from fastapi import APIRouter, Depends
from dependencies import get_current_user, get_admin_user
from database import users_collections
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.get("/all")
def get_users(admin_user= Depends(get_admin_user)):
    users = list(users_collections.find({}))
    for user in users:
        user["_id"] = str(user["_id"])
        user.pop("password", None)

    return users