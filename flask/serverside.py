
from flask import Flask,render_template

application=Flask(__name__)

@application.route("/")
def homepage():
    return render_template("home.html")
    
@application.route("/Angus")
def message1():
    return render_template("Angus.html")

@application.route("/William")
def message2():
    return render_template("William.html")

@application.route("/Thompson")
def message3():
    return render_template("Thompson.html")

@application.route("/login")
def message4():
    return render_template("Login.html")

@application.route("/timestable/<num>")
def printing(num):
    return render_template("timestable.html", T=int(num))

@application.route("/index")
def message5():
    return render_template("index.html")
    
application.run(debug=True)