
from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuarios import RolesUsuarios, RolesSchema

routes_listpersonal = Blueprint("routes_listpersonal", __name__)

@routes_listpersonal.route('/indexlist_personal', methods=['GET'] )
def indexlist_personal():
    
    return render_template('/main/listpersonal.html')


'''
@routes_listpersonal.route('/conpersonal', methods=['GET'])
def consullist():
    print("Yisus, I trust you")
    tblusuarios = db.Table('tblusuarios', db.metadata, autoload=True, autoload_with=db.engine)
    usuarios_alias = db.aliased(tblusuarios)
    datos= {}
    resultado = db.session.query(tblusuarios).filter(tblusuarios.id_roles == 4).all()
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
    resultado = db.session.query(Users, RolesUsuarios). select_from(Users).join(RolesUsuarios).filter(RolesUsuarios.roles== "Personal").all()
    users = []
    i = 0
    for usuarios, roles in resultado:
        i += 1
        datos[i] = {
        'dui':usuarios.cedula,
		'nombre':usuarios.full_name,
		'telefono':usuarios.telefono,
		'cargo': usuarios.especialidad                      
        }
    users.append(datos)
    print(users)
    return jsonify(datos)

'''
@app.route('/selectrol/<id_roles>', methods=['GET'] )
def person(id_roles):
    cedula = Users.query.get(id_roles)
    full_name = Users.query.get(id_roles)
    telefono = Users.query.get(id_roles)
    especialidad = Users.query.get(id_roles)      
    db.session.select(cedula, full_name,telefono,especialidad)
    db.session.commit()
    return jsonify(UsuariosSchema.dump(cedula, full_name,telefono,especialidad)) '''