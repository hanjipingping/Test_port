# _*_coding:utf-8_*_
# @time :2020/11/23 2:37 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :test_json_path.py
# @software PyCharm
from jsonpath import jsonpath
import json
#获取json中的数据，jsonpath
with open("/Users/hanjiping/Desktop/番茄视频banner","r",encoding= 'utf-8') as f:
    res = json.load(f)
json_data = jsonpath(res,"$..url_list[0].url")
print(json_data)