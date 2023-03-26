from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Libros import Libros

routes_book = Blueprint("routes_book", __name__)


@routes_book.route('/indexbook', methods=['GET'] )
def indexbook():
    
    return render_template('/main/book.html')

@routes_book.route('/guardarbook',methods=['POST'])
def savebook():
    titulo = request.form['titulo']
    print(titulo)
    new_libro = Libros(titulo)
    db.session.add(new_libro)
    db.session.commit()
    return titulo