from flask import Flask, render_template, request, redirect, url_for

app = flask(__name__)

@app.route('/',methods = ("GET","POST"))
def index():
    return render_template("index.html")

if __main__ == __name__ :
    app.run();
