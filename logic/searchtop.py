from flask import Blueprint, render_template

searchtop = Blueprint('searchtop', __name__,template_folder='templates',static_folder='./static')

@searchtop.route('/search')
def hello():
    return render_template('searchTop.html')
