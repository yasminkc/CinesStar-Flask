from Models.peliculaModels import peliculaModels as PeliculaModel

#from ControllerBase import ControllerBase

from flask import Blueprint, render_template, jsonify


pelicula_blue = Blueprint('pelicula', __name__, url_prefix='/pelicula')

pelicula_model = PeliculaModel()


        
@pelicula_blue.route("/pelicula/<int:id_film>")
def pelicula(id_film):
    films = pelicula_model.view_pelicula(1)
    return render_template("pelicula.html",films = films)

@pelicula_blue.route("/peliculas")
def peliculas():
    films = pelicula_model.get_peliculas(1)
    return render_template("peliculas.html", films = films)
