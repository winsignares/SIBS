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

    return render_template('/main/teacher.html')
#-----------------PERSONAL ADMINISTRATIVO---------------------
@routes_home.route('/indexpersonaladministrativo', methods=['GET'])
def indexpersonaladministrativo():

    return render_template('/main/personal.html')
#-----------------LIBROS--------------------------------------
@routes_home.route('/indexlibros', methods=['GET'])
def indexlibros():

    return  render_template('/main/book.html')
#----------------------------CONFIGURACION AVANZADA---------------------------------
@routes_home.route('/indexconfiguracionesavanzadas', methods=['GET'])
def indexconfiguracionesavanzadas():
    
    return render_template('/main/advancesettings.html')

#-----------------------------ESTUDIANTES---------------------------------------------
@routes_home.route('/indexestudiantes', methods=['GET'])
def indexestudiantes():
    
    return render_template('/main/student.html')

#-----------------------------PROVEEDORES---------------------------------------------
@routes_home.route('/indexproveedores', methods=['GET'])
def indexproveedores():
    
    return render_template('/main/provider.html')

#-----------------------------CATEGORÍA------------------------------------------------
@routes_home.route('/indexcategorias', methods=['GET'])
def indexcategorias():
    
    return render_template('/main/Categoria.html')

#---------------------------SECCIONES---------------------------------------------------
@routes_home.route('/indexsecciones', methods=['GET'])
def indexsecciones():
    
    return render_template('/main/section.html')

#---------------------------Reservaciones----------------------------------------------
@routes_home.route('/indexreservaciones', methods=['GET'])
def indexreservaciones():
    
    return render_template('/main/loanreservation.html')

#---------------------------DEVOLUCIONES PENDIENTES--------------------------------------
@routes_home.route('/indexdevolucionespendientes', methods=['GET'])
def indexdevolucionespendientes():
    
    return render_template('/main/loanpending.html')

#---------------------------PRESTAMOS----------------------------------------------------
@routes_home.route('/indexprestamos', methods=['GET'])
def indexprestamos():

    return render_template('/main/loan.html')

#---------------------------REPORTES Y PRESTAMOS----------------------------------------------------
@routes_home.route('/indexreportesyestadisticas', methods=['GET'])
def indexreportesyestadisticas():

    return render_template('/main/report.html')

#---------------------------MENU IZQUIERDA------------------------------------------------------------
@routes_home.route('/indexinstitution', methods=['GET'])
def indexinstitution():

    return render_template('/main/institution.html')






