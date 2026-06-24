from langchain.tools import tool

@tool
def get_weather(city:str)->dict:
    """Get weather for destination."""
    return {
        'city':city,
        'temperature':30,
        'condition':'Sunny'
    }
