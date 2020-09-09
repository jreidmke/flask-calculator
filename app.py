# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/')
def home_page():
    return """Welcome to math. To perform an operation, input your information in the URL <br><br> EX: '/add?a=1&b=2' will return an output of 'Your sum is 3.'<br><br> Operation Codes: <br> Subtraction: '/sub' <br> Multiplication: '/mult' <br> Division: '/div'"""

@app.route('/add')
def show_sum():
    a = int(request.args['a'])
    b = int(request.args['b'])
    s = operations.add(a, b)
    return f"<h1>Your sum is {s}"

@app.route('/sub')
def show_diff():
    a = int(request.args['a'])
    b = int(request.args['b'])
    s = operations.sub(a, b)
    return f"<h1>Your difference is {s}"

@app.route('/mult')
def show_prod():
    a = int(request.args['a'])
    b = int(request.args['b'])
    s = operations.mult(a, b)
    return f"<h1>Your product is {s}"

@app.route('/div')
def show_div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    s = operations.div(a, b)
    return f"<h1>Your dividend is {s}"