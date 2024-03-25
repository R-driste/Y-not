from flask import render_template, url_for, Flask, request

app = Flask(__name__)
grou = ['hi','bye','hey']

@app.route("/")
def home():
    return render_template("ht.html", GROUPS=grou)

if __name__ == "__main__":
    app.run(debug=True)