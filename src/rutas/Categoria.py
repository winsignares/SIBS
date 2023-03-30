from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema

routes_category = Blueprint("routes_categ", __name__)


@routes_category.route('/indexcategoria', methods=['GET'] )
def indexCategoria():
    
    return render_template('/main/Categoria.html')

@routes_category.route('/guardarcategoria',methods=['POST'])
def savecategoria():
   
 #request.form['title']
    NombreCategoria = request.form['fullname']
    print(NombreCategoria)
    new_rol = Categorias(NombreCategoria)
    db.session.add(new_rol)
    db.session.commit()
    return NombreCategoria
