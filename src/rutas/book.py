from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Libros import Libros

routes_book = Blueprint("routes_book", __name__)


@routes_book.route('/indexbook', methods=['GET'] )
def indexbook():
    
    return render_template('/main/book.html')

@routes_book.route('/guardarbook',methods=['POST'])
def savebook():
    book = request.form['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion', 'id_deta_cat', 'id_autor', 'id_editoral', 'id_proov']
    print(book)
    new_libro = Libros(book)
    db.session.add(new_libro)
    db.session.commit()
    return book