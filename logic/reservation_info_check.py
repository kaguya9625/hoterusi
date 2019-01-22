from flask import Blueprint, render_template,request, redirect, url_for

re_ch = Blueprint('re_ch', __name__,template_folder='templates',static_folder='./static')

@re_ch.route('/reservation_check')
def reservation_check():
    return render_template('reservation_check.html')