from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calc():
    num1 = float(request.form['a'])
    num2 = float(request.form['b'])
    if 'add' in request.form:
        result = num1 + num2
    elif 'sub' in request.form:
        result = num1 - num2
    else:
        result = 'Invalid operation'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)