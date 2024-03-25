from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("frontPage.html")

@app.route("/sign-in")
def sign_in():
  return render_template("signin.html")

@app.route("/sign-up")
def sign_up():
  return render_template("signup.html")

@app.route("/profile")
def profile():
  return render_template("ht.html")

@app.route("/ourMission")
def explore():
  return render_template("mission.html")

'''
def getInput():
  if request.method == "POST":
       # getting input with name = fname in HTML form
       user_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       password = request.form.get("lname") 
       return "Your name is "+first_name + last_name
  return render_template("form.html")
  '''

def getInput():
  userName = request.form['uname']
  password = request.form['psw']
  print(userName)
  return userName + " and " + password


if __name__ == "__main__":
  app.run()