from flask import Flask, redirect, render_template, url_for

from controlador_cine import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base/index.html")

@app.route("/cine/<int:id_cinema>")
def cine(id_cinema):
    cinema = Cine.view_cine(id_cinema)
    tarifa = Cine.get_cineTarifas(id_cinema)
    cinema_film = Cine.get_cinePeliculas(id_cinema)

    return render_template("cine.html", cinema = cinema,tarifa = tarifa, cinema_film = cinema_film)

@app.route("/cines")
def cines():
    cinema = Cine.get_cines()

    return render_template("cines.html", cinema = cinema)

@app.route("/pelicula/<int:id_film>")
def pelicula(id_film):
    films = Pelicula.view_pelicula(1)
    return render_template("pelicula.html",films = films)

@app.route("/peliculas")
def peliculas():
    films = Pelicula.get_peliculas(1)
    return render_template("peliculas.html", films = films)








if __name__ =="__main__":
    app.run(debug = True, port= 4000)

