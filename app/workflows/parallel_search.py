import asyncio
from app.tools.weather_tool import get_weather
from app.tools.flight_tool import search_flights
from app.tools.hotel_tool import search_hotels

async def run_parallel(destination:str):
    return await asyncio.gather(
        asyncio.to_thread(get_weather.invoke,destination),
        asyncio.to_thread(search_flights.invoke,{'source':'Delhi','destination':destination,'date':'next-week'}),
        asyncio.to_thread(search_hotels.invoke,destination)
    )
