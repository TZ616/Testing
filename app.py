from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/courses")
def cur_courses():
    return "Hello"

@app.route("/timetable")
def cur_timetable():
    return "True"

app.run(debug=True)