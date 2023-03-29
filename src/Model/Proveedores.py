from config.db import db, app, ma 

class Proveedores(db.Model):
    __tablename__ = "tblproveedores"

    
    id  = db.Column(db.Integer, primary_key=True)
    Nombre_proveedor = db.Column(db.String(50))
    correo = db.Column(db.Integer)
    Direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    Descripcion = db.Column(db.Text)
    

    def __init__(self, Nombre_proveedor, correo, Direccion, telefono,Descripcion):
        
        self.Nombre_proveedor = Nombre_proveedor
        self.correo = correo
        self.Direccion = Direccion
        self.telefono = telefono
        self.Descripcion = Descripcion
        
    
with app.app_context():
    db.create_all()

class ProveedoresSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre_proveedor','correo','Direccion','telefono','Descripcion')