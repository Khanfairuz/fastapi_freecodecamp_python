from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..import model,schema
from sqlalchemy.orm import Session
from ..database  import engine,get_db
from typing import List,Optional
from . import oauth2

from  sqlalchemy import func
#eita onk useful --->url er common part ta prefix e rakhbo
#tag help kore amader http://127.0.0.1:8888/docs#/default eikhaner shob   
router=APIRouter(
    prefix="/sqlalchemy/posts",
    tags=['Posts'] 
) 
#ORM--->code
@router.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #Post model ta pass
    posts=db.query(model.Post).all()
    #posts->var e shob post k fetch kore database theke
    return {"status":posts}


#eikhane amra onk gula post pathabo ->but response_model ekta post k she schema r sathe match kore return kore
#eikahner Limit j ase-->eita user er jonno query
#user ?Limit=x likhle shei koakta post show korbe
#offset use korle limit er shoman post show but oi poriman offset er por theke
#response_model=List[schema.Post]
@router.get("/")
def get_posts(db: Session = Depends(get_db) ,current_user:int=Depends(oauth2.get_current_user),Limit:int=10 ,skip:int=0 ,search:Optional[str]=""):
    print(Limit)
    print(skip)
    #contains check kore kothao ei title ase kina string er modhe
    print(search)
    posts=db.query(model.Post).filter(model.Post.title.contains(search)).limit(Limit).offset(skip).all()
    
    #inner
    res=db.query(model.Post , func.count(model.Vote.post_id).label("votes")).join(model.Vote,model.Vote.post_id==model.Post.id , isouter=True).group_by(model.Post.id).filter(model.Post.title.contains(search)).limit(Limit).offset(skip).all()
    
    return res

#response_model holo user k ki ki information dekhabo tar schema
@router.post("/" , status_code=status.HTTP_201_CREATED , response_model=schema.Post)
def create_post(post:schema.PostCreate,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #value pass ja diye post create hbe + database e insert hbe
    #onk filed exist kore
    #post value extract from body
    #dict->
    #**post.dict(): This is a syntax in Python called "unpacking." It is used to unpack the key-value pairs from the dictionary returned by post.dict() and pass them as keyword arguments to the constructor of model.Post. The ** operator is used for unpacking dictionaries.
    print(current_user.email)
    #eikahne ami foreihn key add korsi post table e-->j log in korbe she current_user-->take oi dictionary r unpacking er sathe dite hbe
    new_post=model.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    #new_post ekta sqlmodel ->oke dict e convert korte hbe->kenona pydantic model dict niye kaaj kore
    return  new_post 

@router.get("/{id}" ) # ,response_model=schema.Post#)
def get_post_sql(id:int , db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user) ):
    #p_post=db.query(model.Post).filter(model.Post.id==id).first()
    post=db.query(model.Post , func.count(model.Vote.post_id).label("votes")).join(model.Vote,model.Vote.post_id==model.Post.id , isouter=True).group_by(model.Post.id).filter(model.Post.id==id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} no post do not exist")
    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post_sql(id:int , db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
   delete_post=db.query(model.Post).filter(model.Post.id==id)

   if delete_post.first()==None:
       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"not authorized to perform actions")
   
   if delete_post.first().owner_id!=current_user.id:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id} does not exist")
       
   delete_post.delete(synchronize_session=False)
   db.commit()
   #db.refresh()
   return Response(status_code=status.HTTP_404_NOT_FOUND)
     

@router.put("/{id}" , response_model=schema.Post)
def update_post_sql(id:int ,fetch_post:schema.PostCreate,db: Session = Depends(get_db) ,current_user:int=Depends(oauth2.get_current_user)):
    
    post=db.query(model.Post).filter(model.Post.id==id)
    #fetch kora shob gulo theke just first er tar jonno check exist kore kina
    update_post=post.first()
    if update_post==None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not found")
    #eikhetre .update ekdom firrst e ja fecth korlam tar upor kaaj kortese
    #imp case->eikhane amra hard coded value pass na kore postman theke val extract korbo->then oke dictionary te convert korbo
    #dictionary te convert korte parbo pydantic model k --->eijonno fetch_post:Post nibo , oke just .dict() e convert korte parbo,r pass kore dibo
    if update_post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"not authorized to perform actions")
    post.update(fetch_post.dict() ,synchronize_session=False)
    db.commit()
    db.refresh()
    return  post.first()










