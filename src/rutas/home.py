from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_home = Blueprint("routes_home", __name__)


@routes_home.route('/indexhome', methods=['GET'] )
def indexhome():
    
    return render_template('/main/Home.html')


@routes_home.route('/indexadministradores', methods=['GET'] )
def indexadministradores():
    
    return render_template('/main/administradores.html')




