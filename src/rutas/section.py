from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_section = Blueprint("routes_section", __name__)


@routes_section.route('/indexsection', methods=['GET'] )
def indexsection():
    
    return render_template('/main/Section.html')

@routes_section.route('/saveDatos',methods=['POST'])
def saveadmin():
    #request.form['title']
    fullname = request.form['fullname']
    print(fullname)
    new_rol = RolesUsuarios(fullname)
    db.session.add(new_rol)
    db.session.commit()
    return fullname