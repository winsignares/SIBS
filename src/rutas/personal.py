from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
<<<<<<< HEAD
from Model.RolesUsuarios import RolesUsuarios
=======
>>>>>>> main

routes_personal = Blueprint("routes_personal", __name__)


@routes_personal.route('/indexpersonal', methods=['GET'] )
def indexpersonal():
    
<<<<<<< HEAD
    return render_template('/main/personal.html')

@routes_personal.route('/guardarperso',methods=['POST'])
def saveperso():
    #request.form['title']
    fullname = request.form['fullname']
    print(fullname)
    new_rol = RolesUsuarios(fullname)
    db.session.add(new_rol)
    db.session.commit()
    return fullname
=======
    return render_template('/main/personal.html')
>>>>>>> main
