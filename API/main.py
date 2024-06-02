from fastapi import *

from Usuarios import Usuarios

app = FastAPI()



usuario = Usuarios

@app.get("/get_usuarios/")
def get_usuarios():
    return usuario.get_usuarios()


@app.get("/get_usuarios/{dni}")
def get_usuarios(dni: int):
    return usuario.get_usuarios(dni)


@app.put("/set_usuarios")
def set_usuarios(usu: Usuarios):
    return usuario.agregarUsuarios(usu)
