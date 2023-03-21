#10.230.16.229
#10.230.16.238
#10.230.16.196

#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

from Model.Categorias import Categorias, CategoriasSchema

from Model.Proveedores  import Proveedores, ProveedoresSchema
from Model.autores import autores, AutoresSchema

from Model.Editoriales import Editoriales, EditorialesSchema
from Model.Libros import Libros, LibrosSchema
from Model.detalles_autores import DetallesAutores, detallesAutoresSchema
from Model.Cate_deta import cate_deta, cate_detaSchema

from Model.Solicitudes import Solicitudes, SolicitudesSchema
from Model.estadosolicitud import estadosolicitud, estadoSchema
from Model.Det_Solicitud import Det_Solicitud, Det_SolicitudesSchema

from dotenv import load_dotenv

from api.user import routes_user
from api.roles import routes_roles
from api.estadosoli import routes_stadosolicitud

app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_stadosolicitud, url_prefix="/api")





#Categoria
Categoria_schema = CategoriasSchema()
Categorias_schema = CategoriasSchema(many=True)
#Autores
autor_schema = AutoresSchema()
autores_Schema = AutoresSchema(many=True)

#Proveedores
Proveedor_schema = SolicitudesSchema()
Proveedores_schema = SolicitudesSchema(many=True)


categoria_detaSchema = cate_detaSchema()
categorias_detaSchema = cate_detaSchema(many=True)
Deta_autor_schema = detallesAutoresSchema()
Detalles_autores_Schema = detallesAutoresSchema(many=True)
editorial_Schema = EditorialesSchema()
editoriales_Schema = EditorialesSchema(many=True)

libro_schema = LibrosSchema()
libros_Schema = LibrosSchema(many=True)
solicitud_schema = SolicitudesSchema()
solicitudes_schema = SolicitudesSchema(many=True)


detalleSolicitud_schema= Det_SolicitudesSchema()
detalleSolicitudes_schema= Det_SolicitudesSchema(many=True)

#USUARIOS
#-------SAVE/CREAR------------


#Categoria
#--------SAVE/CREAR-----------
@app.route('/saveCat', methods=['POST'] )
def guardar_categoria():
    categori = request.json['N_cat']
    print(categori)
    new_Cat = Categorias(categori)
    db.session.add(new_Cat)
    db.session.commit()
    return redirect('/Categorias')
#Autores
#---------SAVE/CREAR------------
@app.route('/saveautores', methods=['POST'] )
def guardar_autores():
    autores = request.json['nombre', 'nacionalidad']
    print(autores)
    new_autor = autores(autores)
    db.session.add(new_autor)
    db.session.commit()
    return redirect('/autores')
#Proveedores
#---------SAVE/CREAR------------
@app.route('/saveProveedores', methods=['POST'])
def guardar_Proveedores():    
    newProveedores = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    new_pro = Proveedores(newProveedores)
    db.session.add(new_pro)
    db.session.commit()
    return redirect('/Proveedores')


#Datos de la tabla autores
@app.route('/autores', methods=['GET'])
def autores():    
    returnall = autores.query.all()
    result_autores = autores_Schema.dump(returnall)
    return jsonify(result_autores)

#Datos de la tabla Detalles_autores
@app.route('/detalles_autores', methods=['GET'])
def detalles_autores():    
    returnall = DetallesAutores.query.all()
    result_detaautores = Detalles_autores_Schema.dump(returnall)
    return jsonify(result_detaautores)
#tbledioriales
@app.route('/Editoriales', methods=['GET'])
def Editoriales():    
    returnall = Editoriales.query.all()
   
    result_Editoriales = EditorialesSchema.dump(returnall)
    return jsonify(result_Editoriales)

#----------------------------crud libros
#metodo para libros
@app.route('/libros', methods=['GET'])
def libros():    
    returnall = Libros.query.all()
    resultado_libros = libros_Schema.dump(returnall)
    return jsonify(resultado_libros)

@app.route('/savelibros', methods=['POST'] )
def guardar_Libros():
    addlibros = request.json['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion', 'id_deta_cat', 'id_autor', 'id_editoral', 'id_proov']
    print(addlibros)
    new_libro = Libros(addlibros)
    db.session.add(new_libro)
    db.session.commit()
    return redirect('/libros')

