from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema


routes_listcategory = Blueprint("routes_listcategory", __name__)

@routes_listcategory.route('/indexlistcategory', methods=['GET'] )
def indexlistcategory():
    return render_template('/main/listcategory.html')

        
@routes_listcategory.route('/viewlist', methods=['GET'])
def consullist():
    datos= {}
    resultado = db.session.query(Categorias).select_from(Categorias).all()
    cate = []
    i = 0
    for catego in resultado:
        i += 1
        datos[i] = {
<<<<<<< HEAD
        'id':catego.id,
		'cat':catego.N_cat,
		'descripcion':catego.Descripcion                       
=======
        'id':cate.id,
		'cat':cate.Nombre_categoria,
		'descripcion':cate.Description,                    
>>>>>>> a3087c4ca59074afcc144fbb8a1a6805efbcae79
        }
    cate.append(datos)
    print(cate)
    return jsonify(datos)