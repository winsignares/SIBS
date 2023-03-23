#10.230.16.229
#10.230.16.238
#10.230.16.196

#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

from dotenv import load_dotenv

#importar routes
from api.user import routes_user
from api.roles import routes_roles
from api.estadosoli import routes_stadosolicitud
from api.Libros import routes_Libros
from api.Det_Solicitud import routes_Dsolicitudes
from api.categoria import routes_category
from api.proveedor import routes_proveedores
from api.autores import routes_autores
from api.detalles_autores import routes_Deautores
from api.Editoriales import routes_Editorial
from api.solicitudes import routes_solicitudes
#rutas
from rutas.home import routes_home
#Santiago

#luis
from rutas.advancesettings import routes_advancesettings
#dainer
from rutas.Admin import routes_Admin
#Gonzalo
from rutas.book import routes_book
#David


#Antonio

#Edwin

#Alejo
from rutas.listadmin import routes_listadmin
#Alet
from rutas.listcategory import routes_listcategory
#Julieth
from rutas.list_personal import routes_listpersonal
#Wilches
from rutas.listprovider import routes_listprovider
#Benedetty
from rutas.listsesion import routes_listsesion
#Jasson

#Sthiwar
from rutas.loan import routes_loan
#Hader

#Jean
from rutas.loanpending import routes_PresPendientes
#Ivan
from rutas.personal import routes_personal
#Ivan villalobos

#Saray

#Camilo
from rutas.reports import routes_report
#Jonathan
from rutas.section import routes_section
#Jorge
from rutas.SearchBooks import routes_searchbooks 

from rutas.teacher import routes_teacher

#ubicacion del api 
app.register_blueprint(routes_stadosolicitud, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_Libros, url_prefix="/api")
app.register_blueprint(routes_autores,  url_prefix="/api")
app.register_blueprint(routes_Deautores,  url_prefix="/api")
app.register_blueprint(routes_Dsolicitudes, url_prefix="/api")
app.register_blueprint(routes_category, url_prefix="/api")
app.register_blueprint(routes_proveedores, url_prefix="/api")
app.register_blueprint(routes_Editorial, url_prefix="/api")
app.register_blueprint(routes_solicitudes, url_prefix="/api")
#ubicación rutas
app.register_blueprint(routes_home, url_prefix="/fronted")



#Santiago

#luis

#dainer
app.register_blueprint(routes_Admin, url_prefix="/fronted")
#Gonzalo
app.register_blueprint(routes_book, url_prefix="/fronted")
#David

#Antonio

#Edwin

#Alejo
app.register_blueprint(routes_listadmin, url_prefix="/api")

#Alet
app.register_blueprint(routes_listcategory, url_prefix="/fronted")
#Julieth
app.register_blueprint(routes_listpersonal, url_prefix="/fronted") 
#Wilches
app.register_blueprint(routes_listprovider, url_prefix="/fronted")
#Benedetty

#Jasson

#Sthiwar
app.register_blueprint(routes_loan, url_prefix="/fronted")
#Hader

#Jean
app.register_blueprint(routes_PresPendientes, url_prefix="/fronted")
#Ivan
app.register_blueprint(routes_personal, url_prefix="/fronted")
#Ivan villalobos

#Saray

#Camilo
app.register_blueprint(routes_report, url_prefix="/fronted")
#Jonathan

#Jorge

app.register_blueprint(routes_teacher, url_prefix="/fronted")

@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/main/login.html', titles=titulo)

@app.route("/algo")
def otr():
    return "hola Santiago"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


#<----------------------------------------------------------------->
'''
@app.route('/consultar3tabla', methods=['GET'])
def consultar3tablas():
    datos= {}
    resultado = db.session.query(Employee,Department, Company). \
        select_from(Employee).join(Department).join(Company).all()
    i=0
    for employee,department,company  in resultado:
        i+=1
        datos[i]={
           
                'Ename': employee.name,
                'Dname': department.name,
                'Cname': company.name          
        }
    print(datos)
    return "Algo"
'''