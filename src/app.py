#10.230.16.229
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

from Model.RolesUsuarios import RolesUsuarios, RolesSchema
from Model.Libros import Libros, LibrosSchema
from Model.Proveedores  import Proveedores, ProveedoresSchema

rolesusuario_schema = RolesSchema()
rolesusuarios_schema = RolesSchema(many=True)

#Datos de la tabla libros listo

libro_schema = LibrosSchema()
libros_Schema = LibrosSchema(many=True)

#Datos de la tabla Proveedores listo
Proveedor_schema = ProveedoresSchema()
Proveedores_Schema = ProveedoresSchema(many=True)

@app.route('/rusuarios', methods=['GET'])
def rusuario():    
    returnall = RolesUsuarios.query.all()
   
    result_rolesusuaiors = rolesusuarios_schema.dump(returnall)
    #print(result_rolesusuaiors)
    return jsonify(result_rolesusuaiors)

#metodos para Proveedores inicio
@app.route('/Proveedores', methods=['GET'])
def Proveedores():    
    returnall = Proveedores.query.all()
   
    resultado_Proveedores = Proveedores_Schema.dump(returnall)
    return jsonify(resultado_Proveedores)
#metodos para Proveedores final 

@app.route('/libros', methods=['GET'])
def libros():    
    returnall = Libros.query.all()
   
    resultado_libros = libros_Schema.dump(returnall)
    return jsonify(resultado_libros)
   
@app.route('/saveroles', methods=['POST'] )
def guardar_roles():
    roles = request.json['roles']
    print(roles)
    new_rol = RolesUsuarios(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/rusuarios')

@app.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = RolesUsuarios.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(rolesusuario_schema.dump(rol)) 

@app.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']
    id = request.json['id']
    rol = request.json['roles']
    rusuario = RolesUsuarios.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/rusuarios')

@app.route("/")
def index():
    return "Hola Mundo!! Dulfran   xD"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')