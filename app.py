from flask import Flask
from algos import sorted
app = Flask(__name__)

@app.route("/")
def hello_friend():
    return sorted().val

