from flask import Flask
from flask import session,request,render_template, url_for, redirect, Response
import os, cv2

app = Flask(__name__)
app.secret_key = "lavaryss"

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/results')
def results():
    results = []
    x = os.listdir('./static/images')
    return render_template("results.html", x)

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0")
