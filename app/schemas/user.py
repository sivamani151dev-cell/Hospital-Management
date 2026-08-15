from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserRespond(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes=True

class Token(BaseModel):
    token_type: str
    access_token: str