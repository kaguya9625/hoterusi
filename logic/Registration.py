from flask import Blueprint, render_template,request, redirect

Regi = Blueprint('Regi', __name__,template_folder='templates',static_folder='./static')

@Regi.route('/Registration')
def Registration():
    return render_template('Registration.html')

@Regi.route('/Registration/confirm', methods=['GET', 'POST'])
def Registration_confirm():
    if request.method == 'POST':
        member_info = request.form.to_dict('member_info')
        # member_info = request.form['member_info[]']
        # member_info = dict(member_info)
        # member_info = member_info['fname']
    return render_template('member_confirm.html', member_info=member_info)