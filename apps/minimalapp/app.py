from flask import Flask, render_template, url_for

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


with app.test_request_context():
    # /
    print(url_for("index"))

    # /hello/world
    print(url_for("hello-endpoint", name="world"))

    # /name/taro?page=taro
    print(url_for("show_name", name="taro", page="1"))
