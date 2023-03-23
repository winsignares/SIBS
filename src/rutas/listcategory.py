from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_listcategory = Blueprint("routes_listcategory", __name__)


@routes_listcategory.route('/indexlistcategory', methods=['GET'] )
def indexlistsesion():
    
    return render_template('/main/listcategory.html')