from bd import BD

bd = BD("cinestar")

#para llamar a nuesta funcion de una clase sin instanciar un objeto, solo basta con no poner self

#si queremos crear un objeto y llamar una funcion, es necesario colocar self en los parametros de las funciones

class Cine:
    def view_cine(id_cine):
        return bd.sentencia(f"call usp_getCine({id_cine})")

    def get_cines():
        return bd.sentencia("call usp_getVerCines()")

    def get_cineTarifas(id_cine):
        return bd.sentencia(f"call usp_getCineTarifas({id_cine})")

    def get_cinePeliculas(id_cine):
        return bd.sentencia(f"call usp_getCinePeliculas({id_cine})")
    

class Pelicula:
    
    def view_pelicula(id_pelicula):
        return bd.sentencia(f"call usp_getPelicula({id_pelicula})")

    def get_peliculas(id_pelicula):
        return bd.sentencia(f"call usp_getVerPeliculas({id_pelicula})")