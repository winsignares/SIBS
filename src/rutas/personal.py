from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_personal = Blueprint("routes_personal", __name__)


@routes_home.route('/indexhome', methods=['GET'] )
def indexhome():
    
    return render_template('/main/Home.html')