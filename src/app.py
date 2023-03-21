#10.230.16.229
#10.230.16.238
#10.230.16.196

#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

from Model.Categorias import Categorias, CategoriasSchema

from Model.Editoriales import Editoriales, EditorialesSchema
from Model.Libros import Libros, LibrosSchema

from Model.Cate_deta import cate_deta, cate_detaSchema


from Model.estadosolicitud import estadosolicitud, estadoSchema
from Model.Det_Solicitud import Det_Solicitud, Det_SolicitudesSchema

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


#ubicacion del api 
app.register_blueprint(routes_stadosolicitud, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_Libros, url_prefix="/api")
app.register_blueprint(routes_autores,  url_prefix="/api")
app.register_blueprint(routes_Deautores,  url_prefix="/api")
app.register_blueprint(routes_Dsolicitudes, url_prefix="/api")
<<<<<<< HEAD
app.register_blueprint(routes_proveedores, url_prefix="/api")
=======
app.register_blueprint(routes_category, url_prefix="/api")
app.register_blueprint(routes_proveedores, url_prefix="/api")
<<<<<<< HEAD
app.register_blueprint(routes_autores,  url_prefix="/api")
app.register_blueprint(routes_Deautores,  url_prefix="/api")
<<<<<<< HEAD
=======
>>>>>>> df019a7e77d152bd8d2d5e91126c01bf45e169fa

=======
>>>>>>> 5cde1d05c24b893e591fe5737ca2c1a8a1f28e9d

<<<<<<< HEAD
#Categoria
Categoria_schema = CategoriasSchema()
Categorias_schema = CategoriasSchema(many=True)

<<<<<<< HEAD
>>>>>>> 6b702cbfd5639202f3da3530e3fc12322c73ace0

#Autores
autor_schema = AutoresSchema()
autores_Schema = AutoresSchema(many=True)
=======

>>>>>>> 5cde1d05c24b893e591fe5737ca2c1a8a1f28e9d

#Proveedores (alguien modifico esto ?)
Proveedor_schema = SolicitudesSchema()
Proveedores_schema = SolicitudesSchema(many=True)

<<<<<<< HEAD
=======
app.register_blueprint(routes_stadosolicitud,  url_prefix="/api")
>>>>>>> 5326bb1272420e02e3b2466e93df3a41a5547e64
=======
>>>>>>> 5cde1d05c24b893e591fe5737ca2c1a8a1f28e9d

=======
>>>>>>> 7e7b247339fe9981b2dc6d7dc8214e9c05c37afa
categoria_detaSchema = cate_detaSchema()
categorias_detaSchema = cate_detaSchema(many=True)

@app.route('/deta_cate', methods=['GET'])
def category():    
    returnall = cate_deta.query.all()
    result_cate_deta = categorias_detaSchema.dump(returnall)
    return jsonify(result_cate_deta)


@app.route("/")
def index():
    return "Hola Mundo!! Dulfran   xD"

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