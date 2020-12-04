# _*_coding:utf-8_*_
# @time :2020/11/22 9:50 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :handel_path.py
# @software PyCharm

import os
#获取绝对路径
res = os.path.abspath(__file__)

#获取父级路径
os.path.dirname(__file__)
#项目的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取配置文件路径
INI_PATH = os.path.join(BASE_DIR,'Conf')

#case的目录
CASE_DIR = os.path.join(BASE_DIR,"TestCase")
#报告目录
REPORT_DIR= os.path.join(BASE_DIR,'Report')
#日志路径
LOG_DIR = os.path.join(BASE_DIR,'Log')
#Data路径
DATA_DIR = os.path.join(BASE_DIR,"Data")



