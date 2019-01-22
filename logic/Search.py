from flask import Blueprint, render_template,request, redirect, url_for, flash
import sqlite3
from logic import func
from datetime import datetime

search = Blueprint('search', __name__,template_folder='templates',static_folder='./static')


#検索画面Topを表示
@search.route('/searchtop',methods=['GET','POST'])
def searchtop():
    return render_template('SearchTop.html')
#検索結果を表示
@search.route('/searchresult',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        #検索条件を取得
        locate = request.form['locate']
        checkin = request.form['CheckIn']
        checkout = request.form['CheckOut']
        roomnumber = request.form['roomnumber']
        adult = request.form['adult']
        child = request.form['child']
        money = request.form['range']
        hotel = func.searchhotel(locate)
        hit = len(hotel)
        #今日の日付を取得
        now = datetime.now()
        #チェックイン日をdatetimeに変換
        checkin_date = datetime.strptime(checkin,'%Y-%m-%d')
        #検索条件の表示のための文章生成
        searchconditions = '場所 ' +''+ locate + '日時 ' + checkin +' ~ '+ checkout + '客室数 ' + roomnumber +'部屋' + '大人:' + adult +'人'+ '子供:'+child +'人'+ '予算' + money + '万円'
        
        #非記入欄があった場合errorを吐き searcherror画面に遷移。
        if locate == '' or checkin == '' or checkout == '' or roomnumber == '' or adult == '' or child == '' or money == '':
            return render_template('searcherror.html',msg='記入されてない事項があります')
        else:
            #チェックイン日がチェックアウト日より小さい場合検索条件を検索結果画面に渡す。
            if checkin < checkout and roomnumber != 0 and now < checkin_date and checkin != checkout and adult != 0: 
                return render_template('SearchResult.html',locate=locate,CheckIn=checkin,CheckOut=checkout,roomnumber=roomnumber,adult=adult,child=child,range=money,searchconditions=searchconditions,hit=hit,hotellist=hotel)
            #チェックイン日がチェックアウト日より大きい場合searcherror画面に遷移
            else:
                return render_template('searcherror.html',msg='誤った情報があります。')    
    else:
        return render_template('SearchTop.html')



