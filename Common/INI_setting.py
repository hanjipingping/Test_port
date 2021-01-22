# _*_coding:utf-8_*_
# @time :2020/11/22 10:05 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :INI_setting.py
# @software PyCharm
from configparser import ConfigParser

from Common.handel_path import INI_PATH
import os

# #创建一个文件配置解析器
# cfg = ConfigParser()
# #读取配置文件,get读取的都是字符串
# cfg.read("/Users/hanjiping/PycharmProjects/Port_test01/Conf/config.ini",encoding="utf-8")
# print(cfg.get("logging",'level'))
#
#
#
# #配置文件写入数据
# cfg.set('logging','name','dddddddd')
# with open("/Users/hanjiping/PycharmProjects/Port_test01/Conf/config.ini",'w',encoding="utf-8") as f:
#     cfg.write(f)


class Config(ConfigParser):
    #初始化直接读取文件数据
    def __init__(self,file_name,encoding= "utf-8"):
        super().__init__()
        self.read(file_name,encoding=encoding)
#创建config对象，获取ini中的数据，直接调用即可
config = Config(os.path.join(INI_PATH,"config.ini"))




