from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema
#Categoria - Schema
Categoria_schema = CategoriasSchema()
Categorias_schema = CategoriasSchema(many=True)
routes_categorias = Blueprint("routes_categorias", __name__)


@routes_categorias.route('/indexcategorias', methods=['GET'])
def indexcategorias():
    
    return render_template('/main/Categoria.html')

@routes_categorias.route('/mostrarCategorias', methods=['GET'])
def Categoria():    
        returnall = Categorias.query.all()    
        result_Categoria = Categorias_schema.dump(returnall)
        return jsonify(result_Categoria)