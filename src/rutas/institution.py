from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, session, render_template
from Model.institucion import institucion
routes_institution = Blueprint("routes_institution", __name__)


@routes_institution.route('/indexinstitution', methods=['GET'] )
def indexinstitution():
    
    return render_template('/main/institution.html')



@routes_institution.route('/guardarinstitution',methods=['POST'])
def saveinstitution():
    #request.form['title']
    codigo_infraestructura = request.form['codigo_infraestructura']
    nombre_institucion = request.form['nombre_institucion']
    distrito = request.form['distrito'] 
    telefono = request.form['telefono'] 
    año = request.form['año'] 
    print(codigo_infraestructura)
    new_institution = institucion(codigo_infraestructura, nombre_institucion, distrito,telefono,año)
    db.session.add(new_institution)
    db.session.commit()
    return "listo"



