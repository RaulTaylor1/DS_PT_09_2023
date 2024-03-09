from flask import Flask, jsonify, render_template
import numpy as np
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def indexo():
    return "<h1>Hello World!</h1>"

@app.route('/rodrigo')
def index1():
    return "<h1>wasa<h1>"


@app.route("/user/<name>/<int:index>")
def index(name, index):
    mylist = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
    mydict = {'key': 'valor'}
    mytuple = ('tuple1', 'tuple2', 'tuple3', 'tuple4')
    return name, index, mylist, mydict, mytuple