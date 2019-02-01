from flask import Blueprint, render_template,request, redirect, url_for
from logic.Search import reservation
from logic import func

re_con = Blueprint('re_con', __name__,template_folder='templates',static_folder='./static')

@re_con.route('/reservation_confirm',methods=['GET','POST'])
def reservation_confirm():
    if request.method == 'POST':
        room1 = request.form['1']
        room2 = request.form['2']
        room3 = request.form['3']
        hotelid = int(reservation[4])
        roomdata = func.selecthotel(hotelid)
        money = room1 * roomdata[0][2] + room2 * roomdata[1][2] + room3 * roomdata[2][2]
        #予約情報ストに追加　　チェックイン日、チェックアウト日、大人、子供　ホテルID　合計金額
        reservation.append(money)
        hoteldata = func.hotel(reservation[4])
        #予約情報ストに追加　　チェックイン日、チェックアウト日、大人、子供　ホテルID 合計金額　ホテル名
        reservation.append(hoteldata[1])
        #予約情報ストに追加　　チェックイン日、チェックアウト日、大人、子供　ホテルID 合計金額　ホテル名、部屋タイプ
        room = ''
        if room1 != 0:
            room +='シングル'
        if room2 != 0:
            room +='ツイン'
        if room3 != 0:
            room += 'ダブル'
        reservation.append(room)
        return render_template('reservation_confirm.html',list = reservation)
    