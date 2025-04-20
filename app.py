from fastapi import FastAPI
from pydantic import BaseModel
from model import get_embeddings
import torch

# Create FastAPI app
app = FastAPI()

# Request body model
class ChatInput(BaseModel):
    message: str

# API endpoint
@app.post("/chat")
async def chat(chat_input: ChatInput):
    embeddings = get_embeddings(chat_input.message)
    
    # Convert tensor to list so it's JSON serializable
    response = embeddings.tolist()
    
    return {"response": response}