@app.route('/actualizarlibros', methods=['POST'] )
def actualizarL():

    id = request.json['id']
    libro = request.json['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion']
    nlibros = Libros.query.get(id)
    nlibros.libro = libro
    db.session.commit()
    return redirect('/libros')

@app.route('/eliminarlibros/<id>', methods=['GET'] )
def eliminarL(id):

    libro = Libros.query.get(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify(libros_Schema.dump(libro)) 
#fin
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

#Datos de la tabla autores
@app.route('/autores', methods=['GET'])
def obtenerautores():    
    returnall = autores.query.all()
   
    result_autores = autores_Schema.dump(returnall)
    return jsonify(result_autores)

#Datos de la tabla Detalles_autores


#Datos de la tabla Datos de categorias
@app.route('/deta_cate', methods=['GET'])
def category():    
    returnall = cate_deta.query.all()
    result_cate_deta = categorias_detaSchema.dump(returnall)
    return jsonify(result_cate_deta)


#metodos para Proveedores inicio
@app.route('/Proveedores', methods=['GET'])
def obtenerproveedor():    
    returnall = Proveedores.query.all()
   
    resultado_Proveedores = ProveedoresSchema.dump(returnall)
    return jsonify(resultado_Proveedores)

@app.route('/eliminarProveedores/<id>', methods=['GET'] )
def eliminarP(id):
    prov = Proveedores.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(Proveedores_schema.dump(prov)) 

@app.route('/actualizarProveedores', methods=['POST'] )
def actualizarP():
    id = request.json['id']
    prov = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = Proveedores.query.get(id)
    pusuario.Nombre_proveedor = prov
    db.session.commit()
    return redirect('/Proveedores')
#metodos para Proveedores final 


@app.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = Users.query.all()
   
    resultado_usuarios = Usuarios_Schema.dump(returnall)
    return jsonify(resultado_usuarios)


@app.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = RolesUsuarios.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(rolesusuario_schema.dump(rol)) 

@app.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = RolesUsuarios.query.get(id)
    rusuario.roles = rolf
    db.session.commit()
    return redirect('/rusuarios')

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


#<----------------------------------------------------------------->
#<--------------------------CRUD AUTORES--------------------------->
@app.route('/eliminarautores/<id>', methods=['GET'] )
def eliminarautores(id):
    rol = autores.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(autor_schema.dump(rol))


@app.route('/actualizarautores', methods=['POST'] )
def actualizarautores():
    id = request.json['id']
    nombre = request.json['nombre']
    nacionalidad = request.json['nacionalidad']
    rautores = autores.query.get(id)
    rautores.autores = nombre
    rautores.autores = nacionalidad
    db.session.commit()
    return redirect('/autores')
#<--------------------------CRUD DETALLES_AUTORES--------------------------->
@app.route('/eliminarDautores/<id>', methods=['GET'] )
def eliminardetalles (id):
    Dautor = DetallesAutores.query.get(id)
    db.session.delete(Dautor)
    db.session.commit()
    return jsonify(Deta_autor_schema.dump(Dautor))

@app.route('/saveDautores', methods=['POST'] )
def guardar_detalles():
    Dautores = request.json['id_libros', 'id_autores']
    print(Dautores)
    new_Dautor = detalles_autores(Dautores)
    db.session.add(new_Dautor)
    db.session.commit()
    return redirect('/detalles_autores')

@app.route('/actualizarautores', methods=['POST'] )
def actualizar_detalles():
    id = request.json['id']
    id_libros = request.json['id_libros']
    id_autores = request.json['id_autores']
    Dautores = detalles_autores.query.get(id)
    Dautores.detalles_autores = id_libros
    Dautores.detalles_autores = id_autores
    db.session.commit()
    return redirect('/detalles_autores')

'''#crud de usuarios
@app.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    full_name = Users.query.get(id)
    Email = Users.query.get(id)
    telefono = Users.query.get(id)
    especialidad = Users.query.get(id)
    jornada = Users.query.get(id)
    direccion = Users.query.get(id)
    db.session.delete(full_name,Email,telefono,especialidad,jornada,direccion)
    db.session.commit()
    return jsonify(UsuariosSchema.dump(full_name,Email,telefono,especialidad,jornada,direccion)) 
'''


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