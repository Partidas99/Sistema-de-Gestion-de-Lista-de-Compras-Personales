from flask import Flask, request, jsonify
from models import db, Categoria, Tienda, Producto

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///compras.db'
db.init_app(app)

@app.route('/categoria', methods=['POST'])
def crear_categoria():
    data = request.get_json()
    nueva_categoria = Categoria(nombre=data['nombre'])
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoría creada exitosamente'}), 201


@app.route('/categoria', methods=['GET'])
def leer_categorias():
    categorias = Categoria.query.all()
    return jsonify([{'id': cat.id, 'nombre': cat.nombre} for cat in categorias])


@app.route('/categoria/<int:id>', methods=['PUT'])
def actualizar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    data = request.get_json()
    categoria.nombre = data['nombre']
    db.session.commit()
    return jsonify({'mensaje': 'Categoría actualizada exitosamente'})


@app.route('/categoria/<int:id>', methods=['DELETE'])
def eliminar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({'mensaje': 'Categoría eliminada exitosamente'})


@app.route('/tienda', methods=['POST'])
def crear_tienda():
    data = request.get_json()
    nuevo_tienda = Tienda(nombre=data['nombre'], correo=data['correo'])
    db.session.add(nuevo_tienda)
    db.session.commit()
    return jsonify({'mensaje': 'Tienda creado exitosamente'}), 201


@app.route('/tienda', methods=['GET'])
def leer_tiendas():
    tiendas = Tienda.query.all()
    return jsonify([{'id': prov.id, 'nombre': prov.nombre, 'correo': prov.correo} for prov in tiendas])


@app.route('/tienda/<int:id>', methods=['PUT'])
def actualizar_tienda(id):
    tiemda = Tienda.query.get_or_404(id)
    data = request.get_json()
    tienda.nombre = data['nombre']
    tienda.correo = data['correo']
    db.session.commit()
    return jsonify({'mensaje': 'Tienda actualizado exitosamente'})


@app.route('/tienda/<int:id>', methods=['DELETE'])
def eliminar_tienda(id):
    tienda = Tienda.query.get_or_404(id)
    db.session.delete(tienda)
    db.session.commit()
    return jsonify({'mensaje': 'Tienda eliminado exitosamente'})


@app.route('/producto', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Producto(
        nombre=data['nombre'],
        cantidad=data['cantidad'],
        comprada=data['comprada'],
        categoria_id=data['categoria_id'],
        tienda_id=data['tienda_id']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto creado exitosamente'}), 201


@app.route('/producto', methods=['GET'])
def leer_productos():
    productos = Producto.query.all()
    return jsonify([
        {
            'id': prod.id,
            'nombre': prod.nombre,
            'cantidad': prod.cantidad,
            'comprada': prod.comprada,
            'categoria': prod.categoria.nombre,
            'tienda': prod.tienda.nombre
        } for prod in productos
    ])


@app.route('/producto/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = Producto.query.get_or_404(id)
    data = request.get_json()
    producto.nombre = data['nombre']
    producto.cantidad = data['cantidad']
    producto.comprada = data['comprada']
    producto.categoria_id = data['categoria_id']
    producto.tienda_id = data['tienda_id']
    db.session.commit()
    return jsonify({'mensaje': 'Producto actualizado exitosamente'})


@app.route('/producto/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado exitosamente'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')