from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..import model,schema,utils
from sqlalchemy.orm import Session
from ..database  import engine,get_db
from .import oauth2
#..->router folder e database nai eijonno .. dite hbe
#notun jinish router 
router=APIRouter(
    prefix="/sqlalchemy/user",
    tags=['Users']  
)

#for user
#hashing
#post korar jonno log in korte hbe /token thaka must
#ei token ta k oauth2 er get_current_user function er sathe kaaj korte hbe -->eijonno amra oke path e add korsi
#what is the use of get current user?
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schema.UserOut)
def create_user( user:schema.UserCreate,db: Session = Depends(get_db)):
   #hash the password-user.passwprd
   hashed_psw=utils.hash(user.password)
   user.password=hashed_psw
   
   
   new_post=model.User(**user.dict())
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post


@router.get("/{id}" , response_model=schema.UserOut)
def get_user(id:int ,db: Session = Depends(get_db)):
     user= db.query(model.User).filter(model.User.id==id).first()
     if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id:{id} doesnt exist")
     
     return user