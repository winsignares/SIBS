from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Usuarios import Users,UsuariosSchema
from Model.RolesUsuarios import RolesUsuarios, RolesSchema

routes_list_estudiantes = Blueprint("routes_list_estudiantes", __name__)

@routes_list_estudiantes.route('/conliststudiantes', methods=['GET'])
def consullist():
    datos= {}
    resultado = db.session.query(Users, RolesUsuarios). select_from(Users).join(RolesUsuarios).filter(RolesUsuarios.roles== "estudiante").all()
    i=0
    for usuarios, roles in resultado:
        i+=1	       
        datos[i] = {
        'NIE':usuarios.telefono,
		'Nombre':usuarios.full_name,
		'Jornada':usuarios.jornada,                    
        }
    print(datos)
    return "u rigth"