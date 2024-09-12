from fastapi import FastAPI
from starlette.responses import Response
import json
import base64
import random

app = FastAPI()

def generate_base64_json():
    # Generate a random amount between 0 and 10000
    amount = random.randint(0, 10000)
    
    # Data to be encoded
    data = {"schema": "0.0.1", "amount": amount}
    
    # Convert data to JSON and then encode to base64
    json_string = json.dumps(data)
    base64_encoded_string = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')
    
    return base64_encoded_string

@app.get("/")
async def root():
    headers = {"X-Payment-Claim-Surcharge": generate_base64_json()}
    return Response(content="Hello, World!", headers=headers)
