from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    productos = db.relationship('Producto', backref='categoria', lazy='dynamic')

    def __repr__(self):
        return f'<Categoria {self.nombre}>'

class Tienda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    productos = db.relationship('Producto', backref='tienda', lazy='dynamic')

    def __repr__(self):
        return f'<Tienda {self.nombre}>'

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    comprada = db.Column(db.Boolean, default=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    tienda_id = db.Column(db.Integer, db.ForeignKey('tienda.id'), nullable=False)

    def __repr__(self):
        return f'<Producto {self.nombre}>'
