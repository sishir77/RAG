
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

@app.get("/")
def home():
    return("welcome to the homepage of rag")

class questionRequest(BaseModel):
    question:str



@app.get("/ask")
def ask_question(request:questionRequest):
    return {"question_recieved": request.question}



