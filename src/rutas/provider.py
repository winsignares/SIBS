from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_provider = Blueprint("routes_provider", __name__)

@routes_provider.route('/indexprovider', methods=['GET'] )
def indexprovider():
    
    return render_template('/main/provider.html')

@routes_provider.route('/saveinstructor', methods=['POST'] )
def guardarinstru():
    Nombre_proveedor = request.json['Nombre_proveedor']
    Telefono = request.json['Telefono']
    Direccion = request.json['Direccion']
    Descripcion = request.json['Descripcion']
    
    print(Nombre_proveedor,Telefono,Direccion,Descripcion)
    new_provider = provider(Nombre_proveedor,Telefono,Direccion,Descripcion)
    db.session.add(new_provider)
    db.session.commit()
    return redirect('/proveedores')