from fastapi import APIRouter, HTTPException, status, Depends
from models import RequestUserRegister, RequestUserLogin, UpdateUserPsw
from database import users_collections
from utils.passwords import hashed_psw, verify_psw
from accessTokens import create_access_token
from dependencies import get_current_user
from bson import ObjectId
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/")
def get_authentication():
    return {"msg" : "welcome to authentication page"}


@router.post("/register")
def create_user(user: RequestUserRegister):
    data = user.model_dump()
    find_user = users_collections.find_one({"email" : user.email})
    if find_user:
        raise HTTPException(
            detail="User already existed try with another email",
            status_code=status.HTTP_208_ALREADY_REPORTED
        )
    data["password"] = hashed_psw(user.password)
    result = users_collections.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return data


@router.post("/login")
def user_login(user:RequestUserLogin):
    data = user.model_dump()
    find_user = users_collections.find_one({"email" : user.email})
    verify = verify_psw(user.password, find_user["password"])

    if not verify:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user credentials not matched with database"
        )
    token = create_access_token({"email" : user.email, "role" : find_user["role"], "name" : find_user["name"]})

    return{
        "token_type" : "Bearer",
        "token" : token
    }



@router.post("/update-password")
def update_password(passwords: UpdateUserPsw,current_user = Depends(get_current_user)):
    print(current_user)
    psw = passwords.model_dump()
    find_user = users_collections.find_one({"_id" : ObjectId(current_user["id"])})
    verify = verify_psw(psw["old_password"], find_user["password"])

    if not verify:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Can't be update the password"
        )
    hash_ps = hashed_psw(passwords.new_password)
    update_psw = users_collections.update_one({"_id" : ObjectId(current_user["id"])}, {"$set" : {"password" : hash_ps}})

    return "successfully updated password"