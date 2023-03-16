from config.db import db, app, ma 

class Proveedores(db.Model):
    __tablename__ = "tblproveedores"

    
    id  = db.Column(db.Integer, primary_key=True)
    Nombre_proveedor = db.Column(db.String(50))
    Telefono = db.Column(db.int)
    Direccion = db.Column(db.String(50))
    Descripcion = db.column(db.text)
    

    def __init__(self, Nombre_proveedor, Telefono, Direccion, Descripcion):
        
        self.Nombre_proveedor = Nombre_proveedor
        self.Telefono = Telefono
        self.Direccion = Direccion
        self.Descripcion = Descripcion
        
    
with app.app_context():
    db.create_all()

class ProveedoresSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre_proveedor','Telefono','Direccion','Descripcion')