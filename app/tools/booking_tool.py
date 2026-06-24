from langchain.tools import tool

@tool
def book_trip(selection:dict):
    return {'booking_id':'BK12345','status':'confirmed','selection':selection}
