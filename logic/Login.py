from flask import Flask, Blueprint, render_template,request, redirect, url_for, session
from sqlite3 import connect, Row
import os

log = Blueprint('log', __name__,template_folder='templates',static_folder='./static')


@log.route('/login', methods=['GET','POST'])
def login():
    return render_template('Login.html')

@log.route('/valid' , methods=['GET','POST'])
def valid():

    if request.method == 'POST':

        #パラメータを取得

        mail = request.form['mail']
        passwd = request.form['pass']
        if mail == "" or passwd == "":
            return  '<dialog open>データを入力してください<br><a href="/login">戻る</a><dialog>'
        con = connect('hoterusi.db')
        #取得する値をディクショナリに
        con.row_factory = Row
        cur = con.cursor()
        #データの存在を確認
        cur.execute('SELECT * FROM user WHERE mail_address=?',(mail,))
        result = cur.fetchall()
        con.close()
        if len(result)!=0:
            for row in result:
                if passwd == row['password']:
                    session['username'] = request.form['mail']
                    session['member_id'] = row['member_id']
                    return redirect('/')
        return '<dialog open>メールアドレスかパスワードが間違っています<br><a href="/">戻る</a></dialog>'