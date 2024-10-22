import boto3
import os
import json


bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

def youWant(ask):
    modelId = "amazon.titan-text-premier-v1:0"
    prompt = ask
    body = {"inputText": prompt}

    try:
        # Invoca el modelo
        response = bedrock_client.invoke_model(
            modelId=modelId,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )

        # Leer y decodificar la respuesta
        response_body = response['body'].read().decode('utf-8')
        return response_body
    except Exception as e:
        return json.dumps({"error": "AWS fail", "type": type(e).__name__})