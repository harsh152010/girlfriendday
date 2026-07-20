from flask import Flask,redirect,request,render_template,session,url_for,Response,render_template

app = Flask(__name__)


#login page
@app.route("/")
def login():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def lock():
    password = request.form.get("password")

    if password == "rachnaharsh":
        return render_template("wel.html")

    return render_template(
        "index.html",
        error="Secret word galat hai darling 💭"
    )
app.run(debug=True)