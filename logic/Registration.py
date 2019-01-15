from flask import Blueprint, render_template,request, redirect, url_for

Regi = Blueprint('Regi', __name__,template_folder='templates',static_folder='./static')

@Regi.route('/Registration')
def Registration():
    return render_template('Registration.html')