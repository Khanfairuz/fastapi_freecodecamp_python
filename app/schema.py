
from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from  pydantic.types import conint
#creating class--->SCEMA_____________
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    #rating:Optional[int]=None

#inheritance

class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True



#inherit korbe PostBase k
class PostCreate(PostBase):
    pass


#post e use korbo
class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    #response korbe  sqlalchemy te oke ignore korte hbe
    class Config:
        orm_mode=True
#format 
class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    #owner er email dekhaite chai -->owner class return kore model.py theke
    owner:UserOut
    #jate new_post j sql alchemy ase she to orm ->she j orm ta jeno ignore kore
    class Config:
        orm_mode=True


class UserCreate(BaseModel):
    email:EmailStr
    password:str




class UserLogin(BaseModel):
    email:EmailStr
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str
   
class TokenData(BaseModel):
    id:Optional[str]=None


#hoi vote dibe naile na-->dir 0,1-->conint
class Vote(BaseModel):
    post_id:int
    dir: conint(le=1)  #less than or equal to 1

class d_Post(BaseModel):
    published :bool
    owner_id :int
    title:str
    content:str
    id:int
    created_at:datetime
    

class PostOut(BaseModel):
    post:d_Post
    votes:int
    class Config:
        orm_mode=True




    #  "Post": -?ei part ta normal Post er moto-->{
    #         "published": true,
    #         "owner_id": 20,
    #         "title": "i am again updated",
    #         "content": "hello world",
    #         "id": 4,
    #         "created_at": "2024-01-16T01:42:29.317556+06:00"
    #     },
    #     "votes": 1
