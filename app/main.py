
from fastapi import FastAPI
from pydantic import BaseModel
from retrieval import similarity_search


app= FastAPI()

@app.get("/")
def home():
    return("welcome to the homepage of rag")

class questionRequest(BaseModel):
    question:str


@app.post("/ask")
def ask_question(request:questionRequest):
    result = similarity_search(request.question)
    return {"question_recieved": request.question,
            "result":result }



