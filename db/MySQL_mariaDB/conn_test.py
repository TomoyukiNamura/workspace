# -*- coding: utf-8 -*-

import MySQLdb

def conn_f():
    con = MySQLdb.connect(
        user    = "test",       # "your username",
        passwd  = "test",       # "your password",
        host    = "127.0.0.1",  # "localhost",
        port    = 3307,
        db      = "test",       # "todo_app",
        charset = "utf8"
    ) 
    # cursor = con.cursor() # カーソルの取得    
    return con  
    
# Debug 
if conn_f():
    print("接続成功")
else:
    print("接続失敗")
