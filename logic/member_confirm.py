from flask import Blueprint, render_template,request, redirect, url_for

log = Blueprint('log', __name__,template_folder='templates',static_folder='./static')

@log.route('/login')
def login():
    return render_template('Login.html')