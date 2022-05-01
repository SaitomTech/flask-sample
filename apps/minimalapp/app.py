from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """URLと実行する関数のマッピング."""
    return "This is a first page."


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    """hello."""
    return f"hello, {name}"


@app.route("/name/<name>")
def show_name(name):
    """Render sample."""
    return render_template("index.html", name=name)
