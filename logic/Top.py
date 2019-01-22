from flask import Blueprint, render_template,request, redirect, url_for

top = Blueprint('top', __name__,template_folder='templates',static_folder='./static')

@top.route('/')
def topppage():
    return render_template('Toppage.html')

