from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.section import Section
routes_section = Blueprint("routes_section", __name__)


@routes_section.route('/indexsection', methods=['GET'] )
def indexsection():
    
    return render_template('/main/Section.html')

@routes_section.route('/guardarsection',methods=['POST'])
def saveSection():
    #request.form['title']
    fullname = request.form['year','especialidad', 'seccion']
    print(fullname)
    new_section = Section(fullname)
    db.session.add(new_section)
    db.session.commit()
    return fullname