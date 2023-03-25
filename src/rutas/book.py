from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_book = Blueprint("routes_book", __name__)


@routes_book.route('/indexbook', methods=['GET'] )
def indexbook():
    
    return render_template('/main/book.html')

@routes_book.route('/guardarbook',methods=['POST'])
def savebook():
    title = request.form['fullname']
    console.log(fullname)
    new_book = libros(title)
    #db.session.add(new_book)
    #db.session.commit()
    return title