from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.citas import citas, citasSchema

routes_citas = Blueprint("routes_citas", __name__)

cita_schema = citasSchema()
citas_Schema = citasSchema(many=True)

#Datos de la tabla autores
@routes_citas.route('/autores', methods=['GET'])
def obtenercitas():    
    returnall = citas.query.all()
    result_citas = citas_Schema.dump(returnall)
    return jsonify(result_citas)


#<--------------------------CRUD AUTORES--------------------------->
@routes_citas.route('/eliminarautores/<id>', methods=['GET'] )
def eliminarcitas(id):
    rol = citas.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(cita_schema.dump(rol))

@routes_citas.route('/actualizarautores', methods=['POST'] )
def actualizarcitas():
    id = request.json['id']
    nombre = request.json['nombre']
    nacionalidad = request.json['nacionalidad']
    rautores = citas.query.get(id)
    rautores.autores = nombre
    rautores.autores = nacionalidad
    db.session.commit()
    return redirect('/autores')

@routes_citas.route('/saveautores', methods=['POST'] )
def guardar_citas():
    autor = request.json['nombre', 'nacionalidad']
    new_autor = citas(autor)
    db.session.add(new_autor)
    db.session.commit()
    return redirect('/autores')