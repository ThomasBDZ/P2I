from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/admin")
def admin():
	return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

@app.route("/for")
def forr():
    return render_template("for.html")


@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/inherit")
def inherit():
    return render_template("inherit.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/list")
def liste():
    return render_template("list.html")

if __name__ == "__main__":
	app.run(debug=True)
