from fastapi import FastAPI
from pydantic import BaseModel
from model import chat_with_bot

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(chat_input: ChatInput):
    response = chat_with_bot(chat_input.message)
    return {"response": response}
