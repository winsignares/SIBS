from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema


routes_listcategory = Blueprint("routes_listcategory", __name__)

@routes_listcategory.route('/indexlistcategory', methods=['GET'] )
def indexlistcategory():
    return render_template('/main/listcategory.html')




@routes_listcategory.route('/viewlist', methods=['GET'])
def viewlistcategor():
    datos= {}
    resultado = db.session.query(Categorias).select_from(Categorias).all()
    i=0
    goria = []
    for cate in resultado:
        i+=1	       
        datos[i] = {
        'id':cate.id,
		'cat':cate.N_cat,
		'descripcion':cate.Descripcion,                    
        }
        goria.append(datos)
    print(goria)
    return jsonify(datos)
        
