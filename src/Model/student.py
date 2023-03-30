from config.db import db, app, ma 

class tblstudent(db.Model):
    __tablename__ = "tblstudent"

    
    id  = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.integer)
    Nombres = db.column(db.string(50))
    Apellidos = db.column(db.string(50))
    Formacion = db.column(db.string(50))
    num_ficha = db.column(db.integer)
    nom_instructorencar = db.column(db.string(50))
    Genero = db.column(db.string(50))
    Telefono = db.Column(db.Integer)
    Nombre_usuario = db.column(db.string)
    Contraseña = db.Column(db.Text)
    Rep_contraseña = db.Column(db.Text)
    
with app.app_context():
    db.create_all()

class StudentSchema(ma.Schema):
    class Meta:
        fields = ()