
from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.RolesUsuarios import RolesUsuarios, RolesSchema

routes_roles = Blueprint("routes_rol", __name__)
#Roles
rolesusuario_schema = RolesSchema()
rolesusuarios_schema = RolesSchema(many=True)

@routes_roles.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Hola Mundo!!"


#Roles
#---------SAVE/CREAR------------
@routes_roles.route('/saveroles', methods=['POST'] )
def guardar_roles():
    roles = request.json['roles']
    print(roles)
    new_rol = RolesUsuarios(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/rusuarios')


@routes_roles.route('/rusuarios', methods=['GET'])
def rusuario():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = RolesUsuarios.query.all()
        result_rolesusuaiors = rolesusuarios_schema.dump(returnall)
        return jsonify(result_rolesusuaiors)
    else:
        return vf

