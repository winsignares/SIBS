
from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users, UsuariosSchema
from Model.RolesUsuarios import RolesUsuarios, RolesSchema

routes_listpersonal = Blueprint("routes_listpersonal", __name__)

@routes_listpersonal.route('/indexlist_personal', methods=['GET'] )
def indexlist_personal():
    
    return render_template('/main/listpersonal.html')

#------------------------------MOSTRAR--------------
@routes_listpersonal.route('/conpersonal', methods=['GET'])
def consullist():
    datos= {}
    resultado = db.session.query(Users, RolesUsuarios).select_from(Users).join(RolesUsuarios).filter(RolesUsuarios.roles== "Personal").all()
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

#------------------------------ACTUALIZAR
@routes_listpersonal.route('/actualizarpersonal', methods=['POST'] )
def actualizar_users():
    id = request.form['id']
    full_name = request.form['full_name']
    Email =request.form['Email']
    telefono= request.form['telefono']
    especialidad= request.form['especialidad']
    cedula = request.form['cedula']
    password= request.form['password']
    
    users = Users.query.get(id)
    users.full_name = full_name
    users.Email = Email
    users.telefono = telefono
    users.especialidad= especialidad
    users.cedula = cedula
    users.password= password
    db.session.commit()
    print(id, full_name, Email, telefono, especialidad, password)
    return redirect('/indexlist_personal')

#--------------------------ELIMINAR

@routes_listpersonal.route('/eliminarpersonal', methods=['DELETE'] )
def eliminarperso():
    cedula = request.json.get('cedula')
    dui = Users.query.filter_by(cedula=cedula).first()
    if dui:
        db.session.delete(dui)
        db.session.commit()
        print(cedula)
        print(dui)
        return 'Registro eliminado', 200
    else:
        return 'Registro no encontrado', 404
  
