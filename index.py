from flask import Flask, Blueprint, redirect, render_template, url_for, request
from Controller.Cine import cine_blue
from Controller.Pelicula import pelicula_blue
<<<<<<< HEAD
from Controller.API import api_blue
=======
>>>>>>> 8b8f25980fb2aa44714e3feaed317ae046f00ab6


app = Flask(__name__)
app.register_blueprint(cine_blue)
app.register_blueprint(pelicula_blue)
<<<<<<< HEAD
app.register_blueprint(api_blue)
=======
>>>>>>> 8b8f25980fb2aa44714e3feaed317ae046f00ab6


@app.route("/")
def index():
    return render_template("base/index.html")




if __name__ =="__main__":
  
    app.run(debug = True, port= 4000)

