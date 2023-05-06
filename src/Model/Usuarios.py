from config.db import db, app, ma


class Users(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True)
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

        with app.app_context():
            db.create_all()


class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'Email', 'telefono',
                  'especialidad', 'jornada', 'id_roles', 'cedula', 'password')
