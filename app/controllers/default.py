from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/post")
def post():
    return render_template('post.html')

#404 handler
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Esta pagina no existe</h1><br><a href='/'>Volver a pagina inicial</a>"