from app.workflows.parallel_search import run_parallel

class TravelAgent:

    async def plan_trip(self,destination:str):
        weather, flights, hotels = await run_parallel(destination)
        return {
            'weather':weather,
            'flights':flights,
            'hotels':hotels
        }
