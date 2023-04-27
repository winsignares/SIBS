from config.db import db, app, ma

class Users(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer)
    nombre = db.Column(db.String(200))
    fecha_nacimiento = db.Column(db.Date)
    correo = db.Column(db.String(200))
    password = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
    direccion = db.Column(db.String(200))
    fecha_registro = db.Column(db.Date)
    fecha_actualizacion = db.Column(db.Date)
    id_roles = db.Column(db.Integer, db.ForeignKey('tblrolesusuarios.id'))

    def __init__(self, cedula, nombre, fecha_nacimiento, correo, password, telefono, direccion, fecha_registro, id_roles):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.password = password
        self.telefono = telefono
        self.direccion= direccion
        self.fecha_registro = fecha_registro
        self.id_roles = id_roles

        with app.app_context():
            db.create_all()


class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cedula', 'nombre', 'fecha_nacimiento', 'correo', 'password', 'telefono', 'direccion'
                  'fecha_registro', 'fecha_actualizacion', 'id_roles')


