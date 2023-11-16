from dotenv import load_dotenv
from fastapi import FastAPI
import jwt
import os

from models import register_body

load_dotenv()
app = FastAPI()
jwt_key = os.getenv('JWT_KEY')

@app.get('/')
def index():
    return {'message': 'Todo OK'}

@app.post('/register/')
def register(body: register_body):
    payload = {
        'usr_name': body.usr_name,
        'password': body.password
    }
    token = jwt.encode(payload, jwt_key)
    return {'token': token}
