from pydantic import BaseModel 
from datetime import datetime

class TokenData(BaseModel):
    id:str=None


class UserOut(BaseModel):
    id:int
    email:str
    created_at:datetime
    class Config:
        orm_mode=True