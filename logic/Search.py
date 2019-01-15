from flask import Blueprint, render_template,request, redirect, url_for, flash
from tkinter import messagebox
import sqlite3

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
        searchconditions = '場所 ' + locate + '日時 ' + checkin +' ~ '+ checkout + '客室数 ' + roomnumber +'部屋' + '大人:' + adult +'人'+ '子供:'+child +'人'+ '予算' + money + '万円'
        if locate == '' or checkin == '' or checkout == '' or roomnumber == '' or adult == '' or child == '' or money == '':
            return render_template('searcherror.html',msg='記入されてない事項があります')
        else:
            if checkin < checkout: 
                return render_template('SearchResult.html',locate=locate,CheckIn=checkin,CheckOut=checkout,roomnumber=roomnumber,adult=adult,child=child,range=money,searchconditions=searchconditions)
            else:
                return render_template('searcherror.html',msg='誤った情報があります。')    
    else:
        return render_template('SearchTop.html')



