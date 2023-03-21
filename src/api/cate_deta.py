from flask import Blueprint, request, jsonify, json
from common.Toke import *
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Cate_deta import cate_deta, cate_detaSchema

routes_Catego_deta = Blueprint("routes_Catego_deta", __name__)

categoria_detaSchema = cate_detaSchema()
categorias_detaSchema = cate_detaSchema(many=True)

#Datos de la tabla Datos de categorias
@app.route('/deta_cate', methods=['GET'])
def category():    
    returnall = cate_deta.query.all()
    result_cate_deta = categorias_detaSchema.dump(returnall)
    return jsonify(result_cate_deta)