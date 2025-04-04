from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home_page():
    """
        Homepage
    """
    return "Hello, World!"

@app.route("/map")
def map_route():
    return render_template("map.html");

if __name__ == "__main__":
    app.debug = True
    app.run()
    