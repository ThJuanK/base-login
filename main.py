from dotenv import load_dotenv
from fastapi import FastAPI
import jwt
import os

from database import select
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


@app.post('/login/')
def register(body: register_body):

    try:
        payload = {
            'usr_name': body.usr_name,
            'password': body.password
        }
        print(payload)
        username = payload['usr_name']
        password = payload['password']
        print(username)

        resultados = select(f"SELECT * FROM users where user = '{username}' AND pass = '{password}' ")
        
        print(resultados)
       
        
        return {'result': resultados[0]}

    except Exception as error:
        print(f"Error: {error}")
        return {"error": error}
   
