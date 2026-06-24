from langchain.tools import tool

@tool
def search_flights(source:str,destination:str,date:str):
    return [{'airline':'Indigo','price':5500,'source':source,'destination':destination,'date':date}]
