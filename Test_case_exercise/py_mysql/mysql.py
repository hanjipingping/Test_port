# _*_coding:utf-8_*_
# @time :2020/11/23 9:46 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :mysql.py
# @software PyCharm
import pymysql

#连接数据库
sql_data = pymysql.connect(
    host = "api.lemonban.com",
    port = 3306,
    user = "future",
    password = "123456",
    charset= "utf8",
    #把查询出的数据转化为字典格式
    cursorclass = pymysql.cursors.DictCursor

)


#创建一个游标对象

cur = sql_data.cursor()


#执行sql语句
cur.execute('SELECT * FROM futureloan.member WHERE mobile_phone=15011466719')
#查询一条数据
data = cur.fetchone()
print(data)


#pymysql操作数据库，默认开启事务，设计改动数据，提交事务才能生效
sql_data.commit()




