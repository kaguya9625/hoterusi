import sqlite3

#ホテルを検索するsql文の実行
#引数 検索時の地名
#0件の場合 msg（ホテルがありません)と返す
#それ以外の場合配列で結果を返す
def searchhotel(locate):
    msg = 'ホテルがありません'
    conn = sqlite3.connect('hoterusi.db')
    c = conn.cursor()
    sql = 'select * from hotel where hotel_addres like ?;'
    c.execute(sql,('%'+ locate,+'%'))
    result = c.fetchall()
    if result == '':
        return msg
    else:
        return result
    c.close()
    conn.close()