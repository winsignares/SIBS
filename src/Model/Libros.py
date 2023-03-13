from config.db import db, app, ma 

class Libros(db.Model):
    __tablename__ = "tbllibros"

    
    id  = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    autor = db.Column(db.String(50))
    categoria = db.Column(db.String(50))
    cantidad = db.Column(db.Integer)
    descripcion = db.Column(db.String(50))
    

    def __init__(self, titulo, autor, categoria, cantidad, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.cantidad = cantidad
        self.descripcion = descripcion
        
    
with app.app_context():
    db.create_all()

class LibrosSchema(ma.Schema):
    class Meta:
        fields = ('id','titulo','autor','categoria','cantidad','descripcion')