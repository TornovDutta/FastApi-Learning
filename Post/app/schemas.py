from pydantic import BaseModel, EmailStr

class UsersBase(BaseModel):
    name: str
    email: str

class Requestedusers(UsersBase):
    password: str

class UsersResponse(UsersBase):
    id: int

    class Config:
        orm_mode = True