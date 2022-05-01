from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """URLと実行する関数のマッピング."""
    return "Hello, World!"
