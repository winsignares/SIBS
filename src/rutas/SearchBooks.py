from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_searchbooks = Blueprint("routes_searchbooks", __name__)


@routes_searchbooks.route('/indexsearchbooks', methods=['GET'] )
def indexsearchbooks():
    
<<<<<<< HEAD
    return render_template('/main/SearchBoks.html')
=======
    return render_template('/main/SearchBoks.html')

@routes_searchbooks.route('/indexbuscador', methods=['GET'] )
def indexbuscador(): 

    return render_template('/main/book.html')
>>>>>>> a6fabb5d3635af4ea5a8a043194983e81e57e6fe
