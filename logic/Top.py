from flask import Blueprint, render_template,request, redirect, session

top = Blueprint('top', __name__,template_folder='templates',static_folder='./static')

@top.route('/')
def topppage():
    member_name = session.get('member_name')
    member_id = session.get('member_id')

    if member_name and member_id:
        login = True
    else:
        login = False


    return render_template('Toppage.html', member_name=member_name, member_id=member_id, login=login)

