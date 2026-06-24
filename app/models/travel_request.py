from pydantic import BaseModel, Field

class TravelRequest(BaseModel):
    source:str
    destination:str
    budget:int = Field(gt=5000)
    start_date:str
