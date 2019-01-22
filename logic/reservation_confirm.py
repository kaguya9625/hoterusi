from flask import Blueprint, render_template,request, redirect, url_for

re_con = Blueprint('re_con', __name__,template_folder='templates',static_folder='./static')

@re_con.route('/reservation_confirm')
def reservation_confirm():
    return render_template('reservation_confirm.html')