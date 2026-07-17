from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from accessTokens import verify_access_token
from database import users_collections
oauth2_verify = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)

def get_current_user(token: str = Depends(oauth2_verify)):
    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "token not verified"
        )
    user_email = payload.get("email")
    find_user = users_collections.find_one({"email" : user_email})
    if not find_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "token not verified"
        )
    return {
        "id": str(find_user["_id"]),
        "name": find_user["name"],
        "email": find_user["email"],
        "role": find_user["role"]
    }


def get_admin_user(current_user=Depends(get_current_user)):
    role = current_user.get("role")
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You Dont have an access to see all users details"
        )

    return current_user