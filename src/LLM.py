import boto3
import os
import json

from src.variablesGlobales import varGlobals
from src.boto3 import bedrock_client


def youWant(ask):
    try:
        response = bedrock_client.fun_invoke_model(prompt=ask)
        
        response_body = response['body'].read().decode('utf-8')
        return response_body
    
    except Exception as e:
        return json.dumps({"error": "AWS fail", "type": str(e)})
