from config.db import db, app, ma 

class Libros(db.Model):
    __tablename__ = "tbllibros"

    
    id  = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    id_autor = db.Column(db.Integer, db.ForeignKey('tblautores.id'))
    pais = db.Column(db.String(50))
    id_Categoria = db.Column(db.Integer, db.ForeignKey('tblcategorias.id'))
    id_proovedor = db.Column(db.Integer, db.ForeignKey('tblproveedores.id'))
    ano_publicado = db.Column(db.Date)
    editoral = db.Column(db.String(100))
    ubicacion = db.Column(db.String(50))
    estimado = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    estado = db.Column(db.String(50))

    def __init__(self, titulo, id_autor, pais, id_Categoria, id_proovedor, ano_publicado, editoral, ubicacion, estimado, cargo, estado):
        self.titulo = titulo
        self.id_autor = id_autor
        self.pais = pais
        self.id_Categoria = id_Categoria
        self.id_proovedor = id_proovedor
        self.ano_publicado = ano_publicado
        self.editoral = editoral
        self.ubicacion = ubicacion
        self.estimado = estimado 
        self.cargo = cargo 
        self.estado = estado 
        
    
with app.app_context():
    db.create_all()

class LibrosSchema(ma.Schema):
    class Meta:
        fields = ('id','titulo', 'id_autor', 'pais', 'id_Categoria', 'id_proovedor', 'ano_publicado', 'editoral', 'ubicacion', 'estimado', 'cargo' 'estado')