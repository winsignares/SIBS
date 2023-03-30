from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import *

routes_categorias = Blueprint("routes_categ", __name__)


@routes_categorias.route('/indexCategoria', methods=['GET'] )
def indexCategoria():
    
    return render_template('/main/Categoria.html')

@routes_categorias.route('/guardarcategoria',methods=['POST'])
def savecategoria():
   
 #request.form['title']
    NombreCategoria = request.form['fullname']
    print(NombreCategoria)
    new_rol = Categorias(NombreCategoria)
    db.session.add(new_rol)
    db.session.commit()
    return NombreCategoria
