from langchain.tools import tool

@tool
def send_email(email:str,itinerary:str):
    return {'status':'sent','email':email}
