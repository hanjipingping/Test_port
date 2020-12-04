# _*_coding:utf-8_*_
# @time :2020/11/22 10:31 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :yaml_.py
# @software PyCharm
import yaml
#获取yaml文件中的数据
with open('/Users/hanjiping/PycharmProjects/Port_test01/Conf/Yaml.yaml','r',encoding='utf-8') as f :
    data = yaml.load(f,Loader=yaml.FullLoader)

print(data)