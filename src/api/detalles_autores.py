from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.detalles_autores import DetallesAutores, detallesAutoresSchema

routes_Deautores = Blueprint("routes_Dautor", __name__)

Deta_autor_schema = detallesAutoresSchema()
Detalles_autores_Schema = detallesAutoresSchema(many=True)

@app.route('/detalles_autores', methods=['GET'])
def detalles_autores():    
    returnall = DetallesAutores.query.all()
    result_detaautores = Detalles_autores_Schema.dump(returnall)
    return jsonify(result_detaautores)

#<--------------------------CRUD DETALLES_AUTORES--------------------------->
@app.route('/eliminarDautores/<id>', methods=['GET'] )
def eliminardetalles (id):
    Dautor = DetallesAutores.query.get(id)
    db.session.delete(Dautor)
    db.session.commit()
    return jsonify(Deta_autor_schema.dump(Dautor))

@app.route('/saveDautores', methods=['POST'] )
def guardar_detalles():
    Dautores = request.json['id_libros', 'id_autores']
    print(Dautores)
    new_Dautor = detalles_autores(Dautores)
    db.session.add(new_Dautor)
    db.session.commit()
    return redirect('/detalles_autores')

@app.route('/actualizarautores', methods=['POST'] )
def actualizar_detalles():
    id = request.json['id']
    id_libros = request.json['id_libros']
    id_autores = request.json['id_autores']
    Dautores = detalles_autores.query.get(id)
    Dautores.detalles_autores = id_libros
    Dautores.detalles_autores = id_autores
    db.session.commit()
    return redirect('/detalles_autores')

@routes_Deautores.route('/detalles_autores', methods=['GET'])
def det_autores():
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = DetallesAutores.query.all()
        result_det_autores = detallesAutoresSchema.dump(returnall)
        return jsonify(result_det_autores)
    else:
        return vf