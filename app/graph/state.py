from typing import TypedDict, List, Dict

class TravelState(TypedDict):
    user_query:str
    weather:Dict
    flights:List
    hotels:List
    itinerary:str
    approved:bool
