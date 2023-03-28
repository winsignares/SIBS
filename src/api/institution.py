from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.institucion import  institucion,institucionSchema

routes_institucion = Blueprint("routes_institucion", __name__)

#libros

InstitucionSchema = institucionSchema()
institucionesSchema = institucionSchema(many=True)


@routes_institucion.route('/institucion', methods=['GET'])
def libros():    
    returnall = institucion.query.all()
    resultado_institucion = institucionSchema.dump(returnall)
    return jsonify(resultado_institucion)


@routes_institucion.route('/actualizarinstitucion', methods=['POST'] )
def actualizarinsti():
    id = request.json['id']
    Institucion = request.json['codigo_infraestructura','nombre_institucion', 'distrito', 'telefono','año']
    ninstitucion = institucion.query.get(id)
    ninstitucion.Institucion = Institucion
    db.session.commit()
    return redirect('/institucion')


@routes_institucion.route('/eliminarinstitucion/<id>', methods=['GET'] )
def eliminarinsti(id):

    Institucion = institucion.query.get(id)
    db.session.delete(Institucion)
    db.session.commit()
    return jsonify(institucionSchema.dump(Institucion)) 


@routes_institucion.route('/guardarinsti', methods=['POST'] )
def guardarinsti():
    addinstitucion = request.json['codigo_infraestructura','nombre_institucion', 'distrito', 'telefono','año']
    print(addinstitucion)
    new_insti = institucion(addinstitucion)
    db.session.add(new_insti)
    db.session.commit()
    return redirect('/institucion')

