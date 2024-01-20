from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..import schema,database,model
from .import oauth2
from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/vote",
    tags=["vote"]
)

@router.post("/" ,status_code=status.HTTP_201_CREATED)
def vote(vote:schema.Vote , db:Session=Depends(database.get_db),current_user:int =Depends(oauth2.get_current_user)):
     post=db.query(model.Post).filter(model.Post.id==vote.post_id).first()
     #post no ado exits kore kina
     if not post:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post {vote.post_id} do not exist")
     #same post e same lok vote dise naki shie ta check
     #post_id r current_user_id milate hbe
     vote_query=  db.query(model.Vote).filter(model.Vote.post_id==vote.post_id , model.Vote.user_id==current_user.id)
     found_vote=vote_query.first()
     
     if(vote.dir==1):
         #emn row exist korle ->alredy voted
         if found_vote:
              raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail=f"user {current_user} has alreday voted on the  post")
         #emn row paw jai nai-->age kaw vote dei nai
         #database e push kort hbe
         new_vote=model.Vote(post_id=vote.post_id , user_id=current_user.id)
         db.add(new_vote)
         db.commit()
         return {"message ": "successfully voted"}
     #vote remove korte chai oi post er jonno
     else:
        #vote exit na korle delete hbe na -->exception
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Vote does not exist")
        #exist kore -->vote table theke oi row baad dibo
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message" :"successfully deleted vote"}














