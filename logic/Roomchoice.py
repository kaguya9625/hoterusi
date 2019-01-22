from flask import Blueprint, render_template,request, redirect, url_for

choice = Blueprint('choice', __name__,template_folder='templates',static_folder='./static')

@choice.route('/Roomchoice')
def Roomchoice():
    return render_template('Roomchoice.html')