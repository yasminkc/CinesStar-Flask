from flask import Blueprint, render_template, jsonify, request, url_for

#from ControllerBase import ControllerBase

api_blue = Blueprint('api', __name__,template_folder='Controller', url_prefix='/')

class API:

    def __init__(self):
        pass
    def llamarApi():
        lista = {
            "precio" : "Para consultar el precio debes de acercarte a nuestra caja",
            "pago" : "Puedes pagar con efectivo, yape o tranferencia",
            "atencion" : "Atendemos de 8 am a 10 pm de L a V",
            "horario" : "Atendemos de 8 am a 10 pm de L a V",
            "compra" : "Las compras los puedes hacer por internet",
            "contacto" : "Para comunicarte con nuestros clientes por favor llamar a 9462655",
            "correo" : "Nuestro correo es cryisthian_06@hotmail.com",
            "gracias" : "Gracias a ti, espero que vuelvas pronto",
            "hola" : "Hola en que puedo ayudarte!",

        }
        return jsonify(lista)
    
    
    
    @api_blue.route("/API/", methods=['POST'])
    def chat(id_cinema = None):
        # Obtener todos los parámetros de formulario
        return API.devolverGet()
        params_form = request.form.to_dict()
        return params_form
        return jsonify(combined_params)

    def devolverGet():
        params = request.form.to_dict()
        return params

    
api = API()
