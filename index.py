from flask import Flask, Blueprint, redirect, render_template, url_for
from Controller.Cine import cine_blue
from Controller.Pelicula import pelicula_blue


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("base/index.html")




if __name__ =="__main__":
    app.register_blueprint(cine_blue)
    app.register_blueprint(pelicula_blue)
    app.run(debug = True, port= 4000)

