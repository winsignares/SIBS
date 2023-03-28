from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model import institucion
routes_institution = Blueprint("routes_institution", __name__)


@routes_institution.route('/indexinstitution', methods=['GET'] )
def indexinstitution():
    
    return render_template('/main/institution.html')



@routes_institution.route('/guardarinstitution',methods=['POST'])
def saveinstitution():
    #request.form['title']

    #en el fullname va el dato de la db y en Roles de usuarios va la tbala donde se sacan los datos de la db
    codigoinfra = request.form['codigo_infraestructura']
    nombreinsti = request.form['nombre_institucion']
    distrito = request.form['distrito']
    telefono = request.form['telefono']
    año = request.form['año']
    print(codigoinfra,nombreinsti,distrito,telefono,año)
    new_insti = institucion(codigoinfra)
    db.session.add(new_insti)
    db.session.commit()
    return new_insti


