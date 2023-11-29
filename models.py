from pydantic import BaseModel

class register_body(BaseModel):
    usr_name: str
    password: str

class crear_body(BaseModel):
    usr_name: str
    password: str

class ingresar_body(BaseModel):
    usr_name: str
    password: str

class borrar_body(BaseModel):
    usr_name: str
    password: str

class actualizar_body(BaseModel):
    usr_name: str
    password: str