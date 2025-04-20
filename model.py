from transformers import AutoTokenizer, AutoModel
import torch

# Load DistilBERT model and tokenizer
model_name = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function for getting token embeddings from the model
def get_embeddings(prompt):
    # Tokenize input text and move to the model's device
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    # Get model outputs
    with torch.no_grad():  # No need to compute gradients
        outputs = model(**inputs)
        
    # Extract last hidden state (embedding)
    embeddings = outputs.last_hidden_state
    return embeddings

# Example usage
prompt = "This is a sample sentence."
embeddings = get_embeddings(prompt)
print(embeddings)

