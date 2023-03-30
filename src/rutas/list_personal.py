from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users, UsuariosSchema

routes_listpersonal = Blueprint("routes_listpersonal", __name__)

@routes_listpersonal.route('/indexlist_personal', methods=['GET'] )
def indexlist_personal():
    
    return render_template('/main/listpersonal.html')



@routes_listpersonal.route('/conpersonal', methods=['GET'])
def consullist():
    print("Yisus, I trust you")
    tblusuarios = None
    datos= {}
    resultado = db.session.query(tblusuarios, tblrolesusuarios).select_from(tblusuarios.cedula, tblusuarios.full_name, tblusuarios.telefono, tblusuarios.especialidad, tblrolesusuarios.roles).join(tblrolesusuarios).filter(tblrolesusuarios.roles == "Personal").all()
    i=0
    for tblusuarios,tblrolesusuarios in resultado:
        i+=1	       
        datos[i] = {
        'dui':tblusuarios.cedula,
		'nombre':tblusuarios.full_name,
		'telefono':tblusuarios.telefono,
		'cargo': tblusuarios.especialidad                      
        }
    print(datos.dui)
    return "u rigth"
'''
@routes_listpersonal.route('/conpersonal', methods=['GET'])
def consullist():
    datos= {}
    resultado = db.session.query(TblUsuarios, tblrolesusuarios). \
        select_from(TblUsuarios.Cedula, TblUsuarios.full_name, TblUsuarios.telefono, TblUsuarios.cargo, tblrolesusuarios.rol).join(tblrolesusuarios).filter(tblrolesusuarios.roles== "personal").all()
    i=0
    for TblUsuarios,tblrolesusuarios in resultado:
        i+=1	       
        datos[i] = {
        'DUI':TblUsuarios.Cedula,
		'Nombre':TblUsuarios.full_name,
		'Telefono':TblUsuarios.telefono,
		'Cargo': TblUsuarios.especialidad                      
        }
    print(datos)
    return datos'''