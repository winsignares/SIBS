from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users, UsuariosSchema

routes_teacher = Blueprint("routes_teacher", __name__)

@routes_teacher.route('/indexteacher', methods=['GET'] )
def indexteacher():
    
    return render_template('/main/teacher.html')

@routes_teacher.route('/saveinstructor', methods=['POST'] )
def guardarinstru():
    								

    full_name = request.form['full_name']
    password = request.form['password']
    Email = request.form['Email']
    telefono = request.form['telefono']
    especialidad = request.form['especialidad']
    jornada = request.form['jornada']
    id_roles = request.form['id_roles']
    cedula = request.form['cedula']
    print(full_name,Email,telefono,especialidad,jornada)
    new_Users = Users(full_name, password, Email,telefono,especialidad,jornada, id_roles, cedula)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')