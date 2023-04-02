from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__,template_folder='template')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/b2")
def b2():
    return render_template('b2.html')

@app.route("/b3")
def b3():
    return render_template('b3.html')

@app.route("/b4")
def b4():
    return render_template('b4.html')

if __name__=="__main__":
    app.run(debug=True)