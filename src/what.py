from src.LLM import youWant
import os
import json

def what(ask, key):
    APIKey = os.getenv("API_KEY")
    if(key != APIKey):
        return json.dumps({"error": "Key incorrecta"}), 400
    
    return json.loads(youWant(ask))
