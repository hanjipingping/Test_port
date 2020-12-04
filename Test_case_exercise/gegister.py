# _*_coding:utf-8_*_
# @time :2020/11/30 6:03 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :gegister.py
# @software PyCharm

import requests
from Common.INI_setting import config
json_data = {


    "mobile_phone":"15011466717",
    "pwd":"12345678"
}
headers =eval(config.get('request','headers'))
response = requests.request(method='post',headers = headers,json = json_data,url = "http://api.lemonban.com/futureloan/member/register" )
print(response.json())