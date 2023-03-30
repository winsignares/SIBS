from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema

<<<<<<< HEAD
routes_listcategory = Blueprint("routes_listcategory", __name__)


@routes_listcategory.route('/indexlistcategory', methods=['GET'] )
def indexlistsesion():
    
    return render_template('/main/listcategory.html')

=======

routes_listcategory = Blueprint("routes_listcategory", __name__)

@routes_listcategory.route('/indexlistcategory', methods=['GET'] )
def indexlistcategory():
    return render_template('/main/listcategory.html')




>>>>>>> main
@routes_listcategory.route('/viewlistcategory', methods=['GET'])
def viewlistcategory():
        returnall = Categorias.query.all()
        result_Categoria = CategoriasSchema.dump(returnall)
<<<<<<< HEAD
        return jsonify(result_Categoria) 
=======
        return result_Categoria
>>>>>>> main
