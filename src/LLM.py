import boto3
import os
import json


bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

def youWant(ask):
    modelId = "meta.llama3-8b-instruct-v1:0"
    prompt = ask
    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

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