from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


#class Courses(db.Model):


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/courses")
def cur_courses():
    return render_template('index1.html')

@app.route("/timetable")
def cur_timetable():
    return "True"

@app.route("/courses/MDM4U1")
def MDM4U1():
    return "False"

@app.route("/courses/MCV4U1")
def MCV4U1():
    return "False"

@app.route("/courses/MHF4U1")
def MHF4U1():
    return "False"

@app.route("/courses/ICS4U1")
def ICS4U1():
    return "False"

app.run(debug=True)