from config.db import db, app, ma 

class Libros(db.Model):
    __tablename__ = "tbllibros"

    
    id  = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    pais = db.Column(db.String(50))
    ano_publicado = db.Column(db.Date)
    copias = db.Column(db.Integer)
    estado = db.Column(db.String(50))
    ubicacion = db.Column(db.String(50))
    id_deta_cat = db.Column(db.Integer)
    id_autor = db.Column(db.Integer)
    id_editoral = db.Column(db.Integer, db.ForeignKey('Editoriales.id'))
    id_proov = db.Column(db.Integer, db.ForeignKey('proveedores.id'))
    

    def __init__(self, titulo, pais, ano_publicado, copias, estado, ubicacion, id_deta_cat, id_autor, id_editoral, id_proov):
        self.titulo = titulo
        self.pais = pais
        self.ano_publicado = ano_publicado
        self.copias = copias
        self.estado = estado
        self.ubicacion = ubicacion
        self.id_deta_cat = id_deta_cat
        self.id_autor = id_autor
        self.id_editoral = id_editoral
        self.id_proov = id_proov
        
        

        
    
with app.app_context():
    db.create_all()

class LibrosSchema(ma.Schema):
    class Meta:
        fields = ('id','titulo','pais', 'ano_publicado', 'copias', 'estado', 'ubicacion', 'id_deta_cat', 'id_autor', 'id_editoral', 'id_proov')