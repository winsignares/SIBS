from config.db import db,app,ma 

class Users(db.Model):
    __tablename__= "Usuarios"    
    
    
<<<<<<< HEAD
    
=======
>>>>>>> 140045de6847f9c61fd0b61a0970976b3ca10416
    id = db.Column(db.Integer,primary_key=True)
    full_name= db.Column(db.String(200))
    Email= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    especialidad= db.Column(db.String(200))
    jornada= db.Column(db.String(200))
    direccion= db.Column(db.String(200))
<<<<<<< HEAD
    id_solicitudes= db.Column(db.Integer,db.Foreingkey('tbSolicitudes.id'))
=======
>>>>>>> 140045de6847f9c61fd0b61a0970976b3ca10416
    
    def __init__(self,full_name,Email,telefono,especialidad,jornada,direccion):
       self.full_name= full_name
       self.full_name= Email
       self.full_name= telefono
       self.full_name= especialidad
       self.full_name= jornada
       self.full_name= direccion
       
       with app.app_context():
           db.create_all()

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','full_name','Email','telefono','especialidad','jornada','direccion')
        
    
    
    
    
