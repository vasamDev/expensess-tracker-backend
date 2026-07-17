from jose import jwt, JWTError
from fastapi import FastAPI , HTTPException
from datetime import datetime
from datetime import timezone
from datetime import timedelta



SECRET_KEY = 'SECRET_KEY'

ALGORITHEM = "HS256"


def create_access_token(data:dict):
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=1)
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHEM)
    return token


def verify_access_token(token:str):
    try:
        result = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHEM])
        return result
    except JWTError:
       raise HTTPException(
            status_code=401,
            detail="something went wrong"
        )