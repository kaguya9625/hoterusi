from flask import Blueprint, render_template,request, redirect, url_for, session
from logic import func
import ast

re_can = Blueprint('re_can', __name__,template_folder='templates',static_folder='./static')

@re_can.route('/reservation_cancel',  methods=['GET', 'POST'])
def reservation_cancel():
    if request.method == 'POST':
        reser = request.form['reser']
        reser = ast.literal_eval(reser)
    return render_template('reservation_cancel.html',re = reser)

# @re_con.route('/reservation_cancel/confirm',  methods=['GET', 'POST'])
# def reservation_confirm():
#     if request.method == 'POST':
#         reser = request.form['reser']
#         reser = ast.literal_eval(reser)
#     # return render_template('reservation_cancel.html',re = reser)
#     return "a"