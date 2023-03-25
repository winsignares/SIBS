from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_section = Blueprint("routes_section", __name__)


@routes_section.route('/indexsection', methods=['GET'] )
def indexsection():
    
    return render_template('/main/Section.html')

