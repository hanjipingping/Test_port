# _*_coding:utf-8_*_
# @time :2020/11/24 11:57 上午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :handel_sql.py
# @software PyCharm
import pymysql
from Common.INI_setting import config
import time
class connect_sql():
    def __init__(self,host,port,user,password):
        self.sql_object = pymysql.connect(

            host = host,
            port = port,
            user= user,
            password = password,
            cursorclass = pymysql.cursors.DictCursor,
            charset = 'utf8'

)
        self.cur = self.sql_object.cursor()

    def find_data(self,sql):
        self.sql_object.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data


sql_data = connect_sql(host= config.get("mysql",'host'),
                       port=eval(config.get('mysql','port')),
                       user=config.get('mysql','user'),
                       password= config.get('mysql','password')
                       )





