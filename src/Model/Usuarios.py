from config.db import db,app,ma 

class Users(db.Model):
    __tablename__= "tblusuarios"    
    
    
    id = db.Column(db.Integer,primary_key=True)
    full_name= db.Column(db.String(200))    
    Email= db.Column(db.String(200))
    telefono= db.Column(db.Integer)
    especialidad= db.Column(db.String(200))
    jornada= db.Column(db.String(200))
    password= db.Column(db.String(200))
    cedula= db.Column(db.String(200))
    id_roles = db.Column(db.Integer, db.ForeignKey('tblrolesusuarios.id'))
    
    def __init__(self,full_name,Email,telefono,especialidad,jornada,password,cedula,id_roles):
       self.full_name= full_name
       self.Email= Email
       self.telefono= telefono
       self.especialidad= especialidad
       self.jornada= jornada
       self.password= password
       self.cedula= cedula
       self.id_roles = id_roles
       
       with app.app_context():
           db.create_all()

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','full_name','Email','telefono','especialidad','jornada','password','cedula', 'id_roles')
        
    
    
    
    
