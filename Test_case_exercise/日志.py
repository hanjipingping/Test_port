# _*_coding:utf-8_*_
# @time :2020/11/20 8:25 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :日志.py
# @software PyCharm
import logging
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
#创建一个日志收集器
def test():
    test_log = logging.getLogger('hanjiping')
    # 设置日志输出等级
    test_log.setLevel("DEBUG")
    # 定义一个日志输出渠道
    put_log = RotatingFileHandler(filename='test.log' + '.log', mode='a',
                                  maxBytes=20,
                                  backupCount=5,
                                  encoding="utf-8")

    put_log.setLevel("DEBUG")

    test_log.addHandler(put_log)

    formats = logging.Formatter("%(asctime)s--%(filename)s--%(lineno)d--%(levelname)s--%(name)s--%(message)s")
    put_log.setFormatter(formats)

test_log.debug('zheshi debug')
test_log.error('哈哈哈哈')
test_log.warning("waring")




