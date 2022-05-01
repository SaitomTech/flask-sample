from crypt import methods
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """URLと実行する関数のマッピング."""
    return "This is a first page."


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    """hello."""
    return f"hello, {name}"
