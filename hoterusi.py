from flask import Flask,render_template,request, redirect, url_for
from logic import Search,Top,Registration,Login

app = Flask(__name__)

module_define = [Search.search, Top.top, Registration.Regi,Login.log]

for apps in module_define:
         app.register_blueprint(apps)

if __name__ == '__main__':
    app.run()