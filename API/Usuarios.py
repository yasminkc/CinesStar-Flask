
from pydantic import BaseModel
from typing import Dict

class Usuarios(BaseModel):
    
    nombre  :str = None
    apellido : str = None
    edad : int = None
    dni : int = None
    _lista : list = []

    def set_dni(self, dni: int):
        self.dni = dni
        
    def get_dni(self) -> int:
        return self.dni
    
    
    def agregarUsuarios(lista : dict):
        anterior = len(Usuarios._lista)
        Usuarios._lista.append(lista)
        ahora = len(Usuarios._lista)
        if(anterior < ahora):
            return {
                "type" : "success",
                "message" : "agregado correctamente"
            }
        else:
            return {
                "type" : "error",
                "message" : "No se pudo agregar"
            }
        
    def get_usuarios(dni : int = 0):
        if(dni > 0):
            return list(filter(lambda elemento: elemento.dni == dni, Usuarios._lista))
        return Usuarios._lista