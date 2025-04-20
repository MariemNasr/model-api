from fastapi import FastAPI
from pydantic import BaseModel
from model import get_embeddings

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(chat_input: ChatInput):
    response = chat_with_bot(chat_input.message)
    return {"response": response}
