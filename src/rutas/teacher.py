from config.db import db, app, ma
from Model.Usuarios import Users
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_teacher = Blueprint("routes_teacher", __name__)

@routes_teacher.route('/indexteacher', methods=['GET'] )
def indexteacher():
    
    return render_template('/main/teacher.html')

@routes_teacher.route('/saveinstructor', methods=['POST'] )
def guardarinstru():
    full_name = request.json['full_name']
    email = request.json['email']
    telefono = request.json['telefono']
    especialidad = request.json['especialidad']
    jornada = request.json['jornada']
    print(full_name,email,telefono,especialidad,jornada)
    new_Users = Users(full_name,email,telefono,especialidad,jornada)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')