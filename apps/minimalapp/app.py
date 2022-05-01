from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """URLと実行する関数のマッピング."""
    return "This is a first page."


@app.route("/hello")
def hello():
    """hello."""
    return "hello, world"
