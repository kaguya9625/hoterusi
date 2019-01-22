from flask import Blueprint, render_template,request, redirect, url_for

re_can = Blueprint('re_can', __name__,template_folder='templates',static_folder='./static')

@re_can.route('/reservation_cancel')
def reservation_cancel():
    return render_template('reservation_cancel.html')