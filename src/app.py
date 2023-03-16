#10.230.16.229

#10.230.16.196

#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema
from config.db import db, app, ma
from Model.RolesUsuarios import RolesUsuarios, RolesSchema
from Model.Editoriales import Editoriales, EditorialesSchema
from Model.Libros import Libros, LibrosSchema
from Model.Proveedores  import Proveedores, ProveedoresSchema
from Model.estadosolicitud import estadosolicitud, estadoSchema
from Model.Usuarios import Users,UsuariosSchema
from Model.Solicitudes import Solicitudes, SolicitudesSchema
from Model.autores import autores, AutoresSchema

#Datos de la tabla autores

autor_schema = AutoresSchema()
autores_Schema = AutoresSchema(many=True)

rolesusuario_schema = RolesSchema()
rolesusuarios_schema = RolesSchema(many=True)

Categoria_schema = CategoriasSchema()
Categoria_schema = CategoriasSchema(many=True)

#Datos de la tabla libros listo

libro_schema = LibrosSchema()
libros_Schema = LibrosSchema(many=True)

#Valores Intermediarios de la TABLA SOLICITUDES
solicitudes_schema = SolicitudesSchema()
solicitudes_schema = SolicitudesSchema(many=True)

#TABLA Proveedores
Proveedores_schema = SolicitudesSchema()
Proveedores_schema = SolicitudesSchema(many=True)


#Datos de la tabla autores
@app.route('/autores', methods=['GET'])
def autores():    
    returnall = autores.query.all()
    result_autores = autores_Schema.dump(returnall)
    return jsonify(result_autores)

@app.route('/rusuarios', methods=['GET'])
def rusuario():    
    returnall = RolesUsuarios.query.all()
   
    result_rolesusuaiors = rolesusuarios_schema.dump(returnall)
    #print(result_rolesusuaiors)
    return jsonify(result_rolesusuaiors)

#metodos para Proveedores inicio
@app.route('/Proveedores', methods=['GET'])
def Proveedores():    
    returnall = Proveedores.query.all()
   
    resultado_Proveedores = ProveedoresSchema.dump(returnall)
    return jsonify(resultado_Proveedores)

@app.route('/saveProveedores', methods=['POST'])
def guardar_Proveedores():    
    newProveedores = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    new_pro = Proveedores(newProveedores)
    db.session.add(new_pro)
    db.session.commit()
    return redirect('/Proveedores')

@app.route('/eliminarProveedores/<id>', methods=['GET'] )
def eliminar(id):
    prov = Proveedores.query.get(id)
    db.session.delete(prov)
    db.session.commit()
    return jsonify(Proveedores_schema.dump(prov)) 

@app.route('/actualizarProveedores', methods=['POST'] )
def actualizar():
    id = request.json['id']
    prov = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = Proveedores.query.get(id)
    pusuario.Nombre_proveedor = prov
    db.session.commit()
    return redirect('/Proveedores')
#metodos para Proveedores final 

#metodo para libros
@app.route('/libros', methods=['GET'])
def libros():    
    returnall = Libros.query.all()
    resultado_libros = libros_Schema.dump(returnall)
    return jsonify(resultado_libros)

@app.route('/savelibros', methods=['POST'] )
def guardar_roles():
    addlibros = request.json['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion', 'id_deta_cat', 'id_autor', 'id_editoral', 'id_proov']
    print(addlibros)
    new_libro = Libros(addlibros)
    db.session.add(new_libro)
    db.session.commit()
    return redirect('/libros')

@app.route('/actualizarlibros', methods=['POST'] )
def actualizar():

    id = request.json['id']
    libro = request.json['titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion']
    nlibros = Libros.query.get(id)
    nlibros.libro = libro
    db.session.commit()
    return redirect('/libros')

@app.route('/eliminarlibros/<id>', methods=['GET'] )
def eliminar(id):

    libro = Libros.query.get(id)
    db.session.delete(libro)
    db.session.commit()
    return jsonify(libros_Schema.dump(libro)) 

