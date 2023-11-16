from pydantic import BaseModel

class register_body(BaseModel):
    usr_name: str
    password: str
