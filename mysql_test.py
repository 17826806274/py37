import pymysql


db = pymysql.connect(user="root",password="123456",host="47.102.153.44",port=3306,db="wzf",charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 执行sql查询操作
sql_select = "select version()"
cursor.execute(sql_select)

# 使用fetchone()获取单条数据
data = cursor.fetchone()
print("DB version is : %s" % data)
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()