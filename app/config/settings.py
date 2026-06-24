from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    openai_api_key:str=os.getenv('OPENAI_API_KEY','')
    postgres_url:str=os.getenv('POSTGRES_URL','')
    redis_url:str=os.getenv('REDIS_URL','redis://localhost:6379')

settings = Settings()
