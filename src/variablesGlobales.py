import os

class VariablesGlobales:
    def __init__(self):
        self._api_key = os.getenv("API_KEY")
        self._bedrock = "bedrock-runtime"
        self._us_east_1 = "us-east-1"
        self._amazon_titan_text_premier_v1 = "amazon.titan-text-premier-v1:0"
        
    @property
    def api_key(self):
        return self._api_key
    
    @property
    def bedrock(self):
        return self._bedrock
    
    @property
    def us_east_1(self):
        return self._us_east_1
    
    @property
    def amazon_titan_text_premier_v1(self):
        return self._amazon_titan_text_premier_v1
    

varGlobals = VariablesGlobales()
    
