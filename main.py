from flask import Flask, request, render_template, g, redirect, url_for, session, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "super secret key"
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index-previous.html')

if __name__ == '__main__':
    app.run(debug = True)
