from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Proveedores import Proveedores

routes_proveedoress = Blueprint("routes_proveedoress", __name__)

@routes_proveedoress.route('/indexprovider', methods=['GET'] )
def indexprovider():
    
    return render_template('/main/provider.html')

@routes_proveedoress.route('/guardarprovider', methods=['POST'] )
def saveprovider():
    
    
    Nombre_proveedor = request.form['Nombre_proveedor']
    correo = request.form['correo']
    Direccion = request.form['Direccion'] 
    telefono = request.form['telefono'] 
    Descripcion = request.form['Descripcion'] 
    print(Nombre_proveedor)
    new_provee = Proveedores(Nombre_proveedor, correo, Direccion,telefono,Descripcion)
    db.session.add(new_provee)
    db.session.commit()
    return "si"
    

