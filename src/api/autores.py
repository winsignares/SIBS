
from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.autores import autores, AutoresSchema

routes_autores = Blueprint("routes_autor", __name__)

autor_schema = AutoresSchema()
autores_Schema = AutoresSchema(many=True)

#Datos de la tabla autores
@app.route('/autores', methods=['GET'])
def obtenerautores():    
    returnall = autores.query.all()
    result_autores = autores_Schema.dump(returnall)
    return jsonify(result_autores)

#<----------------------------------------------------------------->
#<--------------------------CRUD AUTORES--------------------------->
@app.route('/eliminarautores/<id>', methods=['GET'] )
def eliminarautores(id):
    rol = autores.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(autor_schema.dump(rol))

@app.route('/actualizarautores', methods=['POST'] )
def actualizarautores():
    id = request.json['id']
    nombre = request.json['nombre']
    nacionalidad = request.json['nacionalidad']
    rautores = autores.query.get(id)
    rautores.autores = nombre
    rautores.autores = nacionalidad
    db.session.commit()
    return redirect('/autores')

@app.route('/saveautores', methods=['POST'] )
def guardar_autores():
    autores = request.json['nombre', 'nacionalidad']
    print(autores)
    new_autor = autores(autores)
    db.session.add(new_autor)
    db.session.commit()
    return redirect('/autores')

@routes_autores.route('/autores', methods=['GET'])
def tautores():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = autores.query.all()
        result_autores = autores_Schema.dump(returnall)
        return jsonify(result_autores)
    else:
        return vf