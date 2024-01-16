from flask import render_template

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

app.run(debug=True)