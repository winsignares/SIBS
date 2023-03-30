from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema


routes_listcategory = Blueprint("routes_listcategory", __name__)

@routes_listcategory.route('/indexlistcategory', methods=['GET'] )
def indexlistcategory():
    return render_template('/main/listcategory.html')




@routes_listcategory.route('/viewlistcategory', methods=['GET'])
def viewlistcategor():
    datos= {}
    resultado = db.session.query(tblcategorias).select_from(tblcategorias.id, tblcategorias.N_cat, tblcategorias.Descripcion).all()
    i=0
    for tblcategorias in resultado:
        i+=1	       
        datos[i] = {
        'id':tblcategorias.id,
		'cat':tblcategorias.N_cat,
		'descripcion':tblcategorias.Descripcion,                    
        }
    print(datos.id)
    return "u right"
        
