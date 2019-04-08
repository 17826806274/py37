# -*- coding:utf-8 -*-

import pymysql
import time


db = pymysql.connect(user="root",password="123456",host="47.102.153.44",port=3306,db="wzf",charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
def local_time():
    return (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

def insert(num_A):
    time_T = str(local_time())
    sql_add1 = """INSERT INTO SERVER1(A,T)
             VALUES  ('%s','%s')
             """%(str(num_A) ,time_T)
    print(num_A,time_T)
    cursor.execute(sql_add1)
    db.commit()
    time.sleep(60)
x = 0
while True:
    x+=1
    insert(x)
