from src.LLM import youWant
from src.variablesGlobales import varGlobals
import os
import json

def what(ask, key):
    APIKey = varGlobals.api_key
    if(key != APIKey):
        return json.dumps({"error": "Key incorrecta"}), 400
    
    return json.loads(youWant(ask))
