from flask import Blueprint, request, jsonify, json
from common.Toke import *

routes_user = Blueprint("routes_user", __name__)

@routes_user.route("/")
def index():
    return "index"

@routes_user.route('/obtenerToken', methods=['GET'])
def obtenertoken():
    #var_request = json.loads(event["body"])   
    datatoken = generar_token("William", 123)
    var_Token = datatoken["token"]
    response = {"statusCode": 200, "body": json.dumps(var_Token)}    
    return response

@routes_user.route('/verificartoken', methods=['GET'])
def verificartoken():
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    print("token =>", token)
      # Call the function to validate token
    vf = verificar_token(token)
    print("vf =>", vf)
    return vf
