from Models.peliculaModels import peliculaModels as PeliculaModel

#from ControllerBase import ControllerBase

from flask import Blueprint, render_template, jsonify


pelicula_blue = Blueprint('pelicula_blue', __name__, url_prefix='/')

pelicula_model = PeliculaModel()


        
@pelicula_blue.route("/pelicula/<int:id_film>")
def pelicula(id_film):
    films = pelicula_model.view_pelicula(1)
    return render_template("pelicula.html",films = films)



@pelicula_blue.route("/peliculas/")
@pelicula_blue.route("/peliculas/<int:parte>")
def peliculas(parte = 1):
    films = pelicula_model.get_peliculas(parte)
    return render_template("peliculas.html", films = films)
