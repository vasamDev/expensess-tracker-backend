from fastapi import APIRouter, Depends, HTTPException, status
from models import RequestExpeses
from database import expenses_collections
from dependencies import get_current_user, get_admin_user

router = APIRouter(
    prefix="/expenses"
)

@router.get("/all")
def get_allexpenses(admin_user=Depends(get_admin_user)):
    result = list(expenses_collections.find({}))
    for each in result:
        each["_id"] = str(each["_id"])

    return result

@router.post("/add")
def create_expense(exp:RequestExpeses, current_user = Depends(get_current_user)):
    data = exp.model_dump()
    data["user_id"] = current_user["id"]
    result = expenses_collections.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return data


@router.get("/")
def get_allexpenses(current_user=Depends(get_current_user)):
    get_data = list(expenses_collections.find({"user_id" : current_user["id"]}))
    if not get_data:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Expenses Not Available"
        )
    for exp in get_data:
        exp["_id"] = str(exp["_id"])
    return get_data