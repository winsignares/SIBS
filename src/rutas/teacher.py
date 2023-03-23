from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_teacher = Blueprint("routes_teacher", __name__)

@routes_teacher.route('/indexteacher', methods=['GET'] )
def indexteacher():
    
    return render_template('/main/teacher.html')