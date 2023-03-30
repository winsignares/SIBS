from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
<<<<<<< HEAD
from Model.Libros import Libros

=======
from Model.Libros import Libros, LibrosSchema
>>>>>>> main
routes_book = Blueprint("routes_book", __name__)


@routes_book.route('/indexbook', methods=['GET'] )
def indexbook():
    
    return render_template('/main/book.html')

@routes_book.route('/guardarbook',methods=['POST'])
def savebook():
<<<<<<< HEAD
    book = request.form['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion', 'id_deta_cat', 'id_autor', 'id_editoral', 'id_proov']
    print(book)
    new_libro = Libros(book)
    db.session.add(new_libro)
    db.session.commit()
    return book
=======
    titulo = request.form['titulo']
    id_autor = request.form['id_autor']
    pais = request.form['pais']
    id_Categoria = request.form['id_Categoria']
    id_proveedor = request.form['id_proveedor']
    ano_publicado = request.form['ano_publicado']
    editorial = request.form['editorial']
    ubicacion = request.form['ubicacion']
    estimado = request.form['estimado']
    cargo = request.form['cargo']
    estado = request.form['estado']

    #book = { titulo,  id_autor, pais,  id_Categoria, id_proveedor,  ano_publicado,  editorial,  ubicacion,  estimado, cargo,  estado}
    #print(book)
    new_libro = Libros(titulo,  id_autor, pais,  id_Categoria, id_proveedor,  ano_publicado,  editorial,  ubicacion,  estimado, cargo,  estado)
    db.session.add(new_libro)
    db.session.commit()
    return {'mensaje':'Informacion Insertada en la base de datos'}


@routes_book.route('/libros', methods=['GET'])
def libros():    
    returnall = Libros.query.all()
    resultado_libros = LibrosSchema.dump(returnall)
    return jsonify(resultado_libros)
>>>>>>> main
