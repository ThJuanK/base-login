from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import jwt
import os
from fastapi.responses import JSONResponse

from database import select
from database import login
from models import register_body
from models import crear_body
from models import ingresar_body
from models import borrar_body
from models import actualizar_body

load_dotenv()
app = FastAPI()
origins = [
   
    "http://localhost",
    "http://localhost:4200",
]

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
def ingresar(body: ingresar_body):

    try:
        payload = {
            'usr_name': body.usr_name,
            'password': body.password
        }
        username = payload['usr_name']
        password = payload['password']
        [resultados] = login(f"SELECT * FROM users where user = '{username}' ")
        print(resultados)
        if not resultados:
            return JSONResponse(content={"msg": "Error Usuario no encontrado"}, status_code=400)
            

        stored_password = resultados['pass']
        if(password.strip() != stored_password.strip() ):
            return JSONResponse(content={"msg": "Contraseña incorrecta"}, status_code=400)
            
        
        return JSONResponse(content={"status": 'true',"msg": "Ingreso Exitoso", "data": resultados}, status_code=200)
        

    except Exception as error:
        print(f"Error: {error}")
        return JSONResponse(content={f"msg": error}, status_code=202)


@app.get('/usuariosall/')
def getUsuarios():

    try:
        
        resultados = login(f"SELECT * FROM users where idusers != 1 and estado = 1 ")
        if not resultados:
            return JSONResponse(content={"msg": "Error consultando usuarios"}, status_code=400)
                
        return JSONResponse(content={"status": 'true',"msg": "Consulta extiosa ", "data": resultados}, status_code=200)
        

    except Exception as error:
        print(f"Error: {error}")
        return JSONResponse(content={f"msg": error}, status_code=202)
       
    
@app.post('/create/')
def crear(body: crear_body):

    try:
        payload = {
            'usr_name': body.usr_name,
            'password': body.password,
            'cedula': body.cedula,
            'nombre': body.nombre,
            'correo': body.correo
        }
        username = payload['usr_name']
        password = payload['password']
        cedula = payload['cedula']
        nombre = payload['nombre']
        correo = payload['correo']
        pol=f"INSERT INTO users (user, pass, cedula, nombre, correo ) VALUES ('{username}', '{password}', '{cedula}', '{nombre}', '{correo}')"
        resultados = select(pol)   
        print(resultados)
        return {'result': resultados}

    except Exception as error:
        print(f"Error: {error}")
        return {"error": error}
    
@app.post('/delete/')
def borrar(body: borrar_body):

    try:
        payload = {
            'usr_name': body.usr_name,   
        }
        username = payload['usr_name']
        print(username)
        pol=f"UPDATE users SET estado = 0 WHERE user = ('{username}')"
        resultados = select(pol)
        
        
        print(resultados)
       
        
        return {'result': resultados}

    except Exception as error:
        print(f"Error: {error}")
        return {"error": error}
    
@app.post('/update/')
def actualizar(body: crear_body):

    try:
        payload = {
            'usr_name': body.usr_name,
            'password': body.password,
            'cedula': body.cedula,
            'nombre': body.nombre,
            'correo': body.correo
        }
        
        username = payload['usr_name']
        password = payload['password']
        cedula = payload['cedula']
        nombre = payload['nombre']
        correo = payload['correo']
        print(username)
        pol=f"UPDATE users SET user = ('{username}'), pass = ('{password}'), cedula = ('{cedula}') , nombre = ('{nombre}') , correo = ('{correo}') WHERE user = ('{username}')"
        resultados = select(pol)
        
        
        print(resultados)
       
        
        return {'result': resultados}

    except Exception as error:
        print(f"Error: {error}")
        return {"error": error}
   
