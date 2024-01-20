#coonection set up
#ORM eita+model.py file
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from  app.config  import settings

#coonection sqlalchemy te pass kora hbe
SQLALCHEMY_DATABASE_URL='postgresql://postgres:79861@localhost/fastapi'
#SQLALCHEMY_DATABASE_URL=f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
#session create
SessionLocal=sessionmaker(autocommit=False,autoflush=False , bind=engine)

Base = declarative_base()

#ORM
# Dependency-->connecting to database ->Sessionlocal talks with databse
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

####raw sql
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import  time
# max_retry =5
# retry_count=0  

# while retry_count < max_retry:
#     try:
#      #host->nijer laptop ip address , database->posygre te amra fastapi create korsilam,user chilo postgres e or {select current_user;} ei query diyeo check kora jai
#      #cursor_factor 
#      #The RealDictCursor is one of the cursor factories provided by psycopg2.extras module. 
#      #When you use RealDictCursor as the cursor_factory, the resulting cursor will return rows as dictionaries where keys are column names. 
#      #Each row will be represented as a dictionary, making it convenie
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='79861', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("hello")
#         print("Database connection was successful!")
#         break  # Break out of the loop if the connection is successful
#     except Exception as error:
#         retry_count += 1
#         print(f"Connecting to database failed. Retry {retry_count}/{max_retry}")
#         print("Error:", error)
#         time.sleep(2)  # Wait before the next retry









