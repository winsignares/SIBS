from config.db import db, app, ma

class pagos(db.Model):
    __tablename__ = "tblpagos"

    id_factura = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_odontologo = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_tratamiento = db.Column(db.Integer, db.ForeignKey('tbltratamientos.id'))
    fecha = db.Column(db.Date) 
    total = db.Column(db.Integer)

    def __init__(self,id_odontologo, id_tratamiento, fecha, id_paciente, total):
        self.id_odontologo= id_odontologo
        self.id_tratamiento  = id_tratamiento
        self.fecha = fecha
        self.id_paciente = id_paciente
        self.total = total
        

        with app.app_context():
            db.create_all()

class HistorialesSchema(ma.Schema):
    class Meta:
        fields = ('id','id_paciente', 'id_odontologo', 'id_tratamiento', 'total', 'fecha')