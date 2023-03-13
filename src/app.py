#10.230.16.229
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

from Model.RolesUsuarios import RolesUsuarios, RolesSchema
from Model.Libros import Libros, LibrosSchema

rolesusuario_schema = RolesSchema()
rolesusuarios_schema = RolesSchema(many=True)

@app.route('/rusuarios', methods=['GET'])
def rusuario():    
    returnall = RolesUsuarios.query.all()
   
    result_rolesusuaiors = rolesusuarios_schema.dump(returnall)
    #print(result_rolesusuaiors)
    return jsonify(result_rolesusuaiors)

#Datos de la tabla libros listo

libros_schema = LibrosSchema()
Libros_Schema = LibrosSchema(many=True)

@app.route('/rusuarios', methods=['GET'])
def rusuario():    
    returnall = Libros.query.all()
   
    resultado_libros = LibrosSchema.dump(returnall)
    return jsonify(resultado_libros)
   
@app.route('/saveroles', methods=['POST'] )
def guardar_roles():
    roles = request['roles']
    new_rol = RolesUsuarios(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/rusuarios')


@app.route("/")
def index():
    return "Hola Mundo!! Dulfran   xD"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')