from pydantic import BaseSettings

#pydantic casr in sensitive
#post url e thake eijonno str nilei hbe
#In the context of the pydantic library and the BaseSettings class, the .env file is used to set values for the attributes of the Settings class. The class Config within BaseSettings is used to configure how the settings are loaded from the environment variables or from an .env file
class Settings(BaseSettings):
    datbase_hostname:str
    datbase_port:str
    datbase_password:str
    datbase_name:str
    datbase_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    class Config:
        env_file=".env"




from pydantic import ValidationError

try:
    settings = Settings()
except ValidationError as e:
    print(e.json())