#fin


#fin

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
def eliminar(id):

    solicitudes = Libros.query.get(id)
    db.session.delete(solicitudes)
    db.session.commit()
    return jsonify(solicitudes_schema.dump(solicitudes)) 

#Actualizar Solicitudes

@app.route('/updatesolicitudes', methods=['POST'] )
def actualizar():
    id = request.json['id']
    solicitudes = request.json['Nombre_proveedor','Telefono','Direccion','Descripcion']
    pusuario = Proveedores.query.get(id)
    pusuario.cantidad = solicitudes
    db.session.commit()
    return redirect('/updatesolicitudes')



#fin

#datos de usuarios listo
Usuario_Schema= UsuariosSchema()
Usuarios_Schema= UsuariosSchema(many=True)

@app.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = Users.query.all()
   
    resultado_usuarios = Usuarios_Schema.dump(returnall)
    return jsonify(resultado_usuarios)




@app.route('/saveroles', methods=['POST'] )
def guardar_roles():
    roles = request.json['roles']
    print(roles)
    new_rol = RolesUsuarios(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/rusuarios')

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
    rusuario.roles = rol
    db.session.commit()
    return redirect('/rusuarios')

@app.route("/")
def index():
    return "Hola Mundo!! Dulfran   xD"

#URL/ Categorias
@app.route('/Categorias', methods=['GET'])
def Categorias2():    
    returnall = Categorias.query.all()
   
    result_Categorias = CategoriasSchema.dump(returnall)
    #print(result_rolesusuaiors)
    return jsonify(result_Categorias)

#Guardar - Categoria
@app.route('/saveCat', methods=['POST'] )
def guardar_categoria():
    categori = request.json['N_cat']
    print(categori)
    new_Cat = Categorias(categori)
    db.session.add(new_Cat)
    db.session.commit()
    return redirect('/Categorias')

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
    app.run(debug=True, port=5000, host='0.0.0.0')

# Datos de la tabla de Editoriales
@app.route('/Editoriales', methods=['GET'])
def Editoriales():    
    returnall = Editoriales.query.all()
   
    result_Editoriales = EditorialesSchema.dump(returnall)
    return jsonify(result_Editoriales)

#<----------------------------------------------------------------->
#<--------------------------CRUD AUTORES--------------------------->
@app.route('/eliminarautores/<id>', methods=['GET'] )
def eliminarautores(id):
    rol = autores.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(autor_schema.dump(rol))

@app.route('/saveautores', methods=['POST'] )
def guardar_autores():
    autores = request.json['autores']
    print(autores)
    new_autor = autores(autores)
    db.session.add(new_autor)
    db.session.commit()
    return redirect('/autores')

@app.route('/actualizarautores', methods=['POST'] )
def actualizarautores():
    id = request.json['id']
    nombre = request.json['nombre']
    nacionalidad = request.json['nacionalidad']
    rautores = autores.query.get(id)
    rautores.autores = nombre
    db.session.commit()
    return redirect('/autores')


#<----------------------------------------------------------------->


#---------------------------------------------------------------------->
#---------------------------------------------------------------------->
#---------------------------------------------------------------------->
#------------------datos de estado de solicitud------------------------>

# datos de estado de solicitud 
estadosolicitud_schema = estadoSchema()
estadosolicitudes_Schema = estadoSchema(many=True)


#metodo de estado de solicitudes
@app.route('/estadosolicitud', methods=['GET'])
def estado():    
    returnall = estadosolicitud.query.all()
    resultado_estadosolicitud = estadosolicitudes_Schema.dump(returnall)
    return jsonify(resultado_estadosolicitud)
   

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
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
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
#---------------------------------------------------------------------->
#---------------------------------------------------------------------->
#---------------------------------------------------------------------->
#---------------------------------------------------------------------->
