from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "hello this is my miin toadge "

@ap.route("/<>")
def user(name):
    return f"halief {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()