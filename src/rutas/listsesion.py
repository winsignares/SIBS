from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_listsesion = Blueprint("routes_listsesion", __name__)


@routes_listsesion.route('/indexlistsesion', methods=['GET'] )
def indexlistsesion():
    
    return render_template('/main/listsection.html')