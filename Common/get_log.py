# _*_coding:utf-8_*_
# @time :2020/11/21 9:19 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :get_log.py
# @software PyCharm

import logging
import os
from logging.handlers import TimedRotatingFileHandler
from Common.handel_path import LOG_DIR


class GetLog:

    @staticmethod
    def get_log():
        """定义一个日志收集器"""
        my_log= logging.getLogger('hanjiping_log')
        '''设置日志收集等级'''
        my_log.setLevel("DEBUG")

        '''设置日志输出器'''
        log_put = TimedRotatingFileHandler(filename=os.path.join(LOG_DIR,'log.txt'),
                                           when='s',
                                           interval=5,
                                           backupCount=100,
                                           encoding="utf-8")
        '''设置日志输出等级'''
        log_put.setLevel("DEBUG")

        my_log.addHandler(log_put)
        #设置日志的=输出格式
        formats = logging.Formatter("%(asctime)s--%(filename)s--%(lineno)d--%(levelname)s--%(name)s--%(message)s")
        #把输出格式加载到日志输出器中
        log_put.setFormatter(formats)
        return my_log



#创建一个日志收集器对象，直接调用对象即可
mylog_test = GetLog().get_log()







