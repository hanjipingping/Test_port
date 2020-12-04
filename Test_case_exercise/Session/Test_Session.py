# _*_coding:utf-8_*_
# @time :2020/11/23 3:21 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :Test_Session.py
# @software PyCharm
#在登录前，设置一个session对象，通过session对象来进行请求
import requests

session = requests.session()
res = session.post("登录地址")

#请求完之后，不用登录，可直接访问其他接口