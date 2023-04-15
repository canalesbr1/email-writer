from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',methods = ("GET","POST"))
def index():
    if request.method == "POST":
        field = request.form["usertext"]
    result = requests.args.get("resultc")
    return render_template("index.html",result = result)

if __name__ == '__main__' :
    app.run();


def promptgen(text):
    return text
