from flask import Flask
from . import algos
app = Flask(__name__)

@app.route("/")
def hello_friend():
    return f'{algos.sorted().val} test'

