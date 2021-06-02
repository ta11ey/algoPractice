from flask import Flask
from . import algos
app = Flask(__name__)

@app.route("/")
def sortLinkedListBy_insertionSort():
    return f'{algos.insertionSort()}'

