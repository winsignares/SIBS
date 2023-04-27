from config.db import db, app, ma
<<<<<<< HEAD
=======

>>>>>>> b062fb0dc3a9fe8c53b036aa078866481a84077d

class Users(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True)
<<<<<<< HEAD
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
=======
    full_name = db.Column(db.String(200))
    Email = db.Column(db.String(200))
    telefono = db.Column(db.Integer)
    especialidad = db.Column(db.String(200))
    jornada = db.Column(db.String(200))
    id_roles = db.Column(db.Integer, db.ForeignKey('tblrolesusuarios.id'))
    cedula = db.Column(db.String(200))
    password = db.Column(db.String(200))

    def __init__(self, full_name, Email, telefono, especialidad, jornada, id_roles, cedula, password):
        self.full_name = full_name
        self.Email = Email
        self.telefono = telefono
        self.especialidad = especialidad
        self.jornada = jornada
        self.id_roles = id_roles
        self.cedula = cedula
        self.password = password
>>>>>>> b062fb0dc3a9fe8c53b036aa078866481a84077d

        with app.app_context():
            db.create_all()


class UsuariosSchema(ma.Schema):
    class Meta:
<<<<<<< HEAD
        fields = ('id', 'cedula', 'nombre', 'fecha_nacimiento', 'correo', 'password', 'telefono', 'direccion'
                  'fecha_registro', 'fecha_actualizacion', 'id_roles')


=======
        fields = ('id', 'full_name', 'Email', 'telefono',
                  'especialidad', 'jornada', 'id_roles', 'cedula', 'password')
>>>>>>> b062fb0dc3a9fe8c53b036aa078866481a84077d
