from flask import Blueprint, render_template,request, redirect, url_for #フラスコ、ブループリント、レンダーテンプレートなどのインポート
from sqlite3 import connect, Row #DB接続やDBの生データ抽出のためのライブラリ
from pprint import pprint
import sqlite3
from collections import defaultdict

nested_dict = lambda: defaultdict(nested_dict) #辞書型を定義するやつ


re_ch = Blueprint('re_ch', __name__,template_folder='templates',static_folder='./static') #ブループリントのパーツとして定義

@re_ch.route('/reservation_info_check') #関数の開始
def reservation_info_check():
    con = sqlite3.connect('hoterusi.db') #hoterusi.dbに接続
    con.row_factory = sqlite3.Row #生データを取得するように設定（これによってカラム名も取得できる）
    cur = con.cursor() #おまじない

    member_id = 1; #ホントはセッションから取得する予定

    cur.execute("SELECT * FROM reservation WHERE member_id=?", (member_id,)) #member_idを基に検索をかける
    reservation = cur.fetchall() #検索の結果出力されたデータを連想配列？で格納

    i = 0
    reservation_info = {}
    # reservation_info = nested_dict()

    for record in reservation:
        record_dict = dict(record)
        # cur.execute("SELECT hotel_name FROM hotel WHERE hotel_id=?", (record["hotel_id"],)) #hotel_idを基に検索をかける
        reservation = []
        reservation_info[i] = record_dict
        i += 1

    test = reservation_info
    return render_template('reservation_info_check.html', reservations=reservation_info, test=test)
    # return render_template('reservation_info_check.html', test=test)