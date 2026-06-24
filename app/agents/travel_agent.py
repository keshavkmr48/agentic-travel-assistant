from app.workflows.parallel_search import run_parallel
from app.workflows.itinerary_builder import build_itinerary
from app.workflows.approval_node import request_approval
from app.tools.booking_tool import book_trip

class TravelAgent:

    async def plan_trip(self,destination:str):
        weather, flights, hotels = await run_parallel(destination)

        itinerary = build_itinerary(weather,flights,hotels)

        approved = request_approval(itinerary)

        if not approved:
            return {'status':'cancelled'}

        booking = book_trip.invoke({'destination':destination})

        return {
            'status':'success',
            'itinerary':itinerary,
            'booking':booking
        }
