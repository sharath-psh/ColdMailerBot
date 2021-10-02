import sqlite3

conn = sqlite3.connect('mails_db.db')

conn.execute('''CREATE TABLE sentMails
         (
         ID INTEGER PRIMARY KEY AUTOINCREMENT,
         Domain           TEXT ,
         Mail            VARCHAR(50)  ,
         Success        TEXT);''')