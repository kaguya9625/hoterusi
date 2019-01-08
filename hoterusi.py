from flask import Flask,render_template,request, redirect, url_for
from logic import searchtop

app = Flask(__name__)

app.register_blueprint(searchtop.searchtop)

if __name__ == '__main__':
    app.run()