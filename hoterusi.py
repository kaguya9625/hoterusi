from flask import Flask,render_template,request, redirect, url_for
from logic import Search,Top,Registration,Login,member_confirm,reservation_cancel,reservation_confirm,reservation_info_check,Roomchoice

app = Flask(__name__)

module_define = [
                Search.search,
                Top.top,
                Registration.Regi,
                Login.log,
                reservation_cancel.re_can,
                reservation_confirm.re_con,
                reservation_info_check.re_ch,
                member_confirm.mem_con,
                Roomchoice.choice
                ]

for apps in module_define:
         app.register_blueprint(apps)

if __name__ == '__main__':
    app.run()