from fastapi import FastAPI
from pydantic import BaseModel
from src.agent.agent import answer_question

app = FastAPI()

@app.get("/")
def home():
    return "Hello World"

@app.get("/customers/{customer_id}")
def customer(customer_id : int):
    return customer_id

@app.get("/customers")
def customers(name):
    return name

class ChatRequest(BaseModel):
    session_id : str
    question : str

class Answerequest(BaseModel):
    answer : str
    session_id : str

@app.post("/chat", response_model=Answerequest)
def chat(request : ChatRequest):
    answer = answer_question(request.question, request.session_id)
    return Answerequest(
        answer = answer,
        session_id = request.session_id
    )

