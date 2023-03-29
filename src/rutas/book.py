from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Libros import Libros, LibrosSchema
from Model.Categorias import Categorias, CategoriasSchema
routes_book = Blueprint("routes_book", __name__)


@routes_book.route('/indexbook', methods=['GET'] )
def indexbook():
    
    return render_template('/main/book.html')

@routes_book.route('/guardarbook',methods=['POST'])
def savebook():
    book = request.form['id','titulo', 'id_autor', 'pais', 'id_Categoria', 'id_proovedor', 'ano_publicado', 'editoral', 'ubicacion', 'estimado', 'cargo', 'estado']
    print(book)
    new_libro = Libros(book)
    db.session.add(new_libro)
    db.session.commit()
    return book

@routes_book.route('/libros', methods=['GET'])
def libros():    
    returnall = Libros.query.all()
    resultado_libros = LibrosSchema.dump(returnall)
    return jsonify(resultado_libros)