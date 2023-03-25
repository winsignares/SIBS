from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_home = Blueprint("routes_home", __name__)


@routes_home.route('/indexhome', methods=['GET'] )
def indexhome():
    
    return render_template('/main/Home.html')


@routes_home.route('/indexadministrativo', methods=['GET'] )
def indexadministradores():
    
    return render_template('/main/administradores.html')
#-----------------RUTA DOCENTES-------------------------------
@routes_home.route('/indexdocentes', methods=['GET'] )
def indexdocentes():

    return render_template('/main/docentes.html')
#-----------------PERSONAL ADMINISTRATIVO---------------------
@routes_home.route('/indexpersonal administrativo', methods=['GET'])
def indexpersonaladministrativo():

    return render_template('/main/personaladministrativo.html')
#-----------------LIBROS--------------------------------------
@routes_home.route('/indexlibros', methods=['GET'])
def indexlibros():

    return  render_template('/main/book.html')
#--------------------------------------------------------------
@routes_home.route('/indexconfiguracionesavanzadas', methods=['GET'])
def indexconfiguracionesavanzadas():
    
    return render_template('/main/advancesettings.html')




