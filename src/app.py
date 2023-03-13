#10.230.16.229
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

from Model.RolesUsuarios import RolesUsuarios, RolesSchema

rolesusuario_schema = RolesSchema()
rolesusuarios_schema = RolesSchema(many=True)

@app.route('/rusuarios', methods=['GET'])
def rusuario():    
    returnall = RolesUsuarios.query.all()
   
    result_rolesusuaiors = rolesusuarios_schema.dump(returnall)
    #print(result_rolesusuaiors)
    return jsonify(result_rolesusuaiors)
   
    
@app.route("/")
def index():
    return "Hola Mundo!! Dulfran xD"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')