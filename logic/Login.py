from flask import Flask,render_template,request, redirect, url_for, session
from sqlite3 import connect, Row
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

###########################################################################

@app.route('/' , methods=['GET','POST'])
def index():

    return render_template('Toppage.html')
###########################################################################

@app.route('/search' , methods=['GET','POST'])
def search():

    return render_template('SearchTop.html')
###########################################################################

@app.route('/toppage' , methods=['GET','POST'])
def toppage():
    return render_template('Toppagelogin.html')
###########################################################################

@app.route('/login', methods=['GET','POST'])
def login():

###########################################################################

    return render_template('Login.html')
@app.route('/valid' , methods=['GET','POST'])
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
                    return redirect(url_for('toppage'))
        return '<dialog open>メールアドレスかパスワードが間違っています<br><a href="/">戻る</a></dialog>'


if __name__ == '__main__':
    app.debug = True
    app.run()
