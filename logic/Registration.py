from flask import Blueprint, render_template,request, redirect
from logic import func
import sqlite3

Regi = Blueprint('Regi', __name__,template_folder='templates',static_folder='./static')

@Regi.route('/Registration')
def Registration():
    return render_template('Registration.html')

@Regi.route('/Registration/confirm', methods=['GET', 'POST'])
def Registration_confirm():
    if request.method == 'POST':
        # member_info = {}
        # member_info = request.form.getlist('fname')
        member_info = request.form.to_dict()
        # member_info = request.form['member_info']
        # member_info = dict(member_info)
        # member_info = member_info['postcode']
        if member_info['gender'] == "1":
            gender = '男'
        elif member_info['gender'] == "2":
            gender = '女'
        elif member_info['gender'] == "3":
            gender = 'その他'
            
        member_info['birth_date'] = member_info['year']+'-'+member_info['month']+'-'+member_info['day']
        member_info['phone_number'] = member_info['tel1']+'-'+member_info['tel2']+'-'+member_info['tel3']

        del member_info['year'],member_info['month'],member_info['day'],member_info['tel1'],member_info['tel2'],member_info['tel3'],member_info['pass2']

        sql = ''.join([
        'INSERT INTO `user` (',
        ', '.join('`' + k + '`' for k in member_info.keys()),
        ') VALUES (',
        ', '.join('`' + v + '`' for v in member_info.values()),
        ')'])

        # func.dbconnect(sql)

    return render_template('member_confirm.html', member_info=member_info, sql=sql, gender=gender)


@Regi.route('/Registration/confirm/true',  methods=['GET', 'POST'])
def Registration_confirm_true():
    if request.method == 'POST':
        sqlite = request.form['sql']
    return render_template("test.html", sql=sqlite)
        # func.dbconnect(sqlite)
    #     conn = sqlite3.connect('hoterusi.db')
    #     c = conn.cursor()
    #     c.execute(sqlite)

    # return redirect('/')
    # return render_template("test.html", sql=sqlite)