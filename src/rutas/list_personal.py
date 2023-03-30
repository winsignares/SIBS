from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users

routes_listpersonal = Blueprint("routes_listpersonal", __name__)

@routes_listpersonal.route('/indexlist_personal', methods=['GET'] )
def indexlist_personal():
    
    return render_template('/main/listpersonal.html')

@routes_listpersonal.route('/conpersonal', methods=['GET'])
def consullist():
    datos= {}
    resultado = db.session.query(tblusuarios, tblrolesusuarios).select_from(tblusuarios.cedula, tblusuarios.full_name, tblusuarios.telefono, tblusuarios.especialidad, tblrolesusuarios.roles).join(tblrolesusuarios).filter(tblrolesusuarios.roles== "Personal").all()
    i=0
    for tblusuarios,tblrolesusuarios in resultado:
        i+=1	       
        datos[i] = {
        'DUI':tblusuarios.cedula,
		'Nombre':tblusuarios.full_name,
		'Telefono':tblusuarios.telefono,
		'Cargo': tblusuarios.especialidad                      
        }
    print(datos.DUI)
    return datos