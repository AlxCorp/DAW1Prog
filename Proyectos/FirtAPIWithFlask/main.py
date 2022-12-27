from flask import Flask, jsonify, request
from products import products
server = Flask(__name__)


@server.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})


@server.route('/products')
def get_products():
    return jsonify(products)


@server.route('/products/<string:product_name>')
def get_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if not products_found:
        return jsonify({"ERROR": "Producto no encontrado"})
    return jsonify(products_found)


@server.route('/products', methods=['POST'])
def add_products():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"RECIBIDO": True, "products": products})


@server.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if not products_found:
        return jsonify({"ERROR": "Producto no encontrado"})
    products_found[0]['name'] = request.json['name']
    products_found[0]['price'] = request.json['price']
    products_found[0]['quantity'] = request.json['quantity']
    return jsonify({
        "message": "Producto Actualizado",
        "product": products_found[0]
    })


@server.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
    products_found = [product for product in products if product['name'] == product_name]
    if not products_found:
        return jsonify({"ERROR": "Producto no encontrado"})
    products.remove(products_found[0])
    return jsonify({
        "message": "Producto Eliminado",
        "product": products
    })


if __name__ == '__main__':
    server.run(debug=True, port=4000)

