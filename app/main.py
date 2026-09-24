
from fastapi import FastAPI
from pydantic import BaseModel
from retrieval import similarity_search
from llm import generate_answer


app= FastAPI()

@app.get("/")
def home():
    return("welcome to the homepage of rag")

class questionRequest(BaseModel):
    question:str


@app.post("/ask")
def ask_question(request:questionRequest):
    results = similarity_search(request.question)

    context = "/n/n".join(
        result['document'] for result in results
    )

    answer = generate_answer(request.question, context)

    return{
        "question": request.question,
        "answer": answer
    }



