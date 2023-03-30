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



@routes_searchbooks.route('/indexlogin', methods=['GET'] )
def indexlogin(): 

    return render_template('/main/login.html')
<<<<<<< HEAD

=======
>>>>>>> main
>>>>>>> da22f4f44c313193996536cdff031f8490edf0bb
