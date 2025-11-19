from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    num = random.randint(1, 101)
    return render_template('index.html', n = num)

if __name__ == '__main__':
    app.run(debug=True)