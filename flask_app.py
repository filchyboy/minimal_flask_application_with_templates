# flask_app.py - a minimal flsk application

# import flask module
from flask import Flask, render_template

# initiate application
app = Flask(__name__)


# define route
@app.route("/")
# attach a function to that route using render_template
# from the flask module
def root():
    return render_template("home.html")
