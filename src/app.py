#10.230.16.229

#10.230.16.196
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Categorias import Categorias, CategoriasSchema
from config.db import db, app, ma

from Model.RolesUsuarios import RolesUsuarios, RolesSchema
from Model.Editoriales import Editoriales, EditorialesSchema

from Model.Libros import Libros, LibrosSchema


from Model.Proveedores  import Proveedores, ProveedoresSchema

from Model.estadosolicitud import estadosolicitud, estadoSchema


from Model.Usuarios import Ussers,UsuariosSchema

from Model.Solicitudes import Solicitudes, SolicitudesSchema


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


# datos de estado de solicitud 
estadosolicitud_schema = estadoSchema()
estadosolicitudes_Schema = estadoSchema(many=True)

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
   
    resultado_Proveedores = Proveedores_Schema.dump(returnall)
    return jsonify(resultado_Proveedores)
#metodos para Proveedores final 

#metodo para libros
@app.route('/libros', methods=['GET'])
def libros():    
    returnall = Libros.query.all()
    resultado_libros = libros_Schema.dump(returnall)
    return jsonify(resultado_libros)

#fin
#metodo de estado de solicitudes
@app.route('/estadosolicitud', methods=['GET'])
def estado():    
    returnall = estadosolicitud.query.all()
    resultado_estadosolicitud = estadosolicitudes_Schema.dump(returnall)
    return jsonify(resultado_estadosolicitud)
   
#fin

#datos de usuarios listo
Usuario_Schema= UsuariosSchema()
Usuarios_Schema= UsuariosSchema(many=True)

@app.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = Ussers.query.all()
   
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
    #Precio = request.form['Precio']
    id = request.json['id']
    rol = request.json['roles']
    rusuario = RolesUsuarios.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/rusuarios')

@app.route("/")
def index():
    return "Hola Mundo!! Dulfran   xD"

@app.route('/Categorias', methods=['GET'])
def Categorias():    
    returnall = Categorias.query.all()
   
    result_Categorias = CategoriasSchema.dump(returnall)
    #print(result_rolesusuaiors)
    return jsonify(result_Categorias)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

# Datos de la tabla de Editoriales
@app.route('/Editoriales', methods=['GET'])
def Editoriales():    
    returnall = Editoriales.query.all()
   
    result_Editoriales = EditorialesSchema.dump(returnall)
    return jsonify(result_Editoriales)












































