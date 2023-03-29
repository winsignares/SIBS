from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from model.section import section , sectionSchema 


routes_listsesion = Blueprint("routes_listsesion", __name__)


@routes_listsesion.route('/indexlistsesion', methods=['GET'] )
def indexlistsesion():
    
    return render_template('/main/listsection.html')



@routes_listsesion.route('/viewlistcategory', methods=['GET'])
def viewlistcategory():
        returnall = section.query.all()
        result_section = sectionSchema.dump(returnall)
        return result_section
