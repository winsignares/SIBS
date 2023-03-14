from config.db import db, app, ma 

class Solicitudes(db.Model):
    __tablename__ = "tbSolicitudes"

    id = db.Columm (db.Integer, primary_key = True)
    fecha_solicitud = db.Columm (db.Datetime)
    cantidad = db.Columm (db.Integer)
  #  id_usu = db.Columm (db.integer) 
    

    def __init__(self, fecha_solicitud, cantidad, id_usu ):
        self.fecha_solicitud = fecha_solicitud
        self.cantidad = cantidad
        self.id_usu = id_usu


with app.app_context():
    db.create_all()

class SolicitudesSchema(ma.Schema):
    class meta:
        fields = ('id', 'fecha_solicitud','cantidad', 'id_usu' )
