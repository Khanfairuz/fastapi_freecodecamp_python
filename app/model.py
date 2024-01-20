#table k python er model hishbe express kora
#The dot (.) before database indicates a relative import from the current package or module
from  .database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.sql.expression import null,text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
#class name capital r age pydentic er jonno BaseMode use to extract data from body part->eikahne Base use
#database er model er jonno->table kmn hbe
class Post(Base):
  __tablename__="posts"
  id=Column(Integer,primary_key=True,nullable=False)
  title=Column(String,nullable=False)
  content=Column(String,nullable=False)
  published=Column(Boolean,server_default='True',nullable=False)
  created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
  owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE",onupdate="CASCADE")  ,nullable=False)
# tablename.pk
#USER->sql alchmey class relationship er bhitore-->return kore class
  owner=relationship("User")
#retive owner property -->figure out rltnship with user
#sql alchemy model for user 
class User(Base):
   __tablename__="users"
   id=Column(Integer,primary_key=True,nullable=False)
   email=Column(String,nullable=False,unique=True)
   password=Column(String,nullable=False)
   created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
   phone_number=Column(String)


class Vote(Base):
   __tablename__="votes"
   user_id=Column(Integer,ForeignKey("users.id" , ondelete="CASCADE") , primary_key=True)
   post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE") ,primary_key=True)


