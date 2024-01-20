from fastapi import FastAPI

#ORM er jonno
from .import model
from .database import engine

#command to create table from model.py-->alembic use korai oke r ekhn lagbe na
#model.Base.metadata.create_all(bind=engine)
from .routers import post,user,auth, vote

#from  config import settings
from fastapi.middleware.cors import CORSMiddleware

#schema

app=FastAPI()

#CROSMIDDLeware-->web frame work
#allow_origins--<jei jei domain k allow korte chai
#allow_mthods-->to allow apecific http methods-->

#list
#origins=["https://www.google.com" ,"https://www.youtube.com"]
#to get req from other domains-->CORS
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#ORM--->code
@app.get("/")
def root():
    return {"message":"Hello world"}



























 














