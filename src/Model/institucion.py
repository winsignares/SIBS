from config.db import db, app, ma 

class institucion(db.Model):
    __tablename__ = "tblinstitucion"

    
    id  = db.Column(db.Integer, primary_key=True)
    codigo_infraestructura = db.Column(db.String(50))
    nombre_institucion = db.Column(db.String(50))
    distrito = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    año = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer, db.ForeignKey('TblUsuarios.id'))
  

    def __init__(self, codigo_infraestructura, nombre_institucion, distrito, telefono, año):
        self.codigo_infraestructura = codigo_infraestructura
        self.nombre_institucion = nombre_institucion
        self.distrito = distrito
        self.telefono = telefono
        self.año = año
       
   
        
with app.app_context():
    db.create_all()

class institucionSchema(ma.Schema):
    class Meta:
        fields = ('id','codigo_infraestructura','nombre_institucion', 'distrito', 'telefono','año','id_usuario')