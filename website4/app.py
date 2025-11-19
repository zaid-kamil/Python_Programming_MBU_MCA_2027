from flask import Flask

app  = Flask(__name__)

# temporary data storage
products = {
    1: {
        'name': "HP Laptop",
        'price': 49799.99,
    },
    2: {
        'name': "Dell Laptop",
        'price': 38199.99,
    },
    3: {
        'name': "Lenovo Laptop",
        'price': 55999.99,
    },
}

@app.route('/')
def home():
    return "Welcome to the Laptop Store!"

@app.route('/browse/<int:pid>')
def browse(pid):
    product = products.get(pid)
    if product:
        return f"Product: {product['name']}, Price: ${product['price']}"
    else:
        return "Product not found."
    
if __name__ == '__main__':
    app.run(debug=True)