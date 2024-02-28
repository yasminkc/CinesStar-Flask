from Models.ModelsBase import ModelsBase


class cineModels(ModelsBase):
    
    
    def __init__(self):
        super().__init__()
        
    def view_cine(self,id_cine):
        return self.sentencia(f"call usp_getCine({id_cine})")

    def get_cines(self):
        
        return self.sentencia("call usp_getVerCines()")

    def get_cineTarifas(self,id_cine):
        return self.sentencia(f"call usp_getCineTarifas({id_cine})")

    def get_cinePeliculas(self,id_cine):
        return self.sentencia(f"call usp_getCinePeliculas({id_cine})")
    