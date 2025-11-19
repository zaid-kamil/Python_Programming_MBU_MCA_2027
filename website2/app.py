from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Website 2!"

@app.route('/about')
def about():
    return "This is the About page of Website 2."

@app.route('/contact')
def contact():
    return "Contact us at contact@website2.com"

@app.route('/blog')
def blog():
    return '''
    <h1>Blog Page</h1>
    <p> There are no blog posts yet. Stay tuned! </p>
    '''

if __name__ == '__main__':
    app.run(debug=True)