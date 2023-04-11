from common.Toke import *
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users,UsuariosSchema

routes_user = Blueprint("routes_user", __name__)

#usuario
Usuario_Schema= UsuariosSchema()
Usuarios_Schema= UsuariosSchema(many=True)


@routes_user.route("/")
def index():
    return "index"

@app.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = Users.query.all()
   
    resultado_usuarios = Usuarios_Schema.dump(returnall)
    return jsonify(resultado_usuarios)

#crud de usuarios
@app.route('/eliminar_Users/<id>', methods=['GET'] )
def eliminar_users(id):
    full_name = Users.query.get(id)
    Email = Users.query.get(id)
    telefono = Users.query.get(id)
    especialidad = Users.query.get(id)
    jornada = Users.query.get(id)
    direccion = Users.query.get(id)
    db.session.delete(full_name,Email,telefono,especialidad,jornada,direccion)
    db.session.commit()
    return jsonify(UsuariosSchema.dump(full_name,Email,telefono,especialidad,jornada,direccion)) 

@app.route('/actualizarUsers', methods=['POST'] )
def actualizar_users():
    id = request.json['id']
    full_name = request.json['full_name']
    Email= request.json['Email']
    telefono= request.json['telefono']
    especialidad= request.json['especialidad']
    jornada= request.json['jornada']
    direccion= request.json['direccion']
    users= Users.query.get(id)
    users.full_name = full_name
    users.Email= Email
    users.telefono = telefono
    users.especialidad= especialidad
    users.jornada = jornada
    users.direccion= direccion
    db.session.commit()
    return redirect('/Usuarios')

@app.route('/save_Users', methods=['POST'] )
def guardar_Users():
    usuarios = request.json['full_name,Email,password,telefono,especialidad,jornada,direccion,id_roles']
    print(usuarios)
    new_Users = Users(usuarios)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')

'''@routes_user.route('/conliststudiantes', methods=['GET'])
def consullist2():
    datos= {}
    resultado = db.session.query(TblUsuarios, tblrolesusuarios). \
        select_from(TblUsuarios.Cedula, TblUsuarios.full_name, TblUsuarios.jornada, tblrolesusuarios.rol).join(tblrolesusuarios).filter(tblrolesusuarios.roles== "estudiante").all()
    i=0
    for tblusuarios,tblrolesusuarios in resultado:
        i+=1	       
        datos[i] = {
        'NIE':TblUsuarios.Cedula,
		'Nombre':TblUsuarios.full_name,
		'Jornada':TblUsuarios.jornada,                    
        }
    print(datos)
    return datos
'''


@routes_user.route('/eliminarpersonal', methods=['GET'] )
def eliminarU(id):

    usu = Users.query.get(id)
    db.session.delete(usu)
    db.session.commit()
    return jsonify(UsuariosSchema.dump(usu)) 
