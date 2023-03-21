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

from Model.Solicitudes import Solicitudes, SolicitudesSchema
from Model.estadosolicitud import estadosolicitud, estadoSchema
from Model.Det_Solicitud import Det_Solicitud, Det_SolicitudesSchema

from dotenv import load_dotenv

#importar routes
from api.user import routes_user
from api.roles import routes_roles
from api.estadosoli import routes_stadosolicitud
from api.Libros import routes_Libros
from api.Det_Solicitud import routes_Dsolicitudes
from api.proveedor import routes_proveedores
from api.autores import routes_autores
from api.detalles_autores import routes_Deautores


#ubicacion del api 
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_Libros, url_prefix="/api")
<<<<<<< HEAD
app.register_blueprint(routes_autores,  url_prefix="/api")
app.register_blueprint(routes_Deautores,  url_prefix="/api")
=======
app.register_blueprint(routes_Dsolicitudes, url_prefix="/api")
app.register_blueprint(routes_proveedores, url_prefix="/api")
>>>>>>> 65d5dcdee6ae46b2df6e125e4911d76098244f90
#blue-print proveedores
app.register_blueprint(routes_proveedor, url_prefix="/api")



#Categoria
Categoria_schema = CategoriasSchema()
Categorias_schema = CategoriasSchema(many=True)



#Proveedores (alguien modifico esto ?)
Proveedor_schema = SolicitudesSchema()
Proveedores_schema = SolicitudesSchema(many=True)


categoria_detaSchema = cate_detaSchema()
categorias_detaSchema = cate_detaSchema(many=True)

editorial_Schema = EditorialesSchema()
editoriales_Schema = EditorialesSchema(many=True)

solicitud_schema = SolicitudesSchema()
solicitudes_schema = SolicitudesSchema(many=True)


detalleSolicitud_schema= Det_SolicitudesSchema()
detalleSolicitudes_schema= Det_SolicitudesSchema(many=True)


#--------SAVE/CREAR-----------
@app.route('/saveCat', methods=['POST'] )
def guardar_categoria():
    categori = request.json['N_cat']
    print(categori)
    new_Cat = Categorias(categori)
    db.session.add(new_Cat)
    db.session.commit()
    return redirect('/Categorias')


#tbledioriales
@app.route('/Editoriales', methods=['GET'])
def Editoriales():    
    returnall = Editoriales.query.all()
   
    result_Editoriales = EditorialesSchema.dump(returnall)
    return jsonify(result_Editoriales)
#----------------------CRUD SOLICITUDES--------------------------------
#metodo para solicitudes
@app.route('/solicitudes', methods=['GET'])
def solicitudes():
    returnall = Solicitudes.query.all()
    resultado_solicitudes = solicitudes_schema.dump(returnall)
    return jsonify(resultado_solicitudes)
#guardar solicitudes 
@app.route('/savesolicitudes', methods=['POST'])
def guardar_solicitudes():
    solicitudes = request.json['fecha_solicitud', 'cantidad','Id_usu' ]
    print(solicitudes)
    new_soli = Solicitudes(solicitudes)
    db.session.add(new_soli)
    db.session.commit()
    return redirect('/savesolicitudes')
#Eliminar   solicitudes
@app.route('/deletesolicitudes/<id>', methods=['GET'] )
def eliminarD(id):
    solicitudes = Libros.query.get(id)
    db.session.delete(solicitudes)
    db.session.commit()
    return jsonify(solicitudes_schema.dump(solicitudes)) 
#Actualizar Solicitudes
@app.route('/updatesolicitudes', methods=['POST'] )
def actualizarS():
    id = request.json['id']
    solicitudes = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = Proveedores.query.get(id)
    pusuario.cantidad = solicitudes
    db.session.commit()
    return redirect('/updatesolicitudes')





#Datos de la tabla Datos de categorias
@app.route('/deta_cate', methods=['GET'])
def category():    
    returnall = cate_deta.query.all()
    result_cate_deta = categorias_detaSchema.dump(returnall)
    return jsonify(result_cate_deta)


#metodos para Proveedores inicio
#metodos para Proveedores final 





@app.route("/")
def index():
    return "Hola Mundo!! Dulfran   xD"

#URL/ Categorias



#Eliminar - Categoria
@app.route('/clearCat', methods=['GET'] )
def eliminarCat(id):
    #id = request.args.get('id')
    #id = request.json['id']
    Cat = Categorias.query.get(id)
    db.session.delete(Cat)
    db.session.commit()
    return jsonify(CategoriasSchema.dump(Cat)) 

#Actualizar - Categoria
@app.route('/updateCat', methods=['POST'] )
def actualizarCat():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']
    id = request.json['id']
    N_cat = request.json['N_cat']
    Descripcion = request.json['Descripcion']

    updateCat = Categorias.query.get(id)
    updateCat.nameCat = N_cat
    updateCat.descripCat = Descripcion

    db.session.commit()
    return redirect('/Categorias')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
# Datos de la tabla de Editoriales
@app.route('/eliminarestadosolicitud/<id>', methods=['GET'] )
def eliminaestadosoli(id):
    fecha = estadosolicitud.query.get(id)
    id_solicitud = estadosolicitud.query.get(id)
    fecha_devolucion = estadosolicitud.query.get(id)
    dias_atraso = estadosolicitud.query.get(id)
    estado = estadosolicitud.query.get(id)
    
    db.session.delete(fecha,id_solicitud,fecha_devolucion, dias_atraso,estado)
    db.session.commit()
    return jsonify(estadoSchema.dump(fecha,id_solicitud,fecha_devolucion,dias_atraso,estado))

@app.route('/saveestadosolicitud', methods=['POST'] )
def guardar_estadosolicitud():
    fecha = request.json['fecha']
    id_solicitud = request.json['id_solicitud']
    fecha_devolucion = request.json['fecha_devolucion']
    dias_atraso = request.json['dias_atraso']
    estado = request.json['estado']
    print(fecha,id_solicitud,fecha_devolucion,dias_atraso,estado)
    new_estadosolicitud = estadosolicitud(fecha,id_solicitud,fecha_devolucion,dias_atraso,estado)
    db.session.add(new_estadosolicitud)
    db.session.commit()
    return redirect('/estadosolicitud')


@app.route('/actualizar_estadosolicitud', methods=['POST'] )
def actualizar_estadosolicitud():
    id = request.json['id']
    fechas = request.json['fechas']
    id_solicitudes = request.json['id_solicitud']
    fecha_devoluciones = request.json['fecha_devolucion']
    dias_atrasos = request.json['dias_atraso']
    estados = request.json['estado']
    
    estadosolicitud = estadosolicitud.query.get(id)
    estadosolicitud.fechas = fechas 
    estadosolicitud.id_solicitudes = id_solicitudes
    estadosolicitud.fecha_devolucion = fecha_devoluciones
    estadosolicitud.dias_atraso = dias_atrasos
    
    
    
    
    estadosolicitud.estado = estados
    db.session.commit()
    return redirect('/estadosolicitud')





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