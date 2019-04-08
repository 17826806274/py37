import pymysql


st = pymysql.connect(user="root",password="123456",host="47.102.153.44",port=3306,db="wzf",charset="utf8")
cursor =st.cursor()

a = cursor.execute('SELECT * FROM student')

