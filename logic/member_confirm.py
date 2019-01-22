from flask import Blueprint, render_template,request, redirect, url_for

mem_con = Blueprint('mem_con', __name__,template_folder='templates',static_folder='./static')

@mem_con.route('/member_confirm')
def member_confirm():
    return render_template('member_confirm.html')