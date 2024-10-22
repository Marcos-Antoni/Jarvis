import boto3
import json
from src.variablesGlobales import varGlobals

class bedrockClient:
    _client = None

    def __init__(self):
        self._client = boto3.client(
            service_name=varGlobals.bedrock,
            region_name=varGlobals.us_east_1
        )
    
    def fun_invoke_model(self, prompt):
        body = {"inputText": prompt}
        
        response = self._client.invoke_model(
            modelId=varGlobals.amazon_titan_text_premier_v1,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )
        
        return response

bedrock_client = bedrockClient()
