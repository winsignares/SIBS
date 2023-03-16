from config.db import db,app,ma 

class Ussers(db.Model):
    __tablename__= "Usuarios"
    
    
    
    id = db.column(db.Integer,primary_key=True)
    full_name= db.column(db.String(200))
    Email= db.column(db.String(200))
    telefono= db.column(db.Integer)
    especialidad= db.column(db.String(200))
    jornada= db.column(db.String(200))
    direccion= db.column(db.String(200))
    id_solicitudes= db.column(db.Integer,db.Foreingkey('tbSolicitudes.id'))
    
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
        
    
    
    
    
