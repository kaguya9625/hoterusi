from flask import Blueprint, render_template,request, redirect, url_for
from logic import func
from logic.Search import reservation

choice = Blueprint('choice', __name__,template_folder='templates',static_folder='./static')

@choice.route('/Roomchoice',methods=['GET','POST'])
def Roomchoice():
    if request.method == 'POST':
        hotelid = request.form['hotel']
        #予約情報ストに追加　　チェックイン日、チェックアウト日、大人、子供　ホテルID
        reservation.append(hotelid)
        price = func.selecthotel(hotelid)
        roomtype = func.roomdata()
        roomlist = []
        for item in price:
            if item[1] == 1:
                roomlist.append('シングル')
            if item[1] == 2:
                roomlist.append('ツイン')
            if item[1] == 3:
                roomlist.append('ダブル')
        list = []
        for room, type in zip(roomlist, price):
            setlist = [room,type]
            list.append([setlist[0],setlist[1][2],setlist[1][1]])
        return render_template('Roomchoice.html',hotelinfo = list , info = price)
    else:
        return render_template('Roomchoice.html')