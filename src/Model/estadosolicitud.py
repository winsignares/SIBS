from config.db import db, app, ma 

class estadosolicitud(db.Model):
    __tablename__ = "tblestadosolicitud"

    
    id  = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.time)
    id_solicitud =db.Column(db.Interger)
    fecha_devolucion = db.Column(db.Integer)
    dias_atraso = db.Column(db.Integer)
    estado = db.Column(db.Integer)
    

    def __init__(self, fecha,id_solicitud , fecha_devolucion,dias_atraso,estado):
        self.fecha = fecha
        self.id_solicitud = id_solicitud
        self.fecha_devolucion = fecha_devolucion
        self.dias_atraso = dias_atraso
        self.estado = estado
with app.app_context():
    db.create_all()

class estadoSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha' ,'id_solicitud' ,'fecha_devolucion','dias_atraso' ,'estado')

