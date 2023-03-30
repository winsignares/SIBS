from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuarios import RolesUsuarios, RolesSchema

routes_listpersonal = Blueprint("routes_listpersonal", __name__)

@routes_listpersonal.route('/indexlist_personal', methods=['GET'] )
def indexlist_personal():
    
    return render_template('/main/listpersonal.html')



@routes_listpersonal.route('/conpersonal', methods=['GET'])
def consullist():
    print("Yisus, I trust you")
    tblusuarios = db.Table('tblusuarios', db.metadata, autoload=True, autoload_with=db.engine)
    usuarios_alias = db.aliased(tblusuarios)
    datos= {}
    resultado = db.session.query(usuarios_alias).filter(usuarios_alias.id_roles == 4).all()
    i=0
    for usuarios in resultado:
        i+=1	       
        datos[i] = {
        'dui': usuarios.cedula,
		'nombre': usuarios.full_name,
		'telefono': usuarios.telefono,
		'cargo': usuarios.especialidad,                       
        }
    for usuario in datos.values():
        print(usuario)
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