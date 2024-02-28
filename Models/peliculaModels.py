from Models.ModelsBase import ModelsBase


class peliculaModels(ModelsBase):
    
    def __init__(self):
        super().__init__()
        
    def view_pelicula(self,id_pelicula):
        return self.sentencia(f"call usp_getPelicula({id_pelicula})")

    def get_peliculas(self,id_pelicula):
        return self.sentencia(f"call usp_getVerPeliculas({id_pelicula})")