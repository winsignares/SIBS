from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.section import Section, sectionSchema
routes_section = Blueprint("routes_section", __name__)

section_Schema = sectionSchema()
sections_Schema = sectionSchema(many=True)

@routes_section.route('/indexsection', methods=['GET'] )
def indexsection():
    
    return render_template('/main/Section.html')

@routes_section.route('/guardarsection',methods=['POST'])
def saveSection():
    #request.form['title']
    year = request.form['year']
    especialidad = request.form['especialidad']
    seccion = request.form['seccion'] 
    print(year)
    new_section = Section(year, especialidad, seccion)
    db.session.add(new_section)
    db.session.commit()
    return "ok"

@routes_section.route('/showsection', methods=['GET'])
def obtenersection():    
    returnall = Section.query.all()
    result_section = sections_Schema.dump(returnall)
    return jsonify(result_section)

@routes_section.route('/deletesection/<id>', methods=['GET'] )
def eliminarsection(id):
    clear = Section.query.get(id)
    db.session.delete(clear)
    db.session.commit()
    return jsonify(section_Schema.dump(clear))