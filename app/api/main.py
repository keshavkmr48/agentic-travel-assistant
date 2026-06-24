from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.travel_agent import TravelAgent

app = FastAPI(title='Agentic Travel Assistant')
agent = TravelAgent()

class TripRequest(BaseModel):
    destination:str

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/plan-trip')
async def plan_trip(request:TripRequest):
    return await agent.plan_trip(request.destination)
