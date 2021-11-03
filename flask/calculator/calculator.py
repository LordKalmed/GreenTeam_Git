from flask import Flask, render_template, request

application=Flask(__name__)

@application.route("/")
def homepage():
    return render_template("/inputform.html")

@application.route("/senddata",methods=["POST"])
def processform():
    return render_template("results.html", no1=int(request.form["num1"]), no2=int(request.form["num2"]))

application.run(debug=True)
 