from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias

routes_categorias = Blueprint("routes_categorias", __name__)


@routes_categorias.route('/indexCategoria', methods=['GET'] )
def indexCategoria():
    
    return render_template('/main/Categoria.html')


@routes_categorias.route('/guardarcategoria',methods=['POST'])
def savecategoria():
     
 #request.form['title']
    NumeroCategoria = request.form['NumeroCategoria']
    descripcion = request.form['descripcion']

    print(NumeroCategoria)
    new_category = Categorias(NumeroCategoria,descripcion)
    db.session.add(new_category)
    db.session.commit()
    return 'ok'
