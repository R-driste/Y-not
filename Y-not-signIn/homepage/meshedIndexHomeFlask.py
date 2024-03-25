from flask import Flask, render_template, url_for, request, redirect
import pymongo
from hehe import *

app = Flask(__name__)
mylist = []
id = 1

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


def getInput():
  userName = request.form['uname']
  password = request.form['psw']
  print(userName)
  return userName + " and " + password
  
l = ['hi','hey']

client = pymongo.MongoClient('mongodb+srv://dristiroy:gpH8AhvZ8NwnJDHo@dristicluster.86w9fpu.mongodb.net/')
print(client.list_database_names())
db = client['users']
dcOne = db['public']
dcTwo = db['private']
dcThree = db['coords']

app = Flask(__name__)
grou = ['hi','bye','hey']

@app.route("/")
def home():
    return render_template("explore.html", GROUPS=grou)

@app.route("/pinpoint")
@app.route("/pinpoint/")
def pin():
    return render_template("pinpoint.html")

@app.route("/recievejavascriptcoordsjbfouefouesfeuofsu")
def recievecoord(id=1):
    mylist = [request.args.get("lat"),request.args.get("lng")]
    updateCoord(dcThree, mylist[0],mylist[1], 1)
    return redirect(url_for(home))

if __name__ == "__main__":
    app.run(debug=True)