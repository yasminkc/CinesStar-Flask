from flask import Flask, Blueprint, redirect, render_template, url_for, request
from Controller.Cine import cine_blue
from Controller.Pelicula import pelicula_blue
from Controller.API import api_blue


app = Flask(__name__)
app.register_blueprint(cine_blue)
app.register_blueprint(pelicula_blue)
app.register_blueprint(api_blue)

@app.route("/")
def index():
    return render_template("base/index.html")

def elminareTrabajo():
    pass


if __name__ =="__main__":
  
    app.run(debug = True)

