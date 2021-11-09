# Put your app in here.
from flask import Flask, request
app = Flask(__name__)

from operations import add, sub, mult, div

@app.route('/add')
def add_request():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)
# Int reuqired because a and b are passed in as strings, and result needs to be converted back into a string

@app.route('/sub')
def sub_request():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def mult_request():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def div_request():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)

##########

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)