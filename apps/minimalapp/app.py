from flask import Flask, render_template, url_for, request, redirect, flash
from email_validator import validate_email, EmailNotValidError
app = Flask(__name__)
app.config["SECRET_KEY"] = "aiueo12345ABC"


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


@app.route("/contact")
def contact():
    """contact."""
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    """contact completed."""
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # validation
        is_valid = True
        if not username:
            flash("ユーザ名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式が不正です")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # メール送信

        # contactエンドポイントにリダイレクト
        flash("お問い合わせありがとうございました")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
