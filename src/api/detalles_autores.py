from flask import Flask, Blueprint,  redirect, request, jsonify, json, session, render_template
from common.Toke import *
from config.db import db, app, ma

from Model.detalles_autores import DetallesAutores, detallesAutoresSchema

routes_Deautores = Blueprint("routes_Dautor", __name__)

Deta_autor_schema = detallesAutoresSchema()
Detalles_autores_Schema = detallesAutoresSchema(many=True)

@routes_Deautores.route('/detalles_autores', methods=['GET'])
def detalles_autores():    
    returnall = DetallesAutores.query.all()
    result_detaautores = Detalles_autores_Schema.dump(returnall)
    return jsonify(result_detaautores)

#<--------------------------CRUD DETALLES_AUTORES--------------------------->
@routes_Deautores.route('/eliminarDautores/<id>', methods=['GET'] )
def eliminardetalles(id):
    Dautor = DetallesAutores.query.get(id)
    db.session.delete(Dautor)
    db.session.commit()
    return jsonify(Deta_autor_schema.dump(Dautor))

@routes_Deautores.route('/saveDautores', methods=['POST'] )
def guardar_detalles():
    Dautores = request.json['id_libros', 'id_autores']
    print(Dautores)
    new_Dautor = DetallesAutores(Dautores)
    db.session.add(new_Dautor)
    db.session.commit()
    return redirect('/detalles_autores')

@routes_Deautores.route('/actualizarautores', methods=['POST'] )
def actualizar_detalles():
    id = request.json['id']
    id_libros = request.json['id_libros']
    id_autores = request.json['id_autores']
    Dautores = DetallesAutores.query.get(id)
    Dautores.detalles_autores = id_libros
    Dautores.detalles_autor = id_autores
    db.session.commit()
    return redirect('/detalles_autores')

