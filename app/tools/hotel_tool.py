from langchain.tools import tool

@tool
def search_hotels(city:str):
    return [{'hotel':'Taj Goa','price':8000,'city':city}]
