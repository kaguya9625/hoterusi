import sqlite3


#sql文を実行する関数
#第一引数にsql文、第二引数にparamを渡す
def paramconnect(sql,param):
    conn = sqlite3.connect('hoterusi.db')
    c = conn.cursor()
    c.execute(sql,param)
    result = c.fetchall()
    conn.close()
    return result

#sql文を実行する関数
#sql文を渡すのみ
def dbconnect(sql):
    conn = sqlite3.connect('hoterusi.db')
    c = conn.cursor()
    c.execute(sql)
    result = c.fetchall()
    conn.close()
    return result


#ホテルを検索するsql文の実行
#引数 検索時の地名
#0件の場合 msg（ホテルがありません)と返す
#それ以外の場合配列で結果を返す
def searchhotel(locate):
    msg = 'ホテルがありません'
    sql = 'select * from hotel where hotel_address like ?'
    locate1 = (locate + '%',)
    result = paramconnect(sql,locate1)
    if result == '':
        return msg
    else:
        return result
#ホテルのルーム情報を取得する関数
#引数hotelid
def selecthotel(hotelid):
    sql = 'select * from room where hotel_id like ?'
    tp_hotel =(hotelid,)
    result = paramconnect(sql,tp_hotel)
    return result

#ルームタイプを取得する関数
#引数無し
def roomdata():
    sql = 'select * from room_type'
    result = dbconnect(sql)
    return result

#room_typeの番号に対応するルームタイプ名を取得する関数
#引数は一つ
def roomtype_get(room_type_num):
    conn = sqlite3.connect('hoterusi.db')
    c = conn.cursor()
    c.execute("SELECT room_type_name FROM room_type WHERE room_id=?", (room_type_num,))
    result = c.fetchone()[0]
    return result

#指定したホテルを取得する関数
#引数はホテルID
def hotel(hotelid):
    sql = 'select * from hotel where hotel_id like ?'
    tp_hotel = (hotelid,)
    result = paramconnect(sql,tp_hotel)
    return result

#特定のカラムの値を基に特定のテーブルからデータを検索する関数
#引数は　テーブル名、　カラム名、　カラムの値
def table_search(table, col, value):
    conn = sqlite3.connect('hoterusi.db')
    c = conn.cursor()
    c.row_factory = sqlite3.Row #生データを取得するように設定（これによってカラム名も取得できる）
    sql = 'SELECT * FROM ' + table + ' WHERE '+ col + '=' +value
    c.execute(sql)
    result = c.fetchall()[0]
    return result