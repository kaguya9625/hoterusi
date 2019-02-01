from flask import Blueprint, render_template,request, redirect, url_for #フラスコ、ブループリント、レンダーテンプレートなどのインポート
from sqlite3 import connect, Row #DB接続やDBの生データ抽出のためのライブラリ
from pprint import pprint
import sqlite3
from logic import func
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
        cur.execute("SELECT hotel_name FROM hotel WHERE hotel_id=?", (record["hotel_id"],)) #hotel_idを基に検索をかけるselect文実行
        hotels = cur.fetchone() #select文で取得したレコｰﾄﾞを格納
        hotel_name = hotels['hotel_name'] #ホテル名を変数に格納
        reservation_info[i] = record_dict #予約テーブルのレコードをそのまま入れる
        reservation_info[i]['hotel_name'] = hotel_name #ホテル名をキーと共に新規追加

        if 'room_type_name' not in reservation_info[i]:
            reservation_info[i]['room_type_name'] = '' #新しいkeyを定義しておく

        reservation_info[i]['room_type_name'] += func.roomtype_get(record['room_type_1'])
        reservation_info[i]['room_type_name'] += func.roomtype_get(record['room_type_2'])

        if record['room_type_3']:
            reservation_info[i]['room_type_name'] += func.roomtype_get(record['room_type_3'])

        i += 1


    test = "room_types"
    return render_template('reservation_info_check.html', reservations=reservation_info, test=test)
    # return render_template('reservation_info_check.html', test=test)