from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Teachers(db.Model):
    name = db.Column(db.String(50), primary_key = True, nullable = False)
    course = db.Column(db.String(50), nullable = False)
    average = db.Column(db.Double, nullable = False)
    rating = db.Column(db.Integer, nullable = False)

with app.app_context():
    db.create_all()

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

@app.route("/courses/BAH")
def BAH():
    return "False"

app.run(debug=True)