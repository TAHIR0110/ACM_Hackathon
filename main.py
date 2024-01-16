from flask import render_template

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


app.run(debug=True)