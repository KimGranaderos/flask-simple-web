from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Kim Granaderos' Blog"
    return render_template("index.html", title=title)


@app.route('/about')
def about():
    title = "About Kim Granaderos"
    names = ["John", "Mary", "Wes", "Sally"]
    return render_template("about.html", names=names, title=title)
