from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_worl():
    return "<h1>Daniel ama Juliana!</h1>"
