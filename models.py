from pydantic import BaseModel, EmailStr, Field

class RequestUserRegister(BaseModel):
    name : str
    email : EmailStr
    password : str
    role : str
    is_activated : bool = Field(default=True)
    is_verified : bool = Field(default=False)
    profile_img : str | None = None


class RequestUserLogin(BaseModel):
    email : EmailStr
    password : str


class UpdateUserPsw(BaseModel):
    old_password : str
    new_password : str



class RequestExpeses(BaseModel):
    title: str
    description: str
    amount: int
    category: str
    expense_date: str
    payment_method: str