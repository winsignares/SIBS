from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Proveedores import Proveedores

routes_proveedores = Blueprint("routes_proveedores", __name__)

@routes_proveedores.route('/indexprovider', methods=['GET'] )
def indexprovider():
    
    return render_template('/main/provider.html')

@routes_proveedores.route('/guardarprovider', methods=['POST'] )
def saveprovider():
    
    Nombre_proveedor = request.json['Nombre_proveedor']
    Telefono = request.json['Telefono']
    Direccion = request.json['Direccion']
    Descripcion = request.json['Descripcion']
    
    print(Nombre_proveedor)
    new_provider = Proveedores(Nombre_proveedor,Telefono,Direccion,Descripcion)
    db.session.add(new_provider)
    db.session.commit()
    return "OK"
