from app import app

@app.route("/")
def index():
    return "<h1>hello world from Python Flask!</h1></h2>New Line</h2>"