from config.db import db,app,ma 

class Users(db.Model):
    __tablename__= "Usuarios"    
    
    
    id = db.Column(db.Integer,primary_key=True)
    full_name= db.Column(db.String(200))
    Email= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    especialidad= db.Column(db.String(200))
    jornada= db.Column(db.String(200))
    direccion= db.Column(db.String(200))
    
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
        
    
    
    
    
