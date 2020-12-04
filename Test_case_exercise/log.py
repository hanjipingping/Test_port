# _*_coding:utf-8_*_
# @time :2020/11/19 1:44 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :log.py
# @software PyCharm

import logging
#定义一个收集器
my_log = logging.getLogger('Test')
#设置收集等级
my_log.setLevel('DEBUG')



#设置一个输出到控制台的输出渠道
put = logging.StreamHandler()
#设置输出等级
put.setLevel("DEBUG")
#将输出渠道加载到收集器中
my_log.addHandler(put)

my_log.debug('11111')


#创建一个文件收集器
#创建文件收集器
file_put= logging.FileHandler("hanjiping_log.log","a",encoding="utf-8")
#设置文件收集器等级
file_put.setLevel("DEBUG")
my_log.addHandler(file_put)



#设置日志输出格式
formats = logging.Formatter("%(asctime)s--%(filename)s--%(lineno)d--%(levelname)s--%(name)s--%(message)s")
file_put.setFormatter(formats)
put.setFormatter(formats)

my_log.debug("123456789")

