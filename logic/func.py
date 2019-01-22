import sqlite3

def adduser():
    conn = sqlite3.connect('hoterusi.db')
    c = conn.cursor()
    c.excute