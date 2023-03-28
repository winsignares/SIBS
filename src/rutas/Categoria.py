from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_Categorias = Blueprint("routes_Categorias", __name__)


@routes_Categorias.route('/indexcategoria', methods=['GET'] )
def indexCategorias():
    
    return render_template('/main/Categoria.html')